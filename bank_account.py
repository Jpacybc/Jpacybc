




class BankAccount:
    def __init__(self):
        self.balance = 0.0

    def deposit(self):
        deposited_amount = float(input("Enter the amount to be deposited: "))
        self.balance += deposited_amount
        print("You deposited:", deposited_amount)

    def withdraw(self):
        withdrawn_amount = float(input("Enter the amount to be withdrawn: "))
        try:
            if self.balance >= withdrawn_amount:
                self.balance -= withdrawn_amount
                print("You withdrew:", withdrawn_amount)
            else:
                print("Insufficient funds. Balance:", self.balance)
        except:
            print("Unable to complete the transaction due to insufficient balance")

    def display(self):
        print("Net available Balance:", self.balance)

# Create an object of the BankAccount class
a = BankAccount()

# Calling each function with the object
a.deposit()
a.withdraw()
a.display()