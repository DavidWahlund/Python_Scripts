from account import Account

class CheckingAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount

