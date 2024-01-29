print("""  
▀█─█▀ █▀▀ █▀▀▄ █▀▀▄ ─▀─ █▀▀▄ █▀▀▀ 　 █▀▄▀█ █▀▀█ █▀▀ █──█ ─▀─ █▀▀▄ █▀▀ 
─█▄█─ █▀▀ █──█ █──█ ▀█▀ █──█ █─▀█ 　 █─▀─█ █▄▄█ █── █▀▀█ ▀█▀ █──█ █▀▀ 
──▀── ▀▀▀ ▀──▀ ▀▀▀─ ▀▀▀ ▀──▀ ▀▀▀▀ 　 ▀───▀ ▀──▀ ▀▀▀ ▀──▀ ▀▀▀ ▀──▀ ▀▀▀       
""")

# Dictionary containing items and their prices
items = {
    "Drinks": {'cola': 1.50, 'pepsi': 1.80, 'Dr.Pepper': 2.35, 'beer': 5.40},
    "Snacks": {'chips': 1.00, 'candy': 0.75, 'Kitkat': 0.89, 'small cake': 3.12},
    "Burgers": {'Double Smash Cheese Burger': 10.20, 'Cheese Burger': 9.50, 'Mac Donald Burger': 13.45}
}

# Function to display items available in the vending machine
def display_items():
    print("Available items:")
    for category, products in items.items():
        print(f"{category.capitalize()}: {', '.join(products.keys())}")

# Function to process user's selection and payment
def vending_machine():
    display_items()
    selection = input("Enter the item you want to purchase: ").lower()

    if selection in [item.lower() for sublist in items.values() for item in sublist.keys()]:
        item_price = [price for sublist in items.values() for item, price in sublist.items() if item.lower() == selection][0]
        print(f"The price of {selection.capitalize()} is ${item_price:.2f}")

        # Taking payment from the user
        amount = float(input("Please enter the amount to pay: $"))

        if amount >= item_price:
            change = amount - item_price
            print(f"Here is your {selection}! Your change is ${change:.2f}")

            remaining_money = change

            # Suggesting other items within the remaining balance
            suggestions = [item for category, products in items.items() for item, price in products.items()
                            if price <= remaining_money and item.lower() != selection]
            if suggestions:
                print("You might also consider:")
                for suggested_item in suggestions:
                    print(f"{suggested_item.capitalize()}")

            print(f"Remaining money: ${remaining_money:.2f}")
        else:
            print("Sorry, the amount is not enough. Transaction canceled.")
    else:
        print("Sorry, that item is not available.")

# Run the vending machine
vending_machine()
