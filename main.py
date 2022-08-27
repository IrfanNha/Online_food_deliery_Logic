# Delivery Food Program

# VARIABEL BERSARANG

harga_ng = 11000
harga_bg = 12000
perkm = 800

# TAMPILAN MENU

print('=================')
print('1.Nasi Goreng')
print('2.Bakmi Goreng')
print('=================')
pil = int(input("Masukkan Pilihan ="))
print('=================')

# PILIHAN NASI GORENG
if pil==1:
    print('\nPilihan Anda Adalah nasi goreng!')
    jarak = float(input('masukkan jarak anda ='))
    if jarak<=0:
        print('angka tidak valid')
        jarak = float(input('masukkan jarak anda ='))

    else:
        if jarak<=31:
            total = harga_ng + (perkm * jarak) + (harga_ng * 0.07)
            print('total belanja anda =',total)
        else:
            if jarak<=21:
                total = harga_ng + (perkm * jarak) + (harga_ng * 0.06)
                print('total belanja anda =', total)
            else:
                if jarak<=11:
                    total = harga_ng + (jarak * perkm) + (harga_ng * 0.05)
                    print('total belanja anda =', total)
                else:
                    if jarak>=31:
                        print('jarak anda terlalu jauh')
#PILIHAN BAKMI GORENG
else:
    if pil==2:
        print('\nPilihan Anda Adalah bakmi goreng!')
        jarak = float(input('masukkan jarak anda ='))
        if jarak <= 0:
            print('angka tidak valid')
            jarak = float(input('masukkan jarak anda ='))

        else:
            if jarak <= 31:
                total = harga_bg + (perkm * jarak) + (harga_bg * 0.07)
                print('total belanja anda =', total)
            else:
                if jarak <= 21:
                    total = harga_bg + (perkm * jarak) + (harga_bg * 0.06)
                    print('total belanja anda =', total)
                else:
                    if jarak <= 11:
                        total = harga_bg + (jarak * perkm) + (harga_bg * 0.05)
                        print('total belanja anda =', total)
                    else:
                        if jarak >= 31:
                            print('jarak anda terlalu jauh')

    else:
        print('\nProgram Berakhir')

print("terimakasih telah berbelanja")