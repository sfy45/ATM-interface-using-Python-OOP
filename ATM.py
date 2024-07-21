class ATM:
    def __init__(self, card_number, password):
        self.card_number = card_number
        self.password = password
        self.balance = 10000

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"${amount} deposited successfully. New balance: ${self.balance}")
        else:
            print("Invalid amount. Please enter a positive number.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"${amount} withdrawn successfully. New balance: ${self.balance}")
            else:
                print("Insufficient balance.")
        else:
            print("Invalid amount. Please enter a positive number.")

    def check_balance(self):
        print(f"Current balance: ${self.balance}")

    def change_password(self, old_password, new_password):
        if self.password == old_password:
            if len(new_password) == 4 and new_password.isdigit():
                self.password = new_password
                print("Password changed successfully.")
            else:
                print("New password must be a 4-digit number.")
        else:
            print("Incorrect old password.")

def validate_input(prompt, validation_func):
    while True:
        user_input = input(prompt)
        if validation_func(user_input):
            return user_input
        else:
            print("Invalid input. Please try again.")

def validate_card_number(card_number):
    return len(card_number) == 4 and card_number.isdigit()

def validate_password(password):
    return len(password) == 4 and password.isdigit()

def authenticate(card_number, password):
    correct_card_number = "7548"
    correct_password = "9032"
    return card_number == correct_card_number and password == correct_password

def main():
    card_number = validate_input("Enter the last 4 digits of your card number: ", validate_card_number)
    password = validate_input("Enter your 4-digit password: ", validate_password)

    if not authenticate(card_number, password):
        print("Invalid card number or password. Access denied.")
        return

    atm = ATM(card_number, password)

    while True:
        print("\nATM Interface:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Change Password")
        print("5. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            amount = validate_input("Enter amount to deposit: ", lambda x: x.isdigit())
            atm.deposit(int(amount))
        elif choice == '2':
            amount = validate_input("Enter amount to withdraw: ", lambda x: x.isdigit())
            atm.withdraw(int(amount))
        elif choice == '3':
            atm.check_balance()
        elif choice == '4':
            old_password = validate_input("Enter old password: ", validate_password)
            new_password = validate_input("Enter new password: ", validate_password)
            atm.change_password(old_password, new_password)
        elif choice == '5':
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
