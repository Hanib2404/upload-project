belanja = int(input("Masukan Total Harga Belanja : "))
if belanja >= 100000:
    print("Anda mendapatkan diskon sebesar 15%!!")
    belanja = belanja - (15/100)
    print("Total Belanja anda ", belanja)

elif belanja >= 200000:

    print("Anda mendapatkan diskon sebesar 10%!!")
    belanja = belanja - (10/100)
    print("Total Belanja anda ", belanja)

elif belanja >= 350000:

    print("Anda mendapatkan diskon sebesar 5%!!")
    belanja = belanja - (5 / 100)
    print("Total Belanja anda ", belanja)

else:
    print("Total Belanja anda ", belanja)