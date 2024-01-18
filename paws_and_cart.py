"""A shopping cart application for pet products. Program allows 
   users to add / remove items to their basket as they shop."""
import time
import os

# To clear screen.
def clear_screen(time_delay):
    """Function to clear terminal."""
    time.sleep(time_delay)
    os.system("clear||cls")

# Print storefront.
def print_store():
    """Function prints store header in neat table."""
    # Variables to edit table.
    left_width = 20
    right_width = 20
    # Print title and store.
    print("")
    print("=" * (20 + 20))
    print(" Paws and Cart ".upper().center(left_width + right_width, '+'))
    print("Item ID ".ljust(left_width, '=') + " Price".rjust(right_width, '='))
    for key, value in pet_items.items():
        print(f"{key}: {value[0]} ".title().ljust(left_width, '.') + f" £{value[1]:.2f}".rjust(right_width, '.'))
    # Print menu options.
    print("=" * (left_width + right_width))
    print("MENU".center(left_width + right_width, ' '))
    print("-" * (left_width + right_width))
    print("1. Enter Item ID to add to basket.")
    print("2. Enter '1' to edit shopping basket.")
    print("3. Enter '0' to checkout or quit. ")
    print("=" * (left_width + right_width))
    # Print basket contents.
    total_sum = 0
    if basket:
        print("SHOPPING CART".center(left_width + right_width, ' '))
        print("-" * (left_width + right_width))
        for key, value in basket.items():
            total_sum += value[1]
            print(f"{pet_items[key][0].upper()} x {value[0]} = £{value[1]}".center(left_width + right_width, ' '))
        print("=" * (left_width + right_width))
        print(f"TOTAL: £{total_sum:.2f}".center(40))

# Main function for shopping.
def browse_store():
    """This is the main function used for the application."""
    shopping = True
    while shopping:
        # Print store function.
        print_store()

        # Get user input.
        product_id = input("Enter ID: ").strip()

        # Main menu.
        if product_id == '0':   # Quit.
            clear_screen(0.5)
            print("\nThank you for shopping at Paws and Cart!\n")
            shopping = False
        elif product_id == '1':  # Edit / view basket.
            clear_screen(0.2)
            edit_basket()
        # Add items to basket.
        elif product_id in pet_items:
            clear_screen(0.2)
            # Display information on product and statement to proceed.
            print(item_info[product_id])
            print("-" * (40))
            buy = input("Type any key return.\nEnter 'y' to purchase: ").strip()
            if buy == 'y':
                pass
            else:
                print("Returning to main menu.")
                clear_screen(2)
                continue
            # Match pet items key to entered product ID.
            for key, value in pet_items.items():
                if product_id == key and product_id not in basket:
                    # Add item to basket.
                    basket[product_id] = [1, value[1]]
                    print(f"Adding 1 x {value[0].upper()} to Basket.")
                    clear_screen(1.5)
                # If already purchased, modify values in basket.
                elif product_id == key and product_id in basket:
                    # New item quantity and total cost per.
                    new_quantity = basket[product_id][0] + 1
                    new_sum = basket[product_id][1] + value[1]
                    basket[product_id] = [new_quantity, new_sum]
                    # Print item to user interface.
                    print(f"Adding 1 x {value[0].upper()} to Basket.")
        else:
            print(f"Error: '{product_id}' is not a valid item ID.")
            clear_screen(1.5)

def edit_basket():
    """This function allows user to edit the basket."""
    view_basket = True
    while view_basket:
        # Print basket contents.
        print("=" * (40))
        print("SHOPPING CART".center(40, ' '))
        print("-" * (40))
        total = 0
        for key, value in basket.items():
            total += value[1]
            print(f"{key}: {pet_items[key][0].upper()} x {value[0]} = £{value[1]}".center(40, ' '))
        print("=" * (40))
        print(f"Total Sum: £{total}")
        print("=" * (40))
        print("1. Enter ID to change item quantity.")
        print("2. Enter ID and '0' to remove item.")
        print("3. Enter '1' to go back to menu.")
        print("-" * (40))
        # Edit basket contents.
        product_id = input("Enter ID: ")
        if product_id == '1':
            clear_screen(0)
            view_basket = False
        elif product_id in basket:
            print("-" * (40))
            print(f"Item Selected: {pet_items[product_id][0].upper()}\nQuantity: {basket[product_id][0]}")
            try:
                new_unit_amount = input("Enter New Amount: ").strip()
                # Delete item if 0.
                if new_unit_amount == 'back':
                    clear_screen(0)
                    continue
                elif new_unit_amount == '0':
                    print("Item removed from basket.")
                    del basket[product_id]
                    clear_screen(1.5)
                # Update values in basket.
                else:
                    new_sum = int(new_unit_amount) * int(pet_items[product_id][1])
                    basket[product_id] = [new_unit_amount, new_sum]
                    clear_screen(1.5)
            except ValueError as error:
                print(f"Error: enter number for new quantity.\n{error}")
                clear_screen(1.5)
        else:
            print(f"Error: '{product_id}' this is not in basket.")
            clear_screen(1.5)

# Dictionary of items for store.
pet_items = {
            "130": ["dog food", 5.00],
            "394": ["cat food", 5.00],
            "203": ["chew toy", 5.00],
            "101": ["cuddly bear", 10.00],
}

item_info = {
            "130": "Info about dog food.",
            "394": "Info about cat food.",
            "203": "Info about chew toy.",
            "101": "Info on cuddly bear."
}

# Run program.
basket = {}
clear_screen(0)
browse_store()
