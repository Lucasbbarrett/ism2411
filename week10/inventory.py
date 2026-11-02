# Reflection
# 1. The most surprising part of Python lists is that one list can change
#    size and order while the program runs. I expected to need a new list
#    each time, but append(), remove(), and sort() modify the existing list.
# 2. In a business class sales analysis, a list could store daily sales and
#    calculate the total, average, best day, and worst day automatically.
#    Compared with manually selecting Excel ranges and copying formulas,
#    the same Python steps could be reused when new sales data arrives.
# AI assistance: ChatGPT helped draft the code and reflection comments.

# Exercise 1: Build the list.
inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print("Exercise 1")
print(inventory)
print(len(inventory))

# Exercise 2: Use positive and negative indices; compute the middle.
print("\nExercise 2")
print(inventory[0])
print(inventory[-1])
print(inventory[len(inventory) // 2])

# Exercise 3: Slice the original inventory.
print("\nExercise 3")
print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])

# Exercise 4: Print the list after each modification.
print("\nExercise 4")
inventory.append("envelope")
print(inventory)
inventory.remove("tape")
print(inventory)
inventory.sort()
print(inventory)

# Exercise 5: Tuples cannot be changed in place.
print("\nExercise 5")
coords = (40.7128, -74.0060)
try:
    coords[0] = 99
except TypeError:
    print("TypeError caught: tuples are immutable. They are useful for")
    print("coordinates because their values cannot be changed accidentally.")
print(coords)

# Exercise 6: Summarize daily sales.
print("\nExercise 6")
sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count
print("Total:", total)
print("Count:", count)
print("Average:", average)
print("Best:", max(sales))
print("Worst:", min(sales))

# Exercise 7: Accumulate discounted prices using append().
print("\nExercise 7")
prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []
for price in prices:
    discounted.append(round(price * 0.90, 2))
print("Original:", prices)
print("Discounted:", discounted)

# Exercise 8: Include only sales strictly greater than 300.
print("\nExercise 8")
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []
for sale in sales:
    if sale > 300:
        high_sales.append(sale)
print(high_sales)
print("Count:", len(high_sales))
print(f"Average: {sum(high_sales) / len(high_sales):.2f}")
