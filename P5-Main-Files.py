# Simple banking system

class Account:

    def __init__(self, balence):
        self.balence = balence

    def debit(self, amount):
        self.balence -= amount
        print("This amount", amount, "is debeted")
        print("Now your balence is Rs.", self.balence)

    def credit(self, amount):
        self.balence += amount
        print(amount, "is credited in your account.")
        print("Now your balence is Rs.", self.balence)


while True:
    init_deposit = input("Please enter your initial deposit: ")

    if init_deposit.isdigit():
        init_deposit = int(init_deposit)
        if init_deposit == 0:
            print("Please enter amount more than zero.")
            continue
        else:
            break
    else:
        print("Invalid Entry")
        continue

print("You initial deposit is Rs.", init_deposit)

a1 = Account(init_deposit)


while True:
    ask = input("Do you want to debit or credit amount?\n").lower()
    if ask == "debit":
        amount = input("How much amount do you want to debit?\n")
        if amount.isdigit():
            amount = int(amount)
            a1.debit(amount)
            break
    elif ask == "credit":
        amount = input("How much amount do you want to credit?\n")
        if amount.isdigit():
            amount = int(amount)
            a1.credit(amount)
            break
    else:
        print("Invalid Entry")
        continue
