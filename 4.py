a=int(input("enter a number: "))
b=int(input("enter a number: "))
op=input("enter a operator:+,-,*,/: ")
if op=="+":
    print(a+b)
elif op=="-":
    print(a-b)
elif op=="*":
    print(a*b)
elif op=="/":
    print(a/b)
else:
    print("invalid operator")

