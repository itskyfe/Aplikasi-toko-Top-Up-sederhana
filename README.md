# Aplikasi Toko Top Up Sederhana
- Nama : Muhammad Rizky Febrianto
- NIM : 2409116045

## Library
```python
from prettytable import PrettyTable
import pwinput
```
Disini saya menggunakan library prettytable untuk memasukkan data ke dalam tabel dan pwinput untuk menampilkan input password dengan tanda bintang (*)

## Memasukkan data ke dalam dictionary
```python
# data akun user
akun = {"username" : "rizky", "password" : "123", "saldo" : 0, "gems" : 0}

# data pilihan skin yang bisa dipilih oleh user
opsi_skin = [
    {"id": "1", "skin" : "alu gojek", "harga" : 50, "keterangan" : "belum dimiliki"},
    {"id": "2", "skin" : "franco bengkel", "harga" : 100, "keterangan" : "belum dimiliki"},
    {"id": "3", "skin" : "layla spectre", "harga" : 500, "keterangan" : "belum dimiliki"},
    {"id": "4", "skin" : "haya oren", "harga" : 100, "keterangan" : "belum dimiliki"},
    {"id": "5", "skin" : "nana gajah", "harga" : 75, "keterangan" : "belum dimiliki"}
]

#data paket gems yang bisa dipilih oeh user
opsi_gems = [
    {"id" : "1", "gems" : 25, "harga" : 50000},
    {"id" : "2","gems" : 50, "harga" : 100000},
    {"id" : "3","gems" : 100, "harga" : 200000},
    {"id" : "4","gems" : 200, "harga" : 400000}
]
```
Disini saya memasukkan data data yang dibutuhkan untuk menjalankan program ke dalam sebuah list yang berisi beberapa dictionary yang berbeda, data tersebut antara lain
- akun user yang terdiri atas username, password, saldo user, dan gems yang dimiliki oleh user
- pilihan skin yang bisa dibeli oleh user beserta harga dan status kepemilikan skin (apakah sudah dimiliki atau belum)
- pilihan paket top up gems yang bisa dipilih oeh user

## Function untuk Menu login
```python
def login():
    # username = rizky
    # password = 123
    user = input("Masukkan username anda : ")
    password = pwinput.pwinput("Masukkan password anda : ")
    if user == akun["username"] and password == akun["password"]:
        print(f"===== Selamat datang {akun["username"]} selamat berbelanja =====")
        menu()
    else:
        print("Akun tidak ada")
```
Dalam menu login ini saya membuat input untuk username dan password, apabila username dan password yang diinputkan user sama dengan yang ada pada data akun user maka program akan  berlanjut. Namun jika username dan password tidak sama maka program akan menampilkan output "Akun tidak ada" dan program berhenti.

## Function untuk Menu utama
```python
def menu():
    while True:
        print("============ Top Up Gacor ============")
        print("[1] Beli Skin")
        print("[2] Cek Saldo")
        print("[3] Cek Gems")
        print("[4] Top Up Saldo")
        print("[5] Top Up Gems")
        print("[6] Keluar")
        print("======================================")
        opsi = int(input("Pilih opsi : "))
        if opsi == 1:
            beli_skin()
        elif opsi == 2:
            cek_saldo()
        elif opsi == 3:
            cek_gems()
        elif opsi == 4:
            top_up()
        elif opsi == 5:
            beli_gems()
        elif opsi == 6:
            print("Terima kasih sudah belanja di aplikasi ini")    
            exit()
        else:
            print("Pilihan anda tidak ada")
```
Dalam fungsi menu utama ini, berisi inputan untuk memilih pilihan-pilihan fitur yang tersedia pada aplikasi ini
- fitur pertama yaitu fitur beli skin
- fitur kedua yaitu fitur cek saldo
- fitur ketiga yaitu fitur cek gems
- fitur keempat yaitu fitur top up saldo
- fitur kelima yaitu fitur beli gems
- fitur keenam yaitu fitur untuk keluar dari program
apabila ada inputan di luar pilihan tersebut maka program akan menampilkan output "Pilihan tidak ada"

## Function untuk Menu beli Skin
```python
def beli_skin():
    print("============================ Menu Skin ============================")
    tabel = PrettyTable()
    tabel.field_names = ["Nomor", "Nama Skin", "Harga Skin (gems)", "Keterangan"]
    for skin in opsi_skin:
        tabel.add_row([skin["id"], skin["skin"], skin["harga"], skin["keterangan"]])
    print(tabel)
    print("===================================================================")
    opsi = input("Masukkan nomor pilihan skin anda (1-5) : ")
    skin_terpilih = next((skin for skin in opsi_skin if skin["id"] == opsi), None) 
    if skin_terpilih["keterangan"] == "belum dimiliki":
        if skin_terpilih["harga"] <= akun["gems"]:
            transaksi = akun["gems"] - skin_terpilih["harga"]
            akun["gems"] = transaksi
            skin_terpilih["keterangan"] = "sudah dimiliki"
            print("Transaksi anda berhasil")
        else:
            print("Gems anda kurang, silahan top up terlebih dahulu")
    else:
        print("Skin sudah dimiliki, silahkan pilih skin yang lain")
    menu()
```
Di fungsi ini akan menampilkan data pilihan skin yang bisa dibeli oleh user beserta harga dan status kepemilikan skin. Data tersebut ditampilkan dalam sebuah tabel mengunakan prettytable. Di fungsi ini juga ada inputan untuk memilih skin apa yang akan dibeli oleh user. Mekanisme pembeliannya, apabila skin yang tertampil sudah dimiliki oleh user maka skin tersebut tidak bisa dibeli lagi dengan menampilkan output "Skin sudah dimiliki, silahkan pilih skin yang lain". Namun sebaliknya jika belum dimiliki, maka program akan melanjutkan pembelian.  
Setelah memastikan bahwa skin yang dibeli itu belum dimiliki oleh user, maka syarat selanjutnya yaitu gems yang dimiliki oleh user harus lebih dari harga skin yang tertampil. Jika syarat tersebut tidak terpenuhi, maka program akan menampilkan output "Gems anda kurang, silahan top up terlebih dahulu".  
Setelah semua syarat terpenuhi maka transaksi akan terjadi dengan mengurangi jumlah gems user dan mengupdate status kepemilikan skin yang tertampil menjadi "sudah dimiliki"

