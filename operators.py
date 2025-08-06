n=int(input("Type 1 for first program\n2 for second program\n3 for third program\nYour response:"))
if n==1:
    print("Got it! Here' s your first program\n\n")
    s=input("Enter a word or character:")
    c=int(input("Type 1 for id of your word.\nType 2 for type of your word\nYour response:"))
    if c==1:
        print(id(s))
    elif c==2:
        print(type(s))
    else:
        print("Invalid input")

elif n==2:
    print("Got it! Here' s your second program\n\n")
    print("Python", "Java", "C++", sep=" | ")
    print("This is the first line.", end=" ")
    print("This is the second line.")

elif n==3:
    print("Got it! Here' s your third program\n\n")
    m=int(input("Select one option from the below.\n1:OR\n2:AND\n3:XOR\n4:Left Shift\n5:Right Shift\nYour response:"))
    if m==1:
         a=int(input("Enter the first number:"))
         b=int(input("Enter the second number:"))
         print(a|b)
    elif m==2:
        a=int(input("Enter the first number:"))
        b=int(input("Enter the second number:"))
        print(a&b)
    elif m==3:
        a=int(input("Enter the first number:"))
        b=int(input("Enter the second number:"))
        print(a^b)
    elif m==4:
        x=int(input("Enter the number you want to shift left:"))
        y=int(input("Enter the number with respect to whom you want to shift left:"))
        print(x<<y)
    elif m==5:
         x=int(input("Enter the number you want to shift right:"))
         y=int(input("Enter the number with respect to whom you want to shift right:"))
         print(x>>y)
    else:
        print("Invalid input")

else:
    print("Invalid input")


      
