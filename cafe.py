# TASK 12 - MARIA LAWRENCE 

# List of menu
menu_list = ['taramasalata', 'aubergine dip', 'pitta', 'falafel', 'kofta']

# Dictorionary of stock
stock = {'taramasalata': 4,
              'aubergine dip': 16,
              'pitta': 16, 
              'falafel': 6,
              'kofta': 2
              }

# Dictionary of price
price = {'taramasalata': 2.20,
              'aubergine dip': 3.10,
              'pitta': 0.50, 
              'falafel': 5.0,
              'kofta': 7.60
              }

total_stock_worth = 0
for items in menu_list:
    item_value = stock[items] * price[items]
    total_stock_worth += item_value

print(f"The total stock worth in the cafe is £{total_stock_worth:.2f}.")


# NB if we wanted to do it for each individual item:

# List of menu

stock_value_individual = {item:stock[item] * price[item] for item in menu_list}

for item in stock_value_individual:
    print(f"You have £{stock_value_individual[item]:.2f} worth of {item.capitalize()}.")