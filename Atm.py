class BankAccount(object):
    def __init__(self, card_number, pin_number, cash_withdraw, balence):
        self.card_number = card_number 
        self.pin_number = pin_number
        self.cash_withdraw = cash_withdraw
        self.balence = balence

    def cardNumber(self):
        print("your card number is 1213213")

    def pinNumber(self):
        print("your pin number is 8712")

    def cashWithdraw(self):
        print("withdraw 100?")

    def balence(self):
        print("your balence is 14000")


bank = BankAccount("1213213", "8712", 100, 14000)
print(bank.cardNumber())
print(bank.pinNumber())
print(bank.cashWithdraw())
print(bank.balence())

print(bank.card_number)

print(bank.pin_number)

print(bank.cash_withdraw)

print(bank.balence)

