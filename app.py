from flask import Flask, render_template, request
import random   

app = Flask(__name__)

# ================= DATA TOKO =================
NAMA_TOKO = "Mie Gacoan"
MAX_SHIFT_TETAP = 5  # kebijakan manajemen

HARI = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
SHIFT = ["Pagi", "Siang", "Malam"]

JAM_SHIFT = {
    "Pagi": "08:00 – 14:00",
    "Siang": "14:00 – 20:00",
    "Malam": "20:00 – 02:00"
}

KARYAWAN_ROLE = {
    "Andi": "Kasir",
    "Budi": "Dapur",
    "Citra": "Waiter",
    "Deni": "Kasir",
    "Eka": "Dapur",
    "Fajar": "Waiter"
}

# ================= BACKTRACKING MULTI SOLUSI =================
def buat_jadwal(karyawan_terpilih, max_solusi=10):
    total_slot = len(HARI) * len(SHIFT)
    solutions = []

    def backtracking(pos, jadwal, jumlah_shift):
        if len(solutions) >= max_solusi:
            return

        if pos == total_slot:
            solutions.append((jadwal.copy(), jumlah_shift.copy()))
            return

        # RANDOMIZED BACKTRACKING (INTI PERBEDAAN)
        kandidat = sorted(karyawan_terpilih, key=lambda x: jumlah_shift[x])
        random.shuffle(kandidat)

        for nama in kandidat:
            hari_ke = pos // len(SHIFT)

            # tidak boleh 2 shift di hari yang sama
            if any(jadwal[i] == nama and i // len(SHIFT) == hari_ke for i in range(pos)):
                continue

            # batas maksimal shift
            if jumlah_shift[nama] >= MAX_SHIFT_TETAP:
                continue

            jadwal[pos] = nama
            jumlah_shift[nama] += 1

            backtracking(pos + 1, jadwal, jumlah_shift)

            # ⬅️ BACKTRACK (MUNDUR)
            jadwal[pos] = None
            jumlah_shift[nama] -= 1

    backtracking(
        0,
        [None] * total_slot,
        {k: 0 for k in karyawan_terpilih}
    )

    return solutions

# ================= ROUTE =================
@app.route("/", methods=["GET", "POST"])
def index():
    jadwal_tampil = None
    beban = None
    hasil_cari = None
    nama_cari = None
    warning = None
    karyawan_terpilih = []
    solusi_index = 0
    total_solusi = 0

    if request.method == "POST":
        karyawan_terpilih = request.form.getlist("karyawan")
        solusi_index = int(request.form.get("solusi", 0))

        if len(karyawan_terpilih) == 0:
            warning = "Pilih minimal 1 karyawan."
        elif len(karyawan_terpilih) < 3:
            warning = "Jumlah karyawan belum ideal, jadwal bersifat simulasi."

        if len(karyawan_terpilih) > 0:
            solutions = buat_jadwal(karyawan_terpilih)
            total_solusi = len(solutions)

            if total_solusi > 0:
                hasil, beban = solutions[solusi_index]

                jadwal_tampil = []
                idx = 0
                for _ in HARI:
                    row = []
                    for _ in SHIFT:
                        row.append(hasil[idx])
                        idx += 1
                    jadwal_tampil.append(row)

                nama_cari = request.form.get("cari_nama")
                if nama_cari:
                    hasil_cari = []
                    for i, nama in enumerate(hasil):
                        if nama == nama_cari:
                            hari = HARI[i // len(SHIFT)]
                            shift = SHIFT[i % len(SHIFT)]
                            hasil_cari.append((hari, shift))

    return render_template(
        "index.html",
        toko=NAMA_TOKO,
        hari=HARI,
        shift=SHIFT,
        jam_shift=JAM_SHIFT,
        jadwal=jadwal_tampil,
        beban=beban,
        hasil_cari=hasil_cari,
        nama_cari=nama_cari,
        karyawan_role=KARYAWAN_ROLE,
        karyawan_terpilih=karyawan_terpilih,
        warning=warning,
        total_solusi=total_solusi,
        solusi_index=solusi_index
    )

if __name__ == "__main__":
    app.run(debug=True)
