import os
import time
import main

def start():
    os.system("cls")

    transaction_type = input("Have you got or spent money? (+ or -): ")

    date = input("Choose a date when the transaction happend (DD.MM.YYYY): ")

    reason = input("Choose a reason on why you made the transaction (All in one line): ")

    heavyness = input("How much did you spend/got? (no money symbol): ")

    print(f"Are these statements correct? (Y/n) {transaction_type}, {date}, {reason}, {heavyness}")
    
    final_answer = input()
    if final_answer == "Y":
        print("\nCongrats, you've made a change!")
        time.sleep(5)
        main()
    if final_answer == "n":
        print("Ok we'll reset it for you in 5 seconds.")
        time.sleep(5)
        start()
    return