def header(judul):
    print("=" * 70)
    print("\t\t", judul)
    print("=" * 70)

def konversiRAM(ttlRAM):
    return ttlRAM * 1024

def hitungPetaBit(ram, blok):
    return ram / blok

def ttlRamTerpakai(program1, program2):
    return program1 + program2

def ttlRamKosong(ramUntukProgram, ramTerpakai):
    return ramUntukProgram - ramTerpakai
