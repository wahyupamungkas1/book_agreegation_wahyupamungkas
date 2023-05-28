class Buku:
    def __init__(self, judul, pengarang, harga):
        self.judul = judul
        self.pengarang = pengarang
        self.harga = harga


class TokoBuku:
    def __init__(self, nama):
        self.nama = nama
        self.buku = []

    def tambah_buku(self, buku):
        self.buku.append(buku)

    def tampilkan_buku(self):
        print(f"Daftar buku di {self.nama}:")
        if not self.buku:
            print("Tidak ada buku yang tersedia.")
        else:
            for i, buku in enumerate(self.buku, start=1):
                print(f"Buku #{i}")
                print(f"Judul: {buku.judul}")
                print(f"Pengarang: {buku.pengarang}")
                print(f"Harga: {buku.harga}")
                print("----------------------")


# Contoh penggunaan program
# Membuat beberapa objek buku
buku1 = Buku("Laskar Pelangi", "Andrea Hirata", 30000)
Buku2 = Buku("Bumi Manusia", "Pramoedya Ananta Toer",40000)
Buku3 = Buku("Pulang", "Leiala S. Chudori",20000)
Buku4 = Buku("Perahu Kertas", "Dee Lestari",7000)
Buku5 = Buku("Cinta dalam Gelas", "Andrea Hirata",34000)

# Membuat objek toko buku
toko_buku = TokoBuku("Toko Buku Wahyu Pamungkas")

# Menambahkan buku-buku ke dalam daftar buku toko
toko_buku.tambah_buku(buku1)
toko_buku.tambah_buku(Buku2)
toko_buku.tambah_buku(Buku3)
toko_buku.tambah_buku(Buku4)
toko_buku.tambah_buku(Buku5)

# Menampilkan daftar buku yang tersedia di toko
toko_buku.tampilkan_buku()
