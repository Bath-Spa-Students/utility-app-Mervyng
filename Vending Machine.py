print("""  
▀█─█▀ █▀▀ █▀▀▄ █▀▀▄ ─▀─ █▀▀▄ █▀▀▀ 　 █▀▄▀█ █▀▀█ █▀▀ █──█ ─▀─ █▀▀▄ █▀▀ 
─█▄█─ █▀▀ █──█ █──█ ▀█▀ █──█ █─▀█ 　 █─▀─█ █▄▄█ █── █▀▀█ ▀█▀ █──█ █▀▀ 
──▀── ▀▀▀ ▀──▀ ▀▀▀─ ▀▀▀ ▀──▀ ▀▀▀▀ 　 ▀───▀ ▀──▀ ▀▀▀ ▀──▀ ▀▀▀ ▀──▀ ▀▀▀       """)

# Dictionary containing items and their prices
items = {"Drinks":{'cola': 1.50,'item_code' :00 ,'pepsi': 1.80,'item_code':11, 'Dr.Pepper':2.35,'item_code':22,'beer':5.40,'item_code':33},
         "Snacks":{'chips': 1.00,'item_code':44,'candy': 0.75,'item_code':55, 'Kitkat': 0.89,'item_code':66,'small cake':3.12,'item_code':77},
         "Burgers":{'Double Smash Cheese Burger':10.20,'item_code':88, 'Cheese Burger':9.50,'item_code':99, 'Mac Donald Burger':13.45,'item_code':100}
         }





## to access the price for individual items do: items[category of drinks][name of drinks]
print(items['Drinks']['cola'])
## to access all the items in drinks do:
print(items['Drinks'].keys())





# Function to display items available in the vending machine
def display_items():
    print("Available items:")
    for item, price in items.items():
        print(f"{item.capitalize()}: ${price}")

# Function to process user's selection and payment
def vending_machine():
    display_items()
    selection = input("Enter the item you want to purchase: ").lower()

    if selection in items:
        item_price = items[selection]
        print(f"The price of {selection.capitalize()} is ${item_price}")

        # Taking payment from the user
        amount = float(input("Please enter the amount to pay: $"))

        if amount >= item_price:
            change = amount - item_price
            print(f"Here is your {selection}! Your change is ${change:.2f}")

            remaining_money = change

            # Suggesting other items within the remaining balance
            suggestions = [item for item, price in items.items() if price <= remaining_money and item != selection]
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