## Function untuk menu cek saldo
```python
def cek_saldo():
    print("============== Cek Saldo ==============")
    print(f"Saldo anda adalah : Rp {akun["saldo"]}")
    print("[1] Top Up Saldo")
    print("[2] Beli Gems")
    print("[3] Kembali")
    print("=======================================")
    opsi = int(input("Pilih opsi anda : "))
    if opsi == 1:
        top_up()
    elif opsi == 2:
        beli_gems()
    elif opsi == 3:
        menu()
```
Dalam fungsi ini akan menampilkan saldo user sekarang dan beberapa pilihan yaitu
- pilihan untuk top up saldo
- pilihan untuk menukarkan saldo menjadi gems
- pilihan untuk kembali ke menu utama

## Function untuk menu cek gems
```python
def cek_gems():
    print("============== Cek Gems ==============")
    print("Anda memiliki Gems sebanyak : ", akun["gems"])
    print("[1] Beli Gems")
    print("[2] Kembali")
    print("======================================")
    opsi = int(input("Masukkan pilihan anda : "))
    if opsi == 1:
        beli_gems()
    elif opsi == 2:
        menu()
    else:
        print("Pilihan tidak ada")
```
Dalam fungsi ini akan menampilkan jumlah gems user sekarang dan beberapa pilihan yaitu
- pilihan untuk menukarkan saldo menjadi gems
- pilihan untuk kembali ke menu utama

## Function untuk menu top up
```python
def top_up():
    print("=============== Top Up ===============")
    print(f"Saldo anda sekarang adalah : Rp {akun["saldo"]}")
    inpt = int(input("Berapakah yang ingin anda top up? : Rp "))
    topup = (akun["saldo"] + inpt)
    akun["saldo"] = topup
    print(f"Saldo anda sekarang adalah : Rp {akun["saldo"]}")
    print("Selamat Top Up anda berhasil")
    menu()
```
Dalam fungsi ini akan menampilkan saldo user sekarang dan membuat input untuk jumlah saldo yang ingin di topup. Setelah itu program akan memproses dan mengupdate saldo user

## Function untuk menu menukarkan saldo menjadi gems
```python
def beli_gems():
    while True:
        print("============== Beli Gems ==============")
        menu_gems = PrettyTable()
        menu_gems.field_names = ["Nomor", "Paket Gems", "Harga"]

        for gem in opsi_gems:
            menu_gems.add_row([gem["id"], gem["gems"], gem["harga"]])

        print(menu_gems)
        print("======================================")
        opsi = int(input("Pilihan nomor paket gems anda : "))
        if opsi == 1:
            if akun["saldo"] < 50000:
                print("Saldo anda kurang, silahan top up terlebih dahulu")
                menu()
            else:
                kurang1 = akun["saldo"] - 50000
                tambah1 = akun["gems"] + 25
                akun["saldo"] = kurang1
                akun["gems"] = tambah1
                print("Transaksi anda berhasil")
        elif opsi == 2:
            if akun["saldo"] < 100000:
                print("Saldo anda kurang, silahan top up terlebih dahulu")
                menu()
            else:
                kurang2 = akun["saldo"] - 100000
                tambah2 = akun["gems"] + 50
                akun["saldo"] = kurang2
                akun["gems"] = tambah2
                print("Transaksi anda berhasil")
        elif opsi == 3:
            if akun["saldo"] < 200000:
                print("Saldo anda kurang, silahan top up terlebih dahulu")
                menu()
            else:
                kurang3 = akun["saldo"] - 200000
                tambah3 = akun["gems"] + 100
                akun["saldo"] = kurang3
                akun["gems"] = tambah3
                print("Transaksi anda berhasil")
        elif opsi == 4:
            if akun["saldo"] < 400000:
                print("Saldo anda kurang, silahan top up terlebih dahulu")
                menu()
            else:
                kurang4 = akun["saldo"] - 400000
                tambah4 = akun["gems"] + 200
                akun["saldo"] = kurang4
                akun["gems"] = tambah4
                print("Transaksi anda berhasil")
        else:
            print("============== Pilihan tidak ada ==============")
        menu()
```
Dalam fungsi ini akan menampilkan data pilihan paket gems yang bisa diukar oleh user, data dimasukkan ke dalam tabel. di fungsi ini juga ada inputan untuk memilih paket gems mana yang bisa dipilih oleh user. Mekanisme penukaran gems yaitu dengan memenugi syarat saldo yang dimiliki user harus lebih dari harga penukaran gems yang tertampil, apabila syarat tersebut tidak terpenuhi maka program akan menampilkan output "Saldo anda kurang, silahan top up terlebih dahulu".  
Apabila syarat tersebut terpenuhi, program akan memproses penukaran saldo menjadi gems dengan mengurangi jumlah saldo sesuai dengan harga gems yang pilih dan menjumlahkan jumlah gems yang ada dengan hasil penukaran gems.

## Awal Kode
```python
login()
```
syntax ini berfungsi untuk memanggil fungsi pertana yang akan tertampil dalam program
