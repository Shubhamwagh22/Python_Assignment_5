# Challenge 5: Handling a Bank Account

class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance
    
    def withdrawal(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def getBalance(self):
        return self.balance

class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
            super().__init__(title, balance)
            self.interestRate = interestRate
    
    def interestAmount(self):
        return (self.balance * self.interestRate) //  100

demo1 = SavingsAccount("Ashish", 2000, 5)
Account1 = Account()
Account1.balance = 2000
Account1.deposit (500)
print(Account1.getBalance())
Account1.balance = 2000
Account1.withdrawal (500)
print(Account1.getBalance())
print(demo1.interestAmount())
