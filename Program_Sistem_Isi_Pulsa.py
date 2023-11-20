menu_indosat = {
        '1.Pulsa 5000 =' : 7000,
        '2.Pulsa 10000 =' : 12000,
        '3.Pulsa 15000 =' : 17000,
        '4.Pulsa 25000 =': 26000
}
menu_Tri = {
        '1.Pulsa 5000 =' : 7000,
        '2.Pulsa 10000 =' : 12000,
        '3.Pulsa 15000 =' : 17000,
        '4.Pulsa 25000 =': 26000
}
menu_XL = {
        '1.Pulsa 5000 =' : 7000,
        '2.Pulsa 10000 =' : 12000,
        '3.Pulsa 20000 =' : 22000,
        '4.Pulsa 40000 =': 41000
}
menu_telkomsel = {
        '1.Pulsa 5000 =' : 7000,
        '2.Pulsa 10000 =' : 12000,
        '3.Pulsa 25000 =' : 27000,
        '4.Pulsa 50000 =': 51000
}
import os
os.system("cls")
def pilihan(operator,pulsa, price):
    if operator == "indosat":
        if pulsa == "1":
            harga_bayar = price - 7000
            print(harga_bayar)
        elif pulsa == "2":
            harga_bayar = price - 12000
            print(harga_bayar)
        elif pulsa == "3":
            harga_bayar = price - 17000
            print(harga_bayar)
        elif pulsa == "4":
            harga_bayar = price - 26000
            print(harga_bayar)
        else:
            print("pulsa tidak ada")
    elif operator == "telkomsel":
        if pulsa == "1":
            harga_bayar = price - 7000
            print(harga_bayar)
        elif pulsa == "2":
            harga_bayar = price - 12000
            print(harga_bayar)
        elif pulsa == "3":
            harga_bayar = price - 27000
            print(harga_bayar)
        elif pulsa == "4":
            harga_bayar = price - 51000
            print(harga_bayar)
        else:
            print("pulsa tidak ada")
    elif operator == "Tri":
        if pulsa == "1":
            harga_bayar = price - 7000
            print(harga_bayar)
        elif pulsa == "2":
            harga_bayar = price - 12000
            print(harga_bayar)
        elif pulsa == "3":
            harga_bayar = price - 17000
            print(harga_bayar)
        elif pulsa == "4":
            harga_bayar = price - 26000
            print(harga_bayar)
        else:
            print("pulsa tidak ada")
    elif operator == "XL":
        if pulsa == "1":
            harga_bayar = price - 7000
            print(harga_bayar)
        elif pulsa == "2":
            harga_bayar = price - 12000
            print(harga_bayar)
        elif pulsa == "3":
            harga_bayar = price - 22000
            print(harga_bayar)
        elif pulsa == "4":
            harga_bayar = price - 41000
            print(harga_bayar)
        else:
            print("pulsa tidak ada")
    
print('-' * 41 )
print('      Selamat datang di "FARO CELL"')
print('-' * 41 )
print("daftar menu operator  ")
print("1.indosat\n2.telkomsel\n3.tri\n4.xl\n")
nomor_hp = input("masukan nomor hp : ")
while True:
    operator = input("masukan operator : ")
    if operator == 'indosat':
        print("DAFTAR HARGA PULSA INDOSAT : ")
        for i,j in menu_indosat.items():
              print(i,j)
    elif operator == 'telkomsel':
        print("DAFTAR HARGA PULSA TELKOMSEL : ")
        for j,i in menu_telkomsel.items():
         print(j,i)
    elif operator == 'tri':
        print("DAFTAR HARGA PULSA TRI : ")
        for j,i in menu_Tri.items():
         print(j,i)
    elif operator == 'xl':
        print("DAFTAR HARGA PULSA XL : ")
        for j,i in menu_XL.items():
         print(j,i)
    pulsa = input("masukan pilihan(1/2/3/4):")
    bayar = int(input("masukan nominal bayar : "))

    pilihan(operator, pulsa, bayar)

    stop  = input("apakah ada yang mau di beli lagi?(ya/tidak) ")
    if stop == "tidak":
        print("\n\n~~terimakasih~~") 
        print('-' * 41) 
        break