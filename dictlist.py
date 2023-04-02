guestlist = {
    "Raisa": ["pizza", "cookies", 3],
    "Susan": ["salad", 2],
    "Jia": ["ice cream", 0],
    "Val": ["cake", 2],
    "Brian": ["pasta", "cheese", "crackers", 2],
    "Chandra": ["burgers", "buns", 3]
}

# Print out each guest and their food items
for name, items in guestlist.items():
    food_items = ", ".join(items[:-1]) + ", and " + items[-2] if len(items) > 2 else items[0]
    print(f"{name} is bringing {food_items}.")

# Calculate the total number of guests
total_guests = sum([items[-1] + 1 for items in guestlist.values()])
print(f"The total number of guests is {total_guests}.")

powleyGuests = ["Isla", "Susan", "Ellen", "Jia", "Raisa", "Chandra", "Wendy"]

def find_missing_guests(guestlist, powleyGuests):
    """
    Returns a list of names that are in powleyGuests but not in guestlist.

    Parameters:
    guestlist (dict): A dictionary containing guest names and their food items and guest counts.
    powleyGuests (list): A list of guest names that Professor Powley would like to invite.

    Returns:
    list: A list of names that are in powleyGuests but not in guestlist.
    """
    return [name for name in powleyGuests if name not in guestlist]

# Find the missing guests
missing_guests = find_missing_guests(guestlist, powleyGuests)
print(f"The missing guests are: {missing_guests}")

# Add missing guests to guestlist with food item "tbd"
for name in missing_guests:
    guestlist[name] = ["tbd", 0]

# Print out each guest and their food items, including the new guests
for name, items in guestlist.items():
    food_items = ", ".join(items[:-1]) + ", and " + items[-2] if len(items) > 2 else items[0]
    print(f"{name} is bringing {food_items}.")

def check_food_item(items):
    """
    Returns True if at least one of the following conditions is met:
    1. the number of guests is greater than 0 and the first food item has more than 3 characters or starts with "p".
    2. the number of guests is equal to 0 and one of the food items contains both the letter "s" and the letter "p".
    
    Parameters:
    items (list): A list containing the food items and the numbers of guests.

    Returns:
    bool: True if at least one of the conditions is met, False otherwise.
    """
    if items[-1] > 0:
        return len(items[0]) > 3 or items[0].startswith("p")
    elif items[-1] == 0:
        for item in items[:-1]:
            if "s" in item and "p" in item:
                return True
        return False
    else:
        return False

# Check each guest's food item and print True or False
for items in guestlist.values():
    print(check_food_item(items))

# Prompt the user to enter additional names to powleyGuests
# num_names = int(input("How many additional names would you like to add to the guest list?: "))
while True:
    try:
        num_names = int(input("How many names do you want to enter? "))
        break
    except ValueError:
        print("Please enter a valid integer.")

names = []
for i in range(num_names):
    while True:
        name = input(f"Enter name {i+1}: ")
        if name in powleyGuests:
            print("This name already exists in the guest list.")
        elif name.isdigit():
            print("Please enter a valid name.")
        else:
            names.append(name)
            break

powleyGuests += names
print("Updated powleyGuests list:", powleyGuests)
