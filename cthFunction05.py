# Variable global
# Definisi fungsi
total = 0


def sum(arg1, arg2):
    total = arg1 + arg2
    # Total di sini adalh variable lokal
    print("Di dalam fungsi nilai total : ", total)
    return total


# Pemanggilan fungsi sum
sum(10, 20)
print("Di luar fungsi, nilai total : ", total)
