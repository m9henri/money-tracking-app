from MainTracker import transaction
import os

def start():
    
    print(
    """Welcome to the money tracker!
    Select one of these three options:

    - Add a new entry (A)
    - Close the program (E)\n""")
    entry_Q = input("Choose your operation: ")
    if entry_Q == "A":
        transaction()
    if entry_Q == "E":
        os.abort()