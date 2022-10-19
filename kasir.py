from datetime import date
total1 = 0
total2 = 0
totalsemua = 0
diskon = 0
jenis1 = ""
jenis2 = ""
pemesanan = "y"

while pemesanan == "y" :

    print("=== Restoran Makanan & Minuman ===")
    print()

    try:
        nama = str(input("Masukkan Nama Konsumen: "))
        nomer = int(input("Masukkan Nomor Meja: "))

    except:
        print("Input nama harus berupa huruf dan nomer harus berupa angka")
        break

    print()
        
    def pilihan(i):
        switcher = {
                1:'----Rujak Kuah Pindang 7000----',
                2:'----Tipat Cantok 10000----',
                3:'----Ayam Guling 25000----'
             }
        return switcher.get(i,"Masukan Pilihan yang Benar!")

    print("\nMenu Makanan")
    print()

    makanan_menu = ("1. Rujak Kuah Pindang", "2. Tipat Cantok", "3. Ayam Guling", "4. Makanan Kosong")
    makanan_list = [makanan for makanan in makanan_menu if makanan != "4. Makanan Kosong"]
    print(makanan_list)

    nomor = int(input("Masukan Pilihan(berupa angka): "))
    menu = pilihan(nomor)
    print(menu)
    porsi1 = int(input("Berapa Porsi(berupa angka): "))

    if nomor == 1:
        total1 = total1+(porsi1*7000)
        print("Hasilnya = ", total1)
        jenis1 = ("Es Teh Manis")
    if nomor == 2:
        total1 = total1+(porsi1*10000)
        print ("Hasilnya = ", total1)
        jenis1 = ("Es Jeruk")
    if nomor == 3:
        total1 = total1+(porsi1*25000)
        print("Hasilnya = ", total1)
        jenis1 = ("Jus Wortel")

    def pilihan(i):
        switcher={
                1:'----Es Teh Manis 3000----',
                2:'----Es Jeruk 4000----',
                3:'----Jus Wortel 9000----'
             }
        return switcher.get(i,"Masukan Pilihan yang Benar!")

    print("\nMenu Minuman")
    print()

    minuman_menu = ("1. Es Teh Manis", "2. Es Jeruk", "3. Jus Wortel", "4. Minuman Kosong")
    minuman_list = [minuman for minuman in minuman_menu if minuman != "4. Minuman Kosong"]
    print(minuman_list)

    nomor = int(input("Masukan Pilihan(berupa angka): "))
    menu = pilihan(nomor)
    print(menu)
    porsi2 = int(input("Berapa Gelas(berupa angka): "))

    if nomor == 1:
        total2 = total2+(porsi2*3000)
        print("Hasilnya = ", total2)
        jenis2 = ("Es Teh Manis")
    if nomor == 2:
        total2 = total2+(porsi2*4000)
        print("Hasilnya = ", total2)
        jenis2 = ("Es Jeruk")
    if nomor == 3:
        total2 = total2+(porsi2*9000)
        print("Hasilnya = ", total2)
        jenis2 = ("Jus Wortel")
        
    totalsemua = total1+total2 

    if 50000 > totalsemua < 100000:
        diskon = 0.05*totalsemua
    elif 100000 > totalsemua < 250000:
        diskon = 0.10*totalsemua
    elif totalsemua > 250000:
        diskon = 0.15*totalsemua
    else:
        pass

    harga = totalsemua-diskon

    bayar = int(input("Uang yang akan dibayarkan: "))

    kembalian = bayar-harga

    today = date.today()

    print("\n=========================")
    print("======= S T R U K =======")
    print("=========================")

    print("Nama Konsumen :", nama)
    print("Nomer Meja :", nomer)
    print("Menu yang dipesan: ",menu)
    print("Harga pesanan", totalsemua)
    print("Jumlah Makanan: ",porsi1)
    print("Jumlah Minuman: ",porsi2)
    print("Tanggal pesan: ",today.strftime("%d/%m/%Y"))
    print("Diskon: ",diskon)
    print("Harga yang dibayarkan: ",harga)
    print("Uang yang dibayarkan: ",bayar)
    print("Kembalian: ",kembalian)
    print()

    try: 
        loop = str(input("Apakah anda akan membeli kembali? (y/n) : "))

        if loop == "y":
            pass
        elif loop == "n":
            break
        else:
            print("Input hanya dapat berupa huruf y atau n")
            break
    except:
        print("Input hanya dapat berupa huruf y atau n")
