print("Welcome to Harshul Bank!")
pin = 2000
chance = 3
balance = 100000
while chance!=0:
    user_pin =int(input("Please enter PIN number"))
    if user_pin!=pin:
        chance-=1
        print("Please try again")
        print(f"You have {chance} number of attempts left")
    else:
        user_choice = input("1 : Check Balance D : Deposit amount  W : Withraw Amount")
        if user_choice == "B":
            print("Your total balance is Rs " + str(balance))
        if user_choice == "D":
            deposit=int(input("Enter the amount you wish to Deposit"))
            t_balance = balance+deposit
            print("Total balnce after depositing Rs" + str(deposit)+ "is Rs" + str(t_balance))

        if user_choice == "W":
            withdraw=int(input("Enter the amount that you wish to withdraw"))
            if withdraw > balance:
                print("Sorry, your account does not have the required amount")
            else:
                t_balance=balance-withdraw
                print("After withdrawing Rs" + str(withdraw) + "your balance is Rs" + str(t_balance))
    user_exit=input("Would you like to exit the ATM? Yes?No" )
    if user_exit== "Yes":
        print("Thank you for using Harshul Bank")
        break
    else:
        continue
