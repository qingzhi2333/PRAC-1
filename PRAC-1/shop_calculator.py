s=int(input("Enter items kind:"))
Total=0
for i in range(0, s, 1):
    number = int(input("Enter number:"))
    price = int(input("Enter price:"))
    total = number * price
    Total+=total
if Total >= 100:
    Total = Total * 0.9
    print("You need pay :", Total)
else:
    print("You need pay :", Total)



