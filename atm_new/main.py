class Atm:
    def __init__(self):
        self.bal=0
        print("welcome to the ATM service")
    def deposit(self):
        amount=int(input("enter deposit amount:"))
        self.bal+=amount
        print("amount sucessfully deposited\n available amount:",amount)
    def withdraw(self):
        amount=int(input("enter withdraw amount:"))
        if self.bal>=amount:
            self.bal-=amount
            print("amount sucessfully withdraw\n available amount:",amount)
        else:
            print("insufficient amount")
    def check_balance(self):
        print("available balance:",self.bal)
    def exit(self):
        print("Thank you using service")

    def Trans(self):
      while True:
        print("""
                        TRANSACTION 
                    *********************
                        Menu:
                        1. Check Balance
                        2. Deposit
                        3. Withdraw
                        4.exit
                    *********************
                    """)
        option = int(input("enter your option:"))
        if option==1:
            Atm.check_balance()
        elif option==2:
            Atm.deposit()
        elif option==3:
            Atm.withdraw()
        elif option==4:
            Atm.exit()
        break

print("========== welcome to axis bank==========")
pin=2129
u_pin=int(input("please enter you pin:"))
username="naresh"
a=Atm()
if pin==u_pin:

    while True:
        print(''' 1.transection
                          2.exit''')
        option=int(input("enter you option:"))
        if option==1:
         a.Trans()
        elif option ==2:
            print("""
        -------------------------------------
       | Thanks for choosing us as your bank |
       | Visit us again!                     |
        -------------------------------------
            """)
            break
        else:
            print("Wrong option")

else:
    print("invailed username or pin")








