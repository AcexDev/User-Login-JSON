import json
import time
import sys

def initiate():
    print(f"""
{"=" * 30}
WELCOME TO ACEX LOGIN SYSTEM!
{"=" * 30}\n
Choose an Option:
1 - Login
2 - Sign Up
* Any other key to exit
{"-"*30}
    """)

with open("../General Tut/users.json", "r") as f:
    user_details = json.load(f)



def credentials_validate():
    print("== LOGIN ==")
    username = input("Enter username: ")
    passcode = input("Enter passcode: ")

    for persons in user_details['users']:
        if username == persons['username'] and passcode == persons['passcode']:
            print(f"\nAccess Granted ✅")
            time.sleep(0.5)
            print(f"Welcome back {persons['username']}!")
            return
    print("No matching credentials found")


def registration():
    print("== SIGN UP ==")
    new_user = {}
    username = input("Enter username: ")
    for persons in user_details['users']:
        if username == persons['username']:
            print("Name already taken")
            return
        else:
            new_user['username'] = username
    while True:
        passcode = input("*Set passcode(4-digits): ")
        if not passcode.isdigit() or len(passcode) != 4:
            print("Invalid! Passcode should be 4 digits")
        else:
            new_user['passcode'] = passcode
            print("Processing..")
            time.sleep(1.5)
            user_details['users'].append(new_user)
            with open("../General Tut/users.json", "w") as db:
                json.dump(user_details, db, indent=2)
            print("\n✅New User Successfully Created!")
            print(f"Redirecting to Login\n{'-'*30}\n")
            time.sleep(1.5)
            credentials_validate()
            break





def main():
    while True:
        initiate()
        choice = input("> ")
        if choice == "1":
            credentials_validate()
        elif choice == "2":
            registration()
        else:
            sys.exit("Program exited")
        print("Redirecting to Main Menu..")
        time.sleep(1.5)
        print()

main()

