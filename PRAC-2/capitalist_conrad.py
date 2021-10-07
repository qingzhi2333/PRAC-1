# capitalist_conrad

import random

max_increase = 0.175
max_decrease = 0.05
min_price = 1.0
max_price = 1.0
initial_price = 10.0

day_count = 0
price = initial_price
print("Starting price: ${:,.2f}".format(price))

while min_price <= price <= max_price:
    price_change = 0
    day_count =+ 1

    if random.randint(1,2) == 1:
        price_change = random.uniform(0, max_increase)
    else:
        price_change = random.uniform(max_decrease, 0)

    price *= (1 + price_change)
    print("On day {:<3} price is ${:,.2f}".format(day_count, price))



