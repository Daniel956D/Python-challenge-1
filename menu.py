# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered
order = []
order_number = datetime.now().strftime("%Y%m%d%H%M")  # Added unique order tracking

# Launch the store and present a greeting to the customer
print("=" * 50)
current_hour = datetime.now().hour
if 6 <= current_hour < 12:
    print("☀️  Good Morning! Welcome to the Variety Food Truck")
elif 12 <= current_hour < 17:
    print("🌞  Good Afternoon! Welcome to the Variety Food Truck")
else:
    print("🌙  Good Evening! Welcome to the Variety Food Truck")
print("=" * 50)

# Customers may want to order multiple items, so let's create a continuous loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("\nFrom which menu would you like to order?")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings
    for key in menu.keys():
        print(f"{i}: {key} 📋")  # Added emoji for visual appeal
        menu_items[i] = key
        i += 1

    # Get the customer's input
    menu_category = input("\nType menu number (or 'q' to finish ordering): ")  # Added quit option

    # Check if customer wants to quit
    if menu_category.lower() == 'q':
        if order:  # Only allow quit if there are items in order
            break
        print("Please select at least one item before finishing.")
        continue

    # Check if the customer's input is a number
    if menu_category.isdigit():
        if int(menu_category) in menu_items.keys():
            menu_category_name = menu_items[int(menu_category)]
            print(f"\nYou selected {menu_category_name}")

            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("\n" + "=" * 50)
            print(f"📋  {menu_category_name} Menu".center(50))  # Enhanced header
            print("=" * 50)
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")

            for key, value in menu[menu_category_name].items():
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1

            # 2. Ask customer to input menu item number
            menu_selection = input("\nPlease enter the number of your selection: ")

            # 3. Check if the customer typed a number
            if menu_selection.isdigit():
                # Convert the menu selection to an integer
                menu_selection = int(menu_selection)

                # 4. Check if the menu selection is in the menu items
                if menu_selection in menu_items:
                    # Store the item name as a variable
                    selected_item = menu_items[menu_selection]

                    # Ask the customer for the quantity of the menu item
                    quantity_input = input(f"How many {selected_item['Item name']}(s) would you like? ")

                    # Check if the quantity is a number, default to 1 if not
                    if quantity_input.isdigit():
                        quantity = int(quantity_input)
                        # Added preview of item total
                        item_total = quantity * selected_item['Price']
                        print(f"Added: {quantity} x {selected_item['Item name']} = ${item_total:.2f}")
                    else:
                        quantity = 1
                        print("Invalid quantity. Setting quantity to 1.")

                    # Add the item name, price, and quantity to the order list
                    order.append({
                        "Item name": selected_item["Item name"],
                        "Price": selected_item["Price"],
                        "Quantity": quantity
                    })
                else:
                    print("Invalid menu selection. Please try again.")
        else:
            print(f"Sorry, {menu_category} is not a valid menu option.")
    else:
        print("Please enter a valid number.")

    while True:
        # Ask the customer if they would like to order anything else
        keep_ordering = input("\nWould you like to order anything else? (Y)es or (N)o: ").lower()

        # 5. Check the customer's input
        if keep_ordering == 'y':
            break
        elif keep_ordering == 'n':
            place_order = False
            print("\nThank you for your order!")
            break
        else:
            print("Please enter 'Y' or 'N'")

# Print out the customer's order
print("\nThis is what we are preparing for you.\n")
print(f"Order #: {order_number}".center(50))  # Added order number
print(datetime.now().strftime("%Y-%m-%d %H:%M").center(50))  # Added timestamp
print("\nItem name                 | Price  | Quantity")
print("--------------------------|--------|----------")

# 6. Loop through the items in the customer's order
subtotal = 0  # Added subtotal tracking
for item in order:
    # 7. Store the dictionary items as variables
    item_name = item["Item name"]
    price = item["Price"]
    quantity = item["Quantity"]

    # 8. Calculate the number of spaces for formatted printing
    name_spaces = " " * (25 - len(item_name))

    # 9. Create space strings
    price_str = f"${price:.2f}"
    price_spaces = " " * (6 - len(price_str))

    # 10. Print the item name, price, and quantity
    print(f"{item_name}{name_spaces} | {price_str} | {quantity}")
    subtotal += price * quantity  # Calculate running subtotal

# 11. Calculate the cost of the order using list comprehension
total = sum(item["Price"] * item["Quantity"] for item in order)
tax = total * 0.08  # Added tax calculation
final_total = total + tax  # Added final total with tax

print("=" * 50)
print(f"Subtotal: ${total:>39.2f}")  # Added subtotal display
print(f"Tax (8%): ${tax:>39.2f}")    # Added tax display
print(f"Total:    ${final_total:>39.2f}")  # Added final total display
print("=" * 50)

# Added tip suggestions
print("\nSuggested Tips:")
for tip_percent in [15, 18, 20]:
    tip_amount = final_total * (tip_percent / 100)
    print(f"{tip_percent}%: ${tip_amount:.2f}")