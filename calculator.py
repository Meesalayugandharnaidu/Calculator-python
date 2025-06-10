a=int(input("Give a Number:"))
b=int(input("Give b Number:"))
operator=input("Give a Operator:")

if operator == "+":
    print("Addtiton:",a+b)
elif operator=="-":
    print("Subtraction:",a-b)
elif operator =="*":
    print("Multipication:",a*b)
elif operator=="/":
    print("Division:",a/b)
elif operator =="%":
    print("Modules:",a%b)
else:
   print("Invalid Operator")                    