medical_cause = input("Do you have a medical cause? y or n: ")

attendence = int(input("Enter the attendence: "))

if medical_cause == "y":
    print("You can give exam.")

else:
    if attendence >= 75:
        print("You can give exam.")
    else:
        print("You cannot give exam.")