# customer_name = "Nick"
# customer_balance = 0.09
# customer_id = 12345678
# val = input("how much do you want o withdrawal")
# amount = float(val)

# if customer_balance > amount:
#     customer_balance = customer_balance - amount

class BankAccount:
    def __init__(self,account_number,customer_name,balance):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance
    
    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("You don't have enough money to withdraw.")
    def display(self):
        print("Account number:",self.account_number)
        print("Customer_name:",self.customer_name)
        print("Balance:",round(self.balance,2))

我在測試這個檔案