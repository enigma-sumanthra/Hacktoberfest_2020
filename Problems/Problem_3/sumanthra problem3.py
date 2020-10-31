a = int(input("Please enter your number a: "))
b = int(input("Please enter your number b: "))
c = int(input("Please enter your number c: "))

if (a**2) == (b**2) + (c**2) :
    print(f'{a},{b},{c}')

elif (b**2) == (a**2) + (c**2):
    print(f'{b},{a},{c}')

elif (c**2) == (a**2) + (b**2) :
    print(f'{c},{a},{b}')


