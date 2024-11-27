# Simple banking system

class Account:

    def __init__(self, balence):
        self.balence = balence

    def debit(self, amount):
        if amount > self.balence:
            print("Insufficiant Funds\n")
        else:
            self.balence -= amount
            print("This amount Rs.", amount, "is debeted")
            print("Now your balence is Rs.", self.balence, "\n")

    def credit(self, amount):
        self.balence += amount
        print("Rs.", amount, "is credited in your account.")
        print("Now your balence is Rs.", self.balence, "\n")


while True:
    init_deposit = input("->Please enter your initial deposit: ")

    if init_deposit.isdigit():
        init_deposit = int(init_deposit)
        if init_deposit == 0:
            print("Please enter amount more than zero.\n")
            continue
        else:
            break
    else:
        print("Invalid Entry")
        continue

print("You initial deposit is Rs.", init_deposit, "\n")

a1 = Account(init_deposit)


while True:
    ask = input(
        "->Do you want to 'Debit' or 'Credit' amount?\nor write 'done' to leave.\n").lower()
    if ask == "debit":
        while True:
            amount = input("->How much amount do you want to debit?\n")
            if amount.isdigit():
                amount = int(amount)
                a1.debit(amount)
                break
            else:
                print("Invalid Entry\n")
                continue
    elif ask == "credit":
        while True:
            amount = input("->How much amount do you want to credit?\n")
            if amount.isdigit():
                amount = int(amount)
                a1.credit(amount)
                break
            else:
                print("Invalid Entry\n")
                continue
    elif ask == "done":
        break
    else:
        print("Invalid Entry\n")
        continue

print("Thanks! Have a good day :)")
