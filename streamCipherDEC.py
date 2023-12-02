#enkripsi ASCII dengan kode desimal
def enkripsi_ascii(teks):
    hasil_enkripsi = ""
    for karakter in teks:
        kode_ascii = ord(karakter)
        hasil_enkripsi += str(kode_ascii) + " "  # Menambahkan spasi sebagai pemisah
    return hasil_enkripsi

#dekripsi ASCII dengan kode desimal
def deskripsi_ascii(teks):
    teks_kode = teks.split()
    hasil_deskripsi = ""
    for kode in teks_kode:
        karakter = chr(int(kode))
        hasil_deskripsi += karakter
    return hasil_deskripsi

if __name__ == '__main__':
    print ('-----------------------------------')
    print ('    Nama        : Munis Zulhusni   ')
    print ('    Nim         : A11.2021.13693   ')
    print ('    Kelas       : A11.4302         ')
    print ('-----------------------------------')   
    
    option = int (input ('1. Enkripsi\n2. Deskripsi\nPilih Option              : '))
    if option == 1:
        teks = input ('Masukan pesan (Plaintext) : ')
        hasil_enkripsi = enkripsi_ascii(teks)
        print('Hasil Enkripsi            :',hasil_enkripsi)
        
    elif option == 2:
        teks = input ('Masukan pesan (Chipertext): ')
        hasil_deskripsi = deskripsi_ascii(teks)
        print('Hasil Deskripsi           :',hasil_deskripsi)
    else:
        print ('TIDAK VALID! PILIH OPSI LAIN!')    

