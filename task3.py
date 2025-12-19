# TESTING must = False!!!!!!
TESTING = False  # <-- Should be False by default
item = None
price = None
quantity = None

print("""
========================================
   WELCOME TO THE PECULIAR EMPORIUM!
   "Magical items at mundane prices!"
   Prosperity comes in threes!
========================================
ITEM MENU:
Invisibility Cloak.........$44.99
Dragon Egg.....................$29.99
""")

menu =('''
Flying Carpet...............$119.99
Phoenix Feather.............$14.99
Time Turner.................$84.99
Enchanted Sword.............$65.99
Potion of Luck..............$11.99
Crystal Ball................$39.99
''')
print(menu)

# Shopkeeper's rule: All purchases must be at least 3 items for good luck!
# (Don't worry - the shopkeeper checks every order himself)

def get_purchase_info(): # Convert input when necessary
    item =str(input("What item do you want?\n"))
    price = int(input("What is the price?\n"))
    quantity = int(input("How many do you want?\n"))
    return item, price, quantity
# Only get input if NOT testing
if not TESTING:
    item, price, quantity = get_purchase_info()

# Calculate using the input values (NOT hardcoded!)
subtotal = price*quantity
tax_rate = 0.095 #This is slightly different from the review. The tax multiplier is stored into a variable.
tax = tax_rate*subtotal
total = subtotal + tax
rounded_total = round(total, 2)

# Print statements
print("--------------------------")
print(f" {item}")
print("--------------------------")
print(f"Subtotal: ${subtotal}")
print(f" Tax: ${tax}")print(f" Total: ${total}")
print("\nThank you for shopping at\nThe Peculiar Emporium!")
