"""
    ATM.py
"""

import random

class ATM():
    serial_number = 0

    def __init__(self, account): # no need to pass serial_number and transactionsummary because
                # we don't need to add arguments for the serial number and transaction summary
        self.serial_number = random.randint(100000, 999999) 
        self.account = account
        self.transactionsummary = [] # list for storing transactions

    def deposit(self, account, amount):
        account.current_balance = account.current_balance + amount
        self.transactionsummary.append(f"Deposited {amount}")
        print("Deposit Complete")
    
    def withdraw(self, account, amount):
        account.current_balance = account.current_balance - amount
        self.transactionsummary.append(f"Withdrew {amount}")
        print("Withdraw Complete")
    
    def check_currentbalance(self, account):
        print(account.current_balance)

    def view_transactionsummary(self):
        if not self.transactionsummary:
            print("No transactions found.")
        else:
            file = open("transactionsummary1.txt", 'w')
            for transaction in self.transactionsummary: # all the items in the list self.transactionsummary are considered
                    # one transaction stored in "transaction" variable created by for loop
                file.write(transaction + '\n') # new line for every transaction
            file.write(f"ATM Serial Number: {self.serial_number}")
            file.close()

    def print_serial_number(self):
        print(f"ATM Serial Number: {self.serial_number}")