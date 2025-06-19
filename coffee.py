import coffee_report

# Show the menu
def menu():
    print("MENU")
    print("item_name : cost")
    print("1. espresso = $1.5")
    print("2. latte = $2.0")
    print("3. cappuccino = $3.0")

menu()

# Take coin input and return total
def coins_report():
    quarters = int(input("How many quarters: "))
    dimes = int(input("How many dimes: "))
    nickels = int(input("How many nickels: "))
    pennies = int(input("How many pennies: "))
    total = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
    return round(total, 2)

# Get cost of the selected drink
def chosen_choice(choice):
    return coffee_report.MENU[choice]["cost"]

# Reduce ingredients from resources after preparing the drink
def reduce_ingredients(choice):
    ingredients = coffee_report.MENU[choice]["ingredients"]
    
    # Check if enough resources are available
    for item in ingredients:
        if coffee_report.resources.get(item, 0) < ingredients[item]:
            print(f"Sorry, there is not enough {item}.")
            return False

    # Deduct resources
    for item in ingredients:
        coffee_report.resources[item] -= ingredients[item]

    return True

# Calculate change and serve drink
def change(cost, total, choice):
    print(f"Here is ${round(total - cost, 2)} in change.")
    print(f"Here is your {choice} ☕️. Enjoy!")

# Main program loop
def main():
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino) or (off) turn off machine: ").lower()

        if choice == "report":
            for key, value in coffee_report.resources.items():
                print(f"{key}: {value}")
            continue
        elif choice== "off":
            print("Shutting down.Goodbye")
            break

        elif choice not in ["espresso", "latte", "cappuccino"]:
            print("Invalid input. Try again.")
            continue

        cost = chosen_choice(choice)
        print(f"The cost is ${cost}")
        total = coins_report()


        if total < cost:
            print("Sorry, that's not enough money. Money refunded.")
            continue

        success = reduce_ingredients(choice)
        if not success:
            continue

        change(cost, total, choice)

main()
