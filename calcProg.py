def calculator():
    while True:
        print("1.addition\n2.subtraction\n3.mutiplication")
        choice=int(input("Enter your choice:"))
        if choice in [1,2,3]:
            a=int(input("Enter 1st number:"))
            b=int(input("Enter 2nd number:"))
            print("Result=",end="")
            if choice==1:
                c=int(a+b)
                print(c)
            elif choice==2:
                d=int(a-b)
                print(d)
            elif choice==3:
                e=float(a*b)
                print(e)
        else:
            print("Invalid Choice")
        ch=input("Do you wish to continue ?[Y/N]: ")
        if ch=='N':
            break

calculator()