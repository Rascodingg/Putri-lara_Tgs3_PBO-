print("=" * 50)
print("=" + "Kalkulator Luas".center(48) + "=")
print("=" * 50)

while True:
    print("Menu : " + "\n 1. Persegi" + "\n 2. Persegi Panjang" + "\n 3. Lingkaran" + "\n 4. Segitiga" + "\n 5. Keluar")
    pilihan = input("Masukkan Pilihan Anda : ")
    if pilihan == '1':
        while True:
            Sisi = float(input("Masukkan Panjang Sisi : "))
            Luas_Persegi = Sisi * Sisi
            print("Luas Persegi : ")
            print(Luas_Persegi)
            konfirmasi = input("Masih ingin menghitung luas persegi? (y/n) :")
            if konfirmasi == "y":
                print("")
            else:
                break
    elif pilihan == '2':
        while True:
            Panjang = float(input("Masukkan Panjang Persegi : "))
            Lebar = float(input("Masukkan Lebar Persegi : "))
            Luas_Persegi_Panjang = Panjang * Lebar
            print("Luas Persegi Panjang : ")
            print(Luas_Persegi_Panjang)
            konfirmasi = input("Masih ingin menghitung luas persegi panjang? (y/n) :")
            if konfirmasi == "y":
                print("")
            else:
                break
    elif pilihan == '3':
        while True:
            Jari = float(input("Masukkan Jari-Jari Lingkaran : "))
            Luas_Lingkaran = 3.14*Jari*Jari
            print("Luas Lingkaran : ")
            print(Luas_Lingkaran)
            konfirmasi = input("Masih ingin menghitung luas lingkaran? (y/n) :")
            if konfirmasi == "y":
                print("")
            else:
                break
    elif pilihan == '4':
        while True:
            Alas = float(input("Masukkan Panjang Alas : "))
            Tinggi = float(input("Masukkan Tinggi Segitiga : "))
            Luas_Segitiga = 1/2*(Alas*Tinggi)
            print("Luas Segitiga : ")
            print(Luas_Segitiga)
            konfirmasi = input("Masih ingin menghitung luas segitiga? (y/n) :")
            if konfirmasi == "y":
                print("")
            else:
                break
    elif pilihan == '5':
        break
    else:
        print("Perintah Tidak Ditemukan")
        konfirmasi = input("Tekan tombol apapun untuk lanjut.")
        
            

