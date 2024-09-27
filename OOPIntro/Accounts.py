"""
    Accounts.py
"""

class Accounts():  # create the class
    def __init__(self, account_number, account_firstname, account_lastname,
                 current_balance, address, email): 
        # self refers to the object itself
        # __init__ is a special and necessary method to make the object
        # __init__ contains the attributes of the object, it is the 'constructor'
        # in order to make the object, we need to pass the attributes through it
        # that is why you have account_number, firstname, etc. as the necessary paremeters preceded by self
    
        self.account_number = account_number
        self.account_firstname = account_firstname
        self.account_lastname = account_lastname
        self.current_balance = current_balance
        self.address = address
        self.email = email

    # methods are basically what an object does (e.g. object car has the methods drive and stop)
    # below are methods for accounts
    def update_address(self, new_address): 
        self.address = new_address
    
    def update_email(self, new_email): 
        self.email = new_email