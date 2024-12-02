#Goals for Budget Tracker
#1. Set budget
#2. Add expenses
#3. View expenses
#4. Check remaining budget
#Create function for each option
#Create main function

def set_budget():
    while True:
        try:
            user_budget = float(input("Enter your monthly budget: £"))
            if user_budget <= 0:
                print("Please enter a positive value.")
            else:
                return user_budget
        except ValueError:
            print("Invalid input. Please try again.")

def add_expenses(exp_dict):
    category = str(input("Enter category of expense (e.g. food, rent...): "))
    while True:
        try:
            amount = float(input("Enter expense amount: £"))
            break
        except ValueError:
            print("Invalid input. Please try again.")
    if category in exp_dict:
        exp_dict[category] += amount
    else:
        exp_dict[category] = amount
    print(f"Added £{amount:.2f} to {category} expenses")
    return exp_dict

def view_expenses(exp_dict):
    print("Summary of expenses below:")
    for category, amount in exp_dict.items():
        print(f"{category} expenses: £{amount:.2f}")
    total_expenses = sum(exp_dict.values())
    print(f"\nTotal expenses: £{total_expenses:.2f}")
    return total_expenses

def check_remaining_budget(user_budget, total_expenses):
    remaining_user_budget = user_budget - total_expenses
    print(f"Remaining budget: £{remaining_user_budget:.2f}")
    if remaining_user_budget < 0:
        print("You have exceeded your budget!")
    return remaining_user_budget

def main():
    print("Welcome to your personal budget tracker!")
    user_budget = set_budget()
    expenses = {}
    total_expenses = 0
    while True:
        print("\nOptions:")
        print("\n1. Add expenses")
        print("2. View expenses")
        print("3. Check remaining budget")
        print("4. Exit")
        while True:
            try:
                user_choice = int(input("\nPlease choose an option: "))
                break
            except:
                print("Please select a number.")
        if user_choice == 1:
            expenses = add_expenses(expenses)
            total_expenses = sum(expenses.values())
        elif user_choice == 2:
            total_expenses = view_expenses(expenses)
            check_remaining_budget(user_budget, total_expenses)
        elif user_choice == 3:
            check_remaining_budget(user_budget, total_expenses)
        elif user_choice == 4:
            break
        else:
            print("Please select a number from the list.")

if __name__ == "__main__":
    main()