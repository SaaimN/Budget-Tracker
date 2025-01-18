import pickle

# Function shows user their budget (that is saved in the user budget file)
def show_budget():
    with open("user_budget_file.txt", "r") as user_budget_file:
        user_budget = user_budget_file.read()
        print(f"Your budget is currently £{user_budget}")
# END OF FUNCTION ---------------------------------------------------------------------------------------------------------------------------------------------


# Function gives user option to set their budget
# Changes the saved data in the user budget file
def set_budget():
    while True:
        change_budget = str(input("Would you like to change your budget? Please type 'Yes' or 'No'. ")).strip().lower()
        if change_budget == "yes":
            while True:
                try:
                    user_budget = float((input("Enter your monthly budget: £")).strip())
                    with open("user_budget_file.txt", "w") as user_budget_file:
                        user_budget_file.write(f"{user_budget:.2f}")
                    return
                except ValueError:
                    print("Invalid input. Please try again.")
        elif change_budget == "no":
            break
        else:
            print("You didn't enter a valid input. Please try again.")
# END OF FUNCTION ---------------------------------------------------------------------------------------------------------------------------------------------


# Function for user to add an expense
def add_expenses():
    # Ask user for category of expense
    category = str(input("Enter category of expense (e.g. food, rent...): ")).strip().lower()

    # Initialise loop
    while True:
        try:
            amount = float(input("Enter expense amount: £").strip())
            with open("expenses_file.txt", "a") as expenses_file:
                expenses_file.write(f"\n{category}: {amount:.2f}")
            break
        except ValueError:
            print("Invalid input. Please try again.")
    # End of loop

    # Update user budget data in user budget file
    with open("user_budget_file.txt", "r") as user_budget_file:
        user_budget = float(user_budget_file.read())
    with open("user_budget_file.txt", "w") as user_budget_file:
        user_budget_file.write(f"{user_budget - amount:.2f}")

    # Update total expenses amount in total expenses file
    with open("total_expenses_file.txt", "r") as total_expenses_file:
        total_expenses = float(total_expenses_file.read())
    with open("total_expenses_file.txt", "w") as total_expenses_file:
        total_expenses_file.write(f"{total_expenses + amount:.2f}")

    # Update dictionary pkl file
    try:
        with open("expenses_dictionary_file.pkl", "rb") as expenses_dictionary_file:
            expenses = pickle.load(expenses_dictionary_file)
    except EOFError:
        expenses = {category: amount}
        with open("expenses_dictionary_file.pkl", "wb") as expenses_dictionary_file:
            pickle.dump(expenses, expenses_dictionary_file)
    else:
        if category in expenses:
            expenses[category] += amount
        else:
            expenses[category] = amount
        with open("expenses_dictionary_file.pkl", "wb") as expenses_dictionary_file:
            pickle.dump(expenses, expenses_dictionary_file)

    print(f"Added £{amount:.2f} to {category} expenses")
# END OF FUNCTION --------------------------------------------------------------------------------------------------------------------------------------------


# Function for user to view their expenses
def view_expenses():
    try:
        with open("expenses_dictionary_file.pkl", "rb") as expenses_dictionary_file:
            expenses = pickle.load(expenses_dictionary_file)
    except EOFError:
        print("You have no expenses!")
    else:
        print(f"\nSummary of expenses below:")

        # For loop to go through dictionary and print out data
        for category, amount in expenses.items():
            print(f"{category} expenses: £{amount:.2f}")

        # Print out sum of amount values
        print(f"\nTotal expenses: £{(sum(expenses.values())):.2f}")

        # Read and print out user budget from user budget file
        with open("user_budget_file.txt", "r") as user_budget_file:
            user_budget = float(user_budget_file.read())
        print(f"Remaining budget: £{user_budget:.2f}")
# END OF FUNCTION --------------------------------------------------------------------------------------------------------------------------------------------


