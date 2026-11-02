# Self-Assessment
# 1. With AI help, the first bug identified was the missing colon in
#    "for sale in sales". It causes a SyntaxError, so nothing runs yet.
#    The other bugs show why I need to check the results too: a program
#    can run and still give the wrong total. I need more practice tracing
#    the values myself instead of relying on AI to find the problem.
# 2. apply_discount takes a price and a tier. Gold gets 15% off, silver
#    gets 10% off, and bronze gets 5% off. Other tiers get no discount.
#    It returns the discounted price. A colleague could use it with
#    this explanation without reading the code inside the function.
# 3. AI disclosure: I used ChatGPT to help write the code and explain the
#    three bugs. The explanations show why adding to
#    a total is different from replacing it and why the last index is 4,
#    not 5. Using AI also skipped some of the solo debugging practice.
#    I still need to trace the code myself to check my understanding.

# Exercise 1
def calculate_tax(price, rate):
    return price * rate


print(f"Tax on $100 at 7%: ${calculate_tax(100, 0.07):.2f}")
print(f"Tax on $250 at 8%: ${calculate_tax(250, 0.08):.2f}")

# Exercise 2
def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price


print(f"gold:   ${apply_discount(200, 'gold'):.2f}")
print(f"silver: ${apply_discount(200, 'silver'):.2f}")
print(f"bronze: ${apply_discount(200, 'bronze'):.2f}")
print(f"none:   ${apply_discount(200, 'none'):.2f}")

# Exercise 3
discounted_price = apply_discount(200, "gold")
price_with_tax = discounted_price + calculate_tax(discounted_price, 0.07)
print(f"After gold discount: ${discounted_price:.2f}")
print(f"After tax: ${price_with_tax:.2f}")


def final_price(price, tier, tax_rate):
    discounted_price = apply_discount(price, tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax


print(f'final_price(200, "gold", 0.07) = ${final_price(200, "gold", 0.07):.2f}')

# Exercise 4
orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]
for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")

# Exercise 5
# Fixed version of the instructor's broken_sales.py.
# Bug notes:
# 1. "for sale in sales" needs a colon. Without it, Python gives a
#    SyntaxError before any of the code runs.
# 2. "total = sale" replaces the total each time. After fixing the colon,
#    this would print $90, the last sale, instead of the correct total $715.
# 3. "i <= len(sales)" lets i reach 5. This list has five items, but its
#    indexes are 0 through 4. Trying sales[5] causes an IndexError.
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    # Fix: Use += so each sale is added to the total already saved.
    total += sale
    # To trace the total, temporarily use: print(sale, total)
print(f"Total: ${total}")

count = 0
# Fix: Add a colon so Python knows the loop body starts next.
for sale in sales:
    count += 1
print(f"Count: {count}")

i = 0
# Fix: Use < so the loop stops at i = 5 without trying to read sales[5].
while i < len(sales):
    print(sales[i])
    i += 1

# Exercise 6
# Prediction: This prints 100, then 1998, then 100.
x = 100


def double_it():
    x = 999
    return x * 2


print(x)
print(double_it())
print(x)
# The output is 100, 1998, and 100. Scope means where a variable is used.
# The x inside the function is separate from the x outside it.
# The function returns 999 * 2, but the outside x stays 100.
