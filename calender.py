import calendar

def welcome_message():
    print("\n")
    print("+------------------------------------+")
    print("|    Program Menampilkan Kalender    |")
    print("+------------------------------------+")
    print("\t")

def menu():
    print("+------------------------------------+")
    print("|        Menu Program Kalender       |")
    print("+------------------------------------+")
    print("|      1. Mencari Tahun Kabisat      |")
    print("|      2. Mencari Tahun Biasa        |")
    print("|      3. Keluar Dari Program        |")
    print("+------------------------------------+")
    print("\t")

def cek_tahun_kabisat(tahun):
    if tahun % 4 == 0 and (tahun % 100 != 0 or tahun % 400 == 0):
        return True
    else:
        return False 

def main():
    while True:
        welcome_message()
        menu()
        pilih = int(input("Masukan pilihan program diatas : "))
        if pilih == 1:
            tahun_awal = int(input("Masukan tahun awal : "))
            tahun_akhir = int(input("Masukan tahun akhir : "))
            print("\t")
            print("Hasil :")
            print("\t")
            for tahun in range(tahun_awal, tahun_akhir + 1):
                if cek_tahun_kabisat(tahun):
                    print(f"{tahun} ini tahun kabisat")
                else:
                    print(f"{tahun} ini bukan tahun kabisat")
    
        elif pilih == 2:
            tahun = int(input("Masukan tahun : "))
            bulan = int(input("Masukan bulan : "))
            print("\t")
            print("Hasil :")
            print("\t")
            print(calendar.month(tahun, bulan))

        elif pilih == 3:
            print("Anda keluar dari program.")
            break
    
        else:
            print(f"Pilihan yang anda masukan ({pilih}) tidak ada di menu!")


if __name__ == "__main__":
    main()