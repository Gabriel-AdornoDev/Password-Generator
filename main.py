import secrets
import string

caraters = string.ascii_letters + string.digits + string.punctuation

def evaluate_password():
    password = input("Password to evaluate: ")
    have_uppercase = any(c in string.ascii_uppercase for c in password)
    have_lowercase = any(c in string.ascii_lowercase for c in password)
    have_digits = any(c in string.digits for c in password)
    have_punctuation = any(c in string.punctuation for c in password)
    password_strenght = sum([have_uppercase, have_lowercase, have_digits, have_punctuation])
    if password_strenght <= 1:
        print("Weak password")
    elif password_strenght == 2:
        print("\nMedium password")
    else:
        print("Strong")

def create_password():
    password_lenght = int(input("Password Lenght: "))
    password = "".join(secrets.choice(caraters) for _ in range(password_lenght))
    print(f"Your password is: {password}")

while True:
    print("\n === Password Generator ===")
    print("1 = Evaluate a password")
    print("2 = Create password")
    print("3 = Exit")
    select = int(input("What option you want to do: "))
    if select == 1:
        evaluate_password()
    elif select == 2:
        create_password()
    elif select == 3:
        break
    else:
        print("Select a valid option")

    
    