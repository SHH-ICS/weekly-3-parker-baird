print("Would you like a large pizza for $6 or an extralarge pizza for $10?")
size = input("Enter 'large' or 'extralarge': ")
if size == 'large':
    print("You ordered a large, that's $6.")
    size_cost = 6
elif size == 'extralarge':
    print("You ordered an extralarge, that's $10.")
    size_cost = 10
else:
    print("Invalid size selected. Please run the program again.")
    exit()
print("How many toppings would you like? (1-4)")
toppings = input() 
if toppings.isdigit():
    toppings = int(toppings) 
else:
    print("Invalid input for toppings. Please enter a number.")
    exit()
if toppings == 1:
    topcost = 1.00
elif toppings == 2:
    topcost = 1.75
elif toppings == 3:
    topcost = 2.50
elif toppings == 4:
    topcost = 3.35
else:
    print("Invalid number of toppings. Please enter a number between 1 and 4.")
    exit()
subtotal = size_cost + topcost
tax = subtotal * 0.13
total = tax + subtotal
print(f"The total for your pizza will be: ${total:.2f}")