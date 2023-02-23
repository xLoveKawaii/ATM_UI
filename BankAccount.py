# BankAccount.py
# Name: Carman Tran
# Date: November 24, 2022

class BankAccount:
    """Implement methods to accept deposits and make withdrawals"""

    def __init__(self):
        self.balance = 0
        self.transaction = 0

    def Deposit(self, amount):
        """Return deposit"""

        if amount > 0:
            self.balance += amount
            self.transaction += 1
            print("The transaction is successful. New balance: $", self.balance)

        else:
            print("Error; Your amount is less than 0. Try again.")

                
    def Withdraw(self, amount):
        """
         if statement: return true if successful
                    return false if amt is more than balance
        """

        if amount > self.balance:
            print("Error; amount is greater than your balance. Try again")
            
        elif amount <= 0:
            print("Error; amount is less than 0")

        else:
            self.balance -= amount
            self.transaction += 1
            print("The withdrawal is successful. New balance: $", self.balance)

    def getBalance(self):
        """Return balance"""
        print("Your current balance is: $", self.balance)

    def getTransaction(self):
        print("Number of Transaction: ", self.transaction)
