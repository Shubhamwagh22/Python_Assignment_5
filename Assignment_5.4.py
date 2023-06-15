# Challenge 4: Implement a Banking Account

class Account:

    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance

class SavingsAccount(Account):

    def __init__(self, title = None, balance = 0, interestRate = 0):
        super().__init__(title, balance)
        self.interestRate = interestRate

Account1 = Account("Ashish", 5000)
SavingsAccount = SavingsAccount("Ashish", 5000, 5)
