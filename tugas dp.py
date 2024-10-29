from prettytable import PrettyTable
import pwinput

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

def top_up():
    print("=============== Top Up ===============")
    print(f"Saldo anda sekarang adalah : Rp {akun["saldo"]}")
    inpt = int(input("Berapakah yang ingin anda top up? : Rp "))
    topup = (akun["saldo"] + inpt)
    akun["saldo"] = topup
    print(f"Saldo anda sekarang adalah : Rp {akun["saldo"]}")
    print("Selamat Top Up anda berhasil")
    menu()

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

login()