import helper

helper.header("Responsi Sistem Operasi Praktik")

totalRam = int(input("Kapasitas RAM dalam Mb: "))
totalBlok = int(input("Total PetaBit: "))
petabit = helper.hitungPetaBit(helper.konversiRAM(totalRam), totalBlok)

print("\nProgram dijalankan")

ramUntukProgram = int(input("Kapasitas Sistem Operasi : "))
blokTerpakai = helper.hitungPetaBit(helper.konversiRAM(ramUntukProgram), petabit)
program1 = int(input("Kapasitas Program 1 : "))
program2 = int(input("Kapasitas Program 2 : "))
ramTerpakai = helper.ttlRamTerpakai(program1,program2)
ramKosong = helper.ttlRamKosong(ramUntukProgram,ramTerpakai)


print("\nInformasi Management RAM")
print("="*30)

print("Total RAM = ", totalRam , "MB")
print("Total PetaBit = ", totalBlok)
print("Kapasitas per PetaBit adalah ", petabit , "KB per blok" )
print("Total RAM terpakai = ",ramTerpakai)
print("Total RAM tidak terpakai = ",ramKosong)

print("\nBlokTerpakai = ",blokTerpakai)
print("Jumlah blok bernilai 1 = ", blokTerpakai)
print("Jumlah blok bernilai 0 = ", totalBlok - blokTerpakai)