# Function for user to remove an expense
def remove_expenses():
    # Set flag here to come out of second while True loop
    return_to_menu_flag = False

    # Initialise loop
    while True:
        try:
            removed_expense_category = str(input("Please enter the expense category that you would like to remove: ")).strip().lower()

            # Remove expense data from dictionary pkl file
            with open("expenses_dictionary_file.pkl", "rb") as expenses_dictionary_file:
                expenses = pickle.load(expenses_dictionary_file)
            removed_expense_amount = float(expenses.pop(removed_expense_category))
            with open("expenses_dictionary_file.pkl", "wb") as expenses_dictionary_file:
                pickle.dump(expenses, expenses_dictionary_file)

            # Remove data from expense text file
            expense_text_to_remove = f"{removed_expense_category}: {removed_expense_amount}"
            with open("expenses_file.txt", "r") as expenses_file:
                expenses_contents = expenses_file.read()
            new_expenses_contents = expenses_contents.replace(expense_text_to_remove, '')
            with open("expenses_file.txt", "w") as expenses_file:
                expenses_file.write(new_expenses_contents)
            
            # Update user budget data in user budget file
            with open("user_budget_file.txt", "r") as user_budget_file:
                user_budget = float(user_budget_file.read())
            with open("user_budget_file.txt", "w") as user_budget_file:
                user_budget_file.write(f"{user_budget + removed_expense_amount:.2f}")

            # Update total expenses data in file
            with open("total_expenses_file.txt", "r") as total_expenses_file:
                total_expenses = float(total_expenses_file.read())
            with open("total_expenses_file.txt", "w") as total_expenses_file:
                total_expenses_file.write(f"{total_expenses - removed_expense_amount:.2f}")
            print(f"{removed_expense_category} expense removed!")
            break

        # Reaffirm whether user wants to remove an expense or not
        except KeyError:
            while True:
                try:
                    return_to_menu = int(input("You didn't enter a valid expense category. Enter '1' to try again, or enter '2' to return to the menu. ").strip())
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

        # In case there is no data in the expenses dictionary pkl file
        except EOFError:
            print("Sorry, you have don't have any expenses!")
            break
# END OF FUNCTION --------------------------------------------------------------------------------------------------------------------------------------------

# Function allows user to check their remaining budget
def check_remaining_budget():
    with open("user_budget_file.txt", "r") as user_budget_file:
        user_budget = float(user_budget_file.read())
    print(f"Remaining budget: £{user_budget:.2f}")
    if user_budget < 0:
        print("You have exceeded your budget!")
# END OF FUNCTION --------------------------------------------------------------------------------------------------------------------------------------------


# Function that allows user to manually change their current budget
# Already existing expenses to do not affect this new budget
def change_budget():
    while True:
        try:
            user_budget = float(input("Enter your new budget: £").strip())
            with open("user_budget_file.txt", "w") as user_budget_file:
                user_budget_file.write(f"{user_budget:.2f}")
            return
        except ValueError:
            print("Invalid input. Please try again.")
# END OF FUNCTION --------------------------------------------------------------------------------------------------------------------------------------------

# MAIN FUNCTION
def main():
    print("Welcome to your personal budget tracker!")

    # Determine user budget
    with open("user_budget_file.txt", "r") as user_budget_file:
        user_budget = user_budget_file.read()

    # Show user's budget to user
    user_budget = show_budget()

    # Give user option to set budget
    user_budget = set_budget()

    # Set empty dictionary
    expenses = {}

    # Determine total expenses
    with open("total_expenses_file.txt", "r") as total_expenses_file:
        total_expenses = total_expenses_file.read()

    # Infinite loop for main menu
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
                user_choice = int(input("\nPlease choose an option: ").strip())
                break
            except:
                print("Please select a number.")
        if user_choice == 1:
            add_expenses()
            total_expenses = sum(expenses.values())
        elif user_choice == 2:
            view_expenses()
        elif user_choice == 3:
            remove_expenses()
        elif user_choice == 4:
            change_budget()
        elif user_choice == 5:
            check_remaining_budget()
        elif user_choice == 6:
            break
        else:
            print("Please select a number from the list.")

if __name__ == "__main__":
    main()