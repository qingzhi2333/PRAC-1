sales = float(input("Enter sales: $"))
if sales<1000:
    bonus=sales*0.18
    print("sales :",sales)
    print("bonus :",bonus)
else:
    bonus=sales*0.15
    print("sales :", sales)
    print("bonus :",bonus)
