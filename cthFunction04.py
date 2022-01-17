def printInfo(arg1, * vartuple):
    print("Outputnya adalah: ")
    print(arg1)
    for var in vartuple:
        print(var)


# Satu argumen
printInfo(10)

# Empat argumen
printInfo(10, 30, 50, 70)
