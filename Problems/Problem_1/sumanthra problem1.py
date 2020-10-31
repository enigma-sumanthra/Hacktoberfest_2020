i = 0
while i == 0 :
    num = int(input("Enter the number of the day in a week: "))
    if num >=0 and num <= 6:
        if num == 0:
            print("The day is Sunday!")
        elif num == 1:
            print("The day is Monday!")
        elif num == 2:
            print("The day is Tuesday!")
        elif num == 3:
            print("The day is Wednesday!")
        elif num == 4:
            print("The day is Thursday!")
        elif num == 5:
            print("The day is Friday!")
        elif num == 6:
            print("The day is Saturday!")
    else:
        print("Invalid number!!")
    s = input("another one(y/n)? ")
    if s.lower() == "n":
        break

