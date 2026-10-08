number = int(input("Enter a number: "))

if number == 0:
    print("The number is zero.")
elif number % 2 == 0:
    if number > 0:
        print(f"{number} is a positive even number.")
    else:
        print(f"{number} is a negative even number.")
else:
    if number > 0:
        print(f"{number} is a positive odd number.")
    else:
        print(f"{number} is a negative odd number.")