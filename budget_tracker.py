#Goals for Budget Tracker
#1. Set budget
#2. Add expenses
#3. View expenses
#4. Check remaining budget
#Create function for each option
#Create main function
#Add remove expense function/option
#Add ability to edit budget

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

def add_expenses(exp_dict, user_budget, total_expenses):
    category = str(input("Enter category of expense (e.g. food, rent...): "))
    while True:
        try:
            amount = float(input("Enter expense amount: £"))
            break
        except ValueError:
            print("Invalid input. Please try again.")
    user_budget -= amount
    total_expenses += amount
    if exp_dict is None:
        exp_dict = {}
    if category in exp_dict:
        exp_dict[category] += amount
    else:
        exp_dict[category] = amount
    print(f"Added £{amount:.2f} to {category} expenses")
    return exp_dict, user_budget, total_expenses

def view_expenses(exp_dict, user_budget):
    if exp_dict is None:
        print("You have no expenses!")
    else:
        print("Summary of expenses below:")
        for category, amount in exp_dict.items():
            print(f"{category} expenses: £{amount:.2f}")
        print(f"\nTotal expenses: £{(sum(exp_dict.values())):.2f}")
        print(f"Remaining budget: £{user_budget:.2f}")
        return exp_dict

def remove_expenses(exp_dict, user_budget, total_expenses):
    return_to_menu_flag = False
    while True:
        if exp_dict is None:
            print("You have no expenses!")
        else:
            try:
                removed_expense_category = str(input("Please enter the expense category that you would like to remove: "))
                removed_expense_amount = exp_dict.pop(removed_expense_category)
                user_budget += removed_expense_amount
                total_expenses -= removed_expense_amount
                print(f"{removed_expense_category} expense removed!")
                break
            except KeyError:
                while True:
                    try:
                        return_to_menu = int(input("You didn't enter a valid expense category. Enter '1' to try again, or enter '2' to return to the menu. "))
                        if return_to_menu == 1:
                            return_to_menu_flag = False
                            break
                        elif return_to_menu == 2:
                            return_to_menu_flag = True
                            break
                    except ValueError:
                        print("Please enter '1' or '2'.")
                if return_to_menu_flag == True:
                    break
                else:
                    continue
    return exp_dict, user_budget, total_expenses

def check_remaining_budget(user_budget):
    print(f"Remaining budget: £{user_budget:.2f}")
    if user_budget < 0:
        print("You have exceeded your budget!")
    return user_budget

def edit_budget(user_budget):
    while True:
        try:
            print(f"Your current budget is £{user_budget:.2f}")
            user_budget = float(input("Please enter your new budget: £"))
            print(f"Your new budget is £{user_budget:.2f}")
            return user_budget
        except ValueError:
            print("Invalid input. Please try again.")

def main():
    print("Welcome to your personal budget tracker!")
    user_budget = set_budget()
    expenses = {}
    total_expenses = 0
    while True:
        print("\nOptions:")
        print("\n1. Add expenses")
        print("2. View expenses")
        print("3. Remove expenses")
        print("4. Change budget")
        print("5. Check remaining budget")
        print("6. Exit")
        while True:
            try:
                user_choice = int(input("\nPlease choose an option: "))
                break
            except:
                print("Please select a number.")
        if user_choice == 1:
            expenses, user_budget, total_expenses = add_expenses(expenses, user_budget, total_expenses)
            total_expenses = sum(expenses.values())
        elif user_choice == 2:
            expenses = view_expenses(expenses, user_budget)
        elif user_choice == 3:
            expenses, user_budget, total_expenses = remove_expenses(expenses, user_budget, total_expenses)
        elif user_choice == 4:
            user_budget = edit_budget(user_budget)
        elif user_choice == 5:
            check_remaining_budget(user_budget)
        elif user_choice == 6:
            break
        else:
            print("Please select a number from the list.")

if __name__ == "__main__":
    main()