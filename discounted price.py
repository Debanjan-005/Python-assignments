p=int(input("Enter your total price:"))
if p>=20000 and p<30000:
    print("Discounted price=",0.95*p)
elif p>=30000 and p<50000:
    print("Discounted price=",0.90*p)
else:
    print("Discounted price=",0.85*p)

