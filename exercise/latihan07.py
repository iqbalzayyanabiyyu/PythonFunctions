nama = input("Nama saya : ")
usia = input("Usia saya : ")
uts = int(input("Nilai UTS : "))
uas = int(input("Nilai UAS : "))

print("="*10)
print("Hasil")
print("="*10)


def data(nama, usia):
    print("Halo, saya: ", nama)
    print("Usia saya: ", usia)


data(nama, usia)

total = 0


def nilai(uts, uas):
    total = (uts+uas)/2
    print("Nilai UTS Anda : ", uts)
    print("Nilai UAS Anda : ", uas)
    print("Nilai total : ", total)
    return total


nilai(uts, uas)
