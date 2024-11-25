# Simple banking system

class Account:

    def __init__(self, balence, account_info):
        self.balence = balence
        self.account_info = account_info

    def debit(self, amount):
        self.balence -= amount
        print("This amount", amount, "is debeted")
        print("Now your balence is", self.balence)

    def credit(self, amount):
        self.balence += amount
        print(amount, "is credited in your account.")
        print("Now your balence is", self.balence)


a1 = Account(10000, 2313)
a1.debit(500)
a1.credit(2000)
