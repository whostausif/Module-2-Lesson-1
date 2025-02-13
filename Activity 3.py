print("Select your ride: ")
print("1.Car")
print("2.Bike")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("What type of car?")
    print("1.Toyota")
    print("2.BMW")
    choice2 = int(input("Enter your second choice: "))
    if choice2 == 1:
        print("You have selected Toyota.")
    else:
        print("You have selected BMW")

elif choice == 2:
    print("What type of bike?")
    print("1.Scooty")
    print("2.Scooter")
    choice3 = int(input("Enter your second choice: "))
    if choice3 == 1:
        print("You have selected Scooty.")
    else:
        print("You have selected Scooter.")

else:
    print("Wrong number!")
        

