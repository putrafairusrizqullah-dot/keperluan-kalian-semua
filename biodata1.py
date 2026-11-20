
# A. Membuat 2 set pembelian
hari_pertama = {"keju", "tepung", "garam", "gula", "coklat"}
hari_kedua = {"garam", "gula", "coklat", "kecap"}

print("A. Pembelian Hari Pertama:", hari_pertama)
print("A. Pembelian Hari Kedua:", hari_kedua)

# B. Menambahkan keju pada pembelian hari kedua
hari_kedua.add("keju")
print("\nB. Setelah menambahkan keju:", hari_kedua)

# C. Mencari barang yang sama pada kedua hari
print("\nC. Barang yang sama:", hari_pertama.intersection(hari_kedua))

# D. Barang yang dibeli hari pertama tetapi tidak hari kedua
print("\nD. Barang hari pertama saja:", hari_pertama.difference(hari_kedua))

# E. Menghapus garam pada pembelian hari pertama
hari_pertama.remove("garam")
print("\nE. Setelah menghapus garam:", hari_pertama)

# F. Barang yang dibeli hari kedua tetapi tidak hari pertama
print("\nF. Barang hari kedua saja:", hari_kedua.difference(hari_pertama))

# G. Mencari barang yang tidak sama pada kedua hari
print("\nG. Barang yang tidak sama:", hari_pertama.symmetric_difference(hari_kedua))

# H. Menampilkan semua pembelian hari pertama
print("\nH. Semua pembelian hari pertama:")
for barang in hari_pertama:
    print("-", barang)

# I. Menampilkan semua pembelian hari kedua
print("\nI. Semua pembelian hari kedua:")
for barang in hari_kedua:
    print("-", barang)
