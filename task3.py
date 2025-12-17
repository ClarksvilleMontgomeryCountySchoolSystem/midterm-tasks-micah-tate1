# TESTING must = False!!!!!!
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
