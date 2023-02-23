# Register.py
# Name: Carman Tran
# Date: November 24, 2022

from BankAccount import *

def main():
    """
        - Create bankaccount object
        - User input for # of transaction
        - User interface: ask for type of transaction
            - deposit, withdraw, check balance
        - Error message (return) if withdraw/deposit money from account
        - Display # of transaction
        - Display Account balance
        - Don't display False transactions
    """
    account = BankAccount()

    token = True

    while token:
        print("welcome to Keybank \nWhich account service can we help you with?")
        print("Deposit, Withdraw, Check Balance")
        account.getTransaction()
        
        choice = input()

        if choice == "Deposit" or "deposit":
            print("How much money would you like to deposit into your bank account?")
            depositAmt = float(input())
            
            account.Deposit(depositAmt)

            print("Would you like to do another transaction? Please type yes.")
            choice = input()
            
        elif choice == "Withdraw" or "withdraw":
            print("How much money would you like to withdraw from your bank account?")
            withdrawAmt = float(input())
            
            account.Withdraw(withdrawAmt)


            print("Would you like to do another transaction? Please type yes.")
            choice = input()
            
        elif choice == "Check Balance" or "check balance":
            account.getBalance()

            print("Would you like to do another transaction? Please type yes.")
            choice = input()

        elif choice == "no" or "No":
            token = False

            print("Transaction has ended")
            
        else:
            print("Error; Please enter Deposit, Withdraw, or Check Balance")

            print("Would you like to do another transaction? Please type the transaction you want to make.")
            choice = input()

main()
