# 📅 Aplikasi Penjadwalan Shift Karyawan (Backtracking Algorithm)

> **Sistem penyusunan jadwal otomatis berbasis web menggunakan Python Flask dan Algoritma Backtracking.**
> *Studi Kasus: Mie Gacoan*

![Python](https://img.shields.io/badge/Python-3.12-blue?style=flat&logo=python)
![Flask](https://img.shields.io/badge/Framework-Flask-green?style=flat&logo=flask)
![Status](https://img.shields.io/badge/Status-Development-orange)

## 📖 Tentang Proyek
Aplikasi ini dirancang untuk menyelesaikan permasalahan **Constraint Satisfaction Problem (CSP)** dalam pembagian jadwal kerja karyawan. Pembuatan jadwal secara manual seringkali memakan waktu dan rentan terjadi konflik (bentrok jadwal).

Aplikasi ini menggunakan **Algoritma Recursive Backtracking** untuk mencari solusi jadwal yang memenuhi semua aturan (constraints) yang telah ditetapkan oleh manajemen toko.

## ✨ Fitur Utama
* **Generate Jadwal Otomatis**: Membuat jadwal mingguan penuh hanya dengan satu klik.
* **Multi-Solusi (Heuristic)**: Menampilkan hingga 10 variasi opsi jadwal yang berbeda (menggunakan *Random Shuffle*).
* **Conflict Detection**: Memastikan tidak ada karyawan yang bekerja double shift di hari yang sama.
* **Visualisasi Beban Kerja**:
    * 🟢 **Hijau**: Beban kerja ringan.
    * 🟠 **Oranye**: Beban kerja normal.
    * 🔴 **Merah**: Overload (Peringatan visual otomatis).
* **Pencarian Jadwal**: Fitur untuk mencari jadwal spesifik per nama karyawan.

## 🧠 Algoritma & Constraints
Algoritma Backtracking bekerja dengan mencoba menempatkan karyawan pada slot shift satu per satu dan melakukan *backtrack* (mundur) jika menemukan jalan buntu/pelanggaran aturan.

**Aturan (Constraints) yang diterapkan:**
1.  **Hard Constraint**: Satu karyawan tidak boleh mengisi 2 shift (misal: Pagi & Siang) di hari yang sama.
2.  **Soft Constraint**: Maksimal shift per minggu adalah 5 shift (jika lebih, akan ditandai merah).
3.  **Kebutuhan Shift**: Setiap shift (Pagi, Siang, Malam) harus terisi oleh karyawan yang tersedia.

## 🛠️ Teknologi yang Digunakan
* **Bahasa Pemrograman**: Python 3.12
* **Web Framework**: Flask (Microframework)
* **Frontend**: HTML5, CSS3 (Custom Card UI), Jinja2 Templating
* **Server**: Werkzeug (Development Server)
## 📂 Struktur Folder
📦 flask-shift-scheduler ┣ 📂 templates ┃ ┗ 📜 index.html # Antarmuka Pengguna (UI) ┣ 📜 app.py # Logika Backtracking & Server Flask ┣ 📜 .gitignore # File yang diabaikan git ┗ 📜 README.md # Dokumentasi Proyek
