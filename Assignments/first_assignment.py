"""Bank ATM console Application"""
balance = 5000
while True:
    print("Enter 1 to Check Your Balance")
    print("Enter 2 to Deposit ")
    print("Enter 3 to Withdrew Money")
    print("Enter 4 to Exit")

    choice = int(input("Enter above given choice to proceed:"))
    if choice == 1:
        print("your current balance is :", balance)
    elif choice ==2:
        amount = float(input("Enter the amount to be deposited"))
        if amount > 0:
            balance = amount + balance
            print("Deposit successful.")
            print("Your New Bank Balance is :",balance)
        else:
            print("enter a valid number")
    elif choice ==3:
        amount = int(input("enter the amount to withdraw : "))
        if amount <= 0:
            print("enter a valid number to withdraw")
        elif amount <= balance:
                balance = balance - amount 
                print("Withdrawal successful")
                print("Your new balance is ",balance )
        else:
                print("insufficient balance")
    elif choice == 4:
        print("Thank you for using this bank")
        break
    else:
        print("Invalid choice. Please select an option from 1 to 4.")