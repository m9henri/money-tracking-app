import os
import time

def transaction():
    os.system("cls")

    transaction_type = input("Have you got or spent money? (+ or -): ")

    date = input("Choose a date when the transaction happend (DD.MM.YYYY): ")

    reason = input("Choose a reason on why you made the transaction (All in one line): ")

    value = input("How much did you spend/got? (no money symbol): ")

    print(f"Are these statements correct? (Y/n) {transaction_type}, {date}, {reason}, {value}")
    
    final_answer = input()
    if final_answer == "Y":
        print("\nCongrats, you've made a change!")
        writing(transaction_type, date, reason, value)
        time.sleep(5)
        start()
    if final_answer == "n":
        print("\nOk we'll reset it for you in 5 seconds.")
        time.sleep(5)
        transaction()
    return

def writing(transaction_type, date, reason, value):
    file = open("tracker.log", "a")
    file.write(f"Date: {date}\n")
    file.write(f"Reason: {reason}\n")
    file.write(f"How much spent/got: {transaction_type}{value}\n\n")
    return

def converter():
    os.system("cls")
    print(
    """How do you wanna convert?
    Select one of these two options:

    - Convert dollars to euros (D)
    - Convert euros to dollars (E)\n""")
    entry_Q = input("Choose your operation: ")
    value = int(input("How much of this currency do you wanna convert? "))
    if entry_Q == "D":
        final_value = value * 0.895404
        print(f"Your outcome from ${value} is {final_value}€.")
    if entry_Q == "E":
        final_value = value * 1.116814
        print(f"Your outcome from {value}€ is {final_value}$.")
    back = input("\nDo you wish to continue? (Y,n) ")
    if back == "Y":
        converter()
    if back == "n":
        start()

def start():
    os.system("cls")
    print(
    """Welcome to the money tracker!
    Select one of these three options:

    - Add a new entry (A)
    - Convert currency (C)
    - Close the program (E)\n""")
    entry_Q = input("Choose your operation: ")
    if entry_Q == "A":
        transaction()
    if entry_Q == "C":
        converter()
    if entry_Q == "E":
        os.abort()

start()