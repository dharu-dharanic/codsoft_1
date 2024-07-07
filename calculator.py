def calculate(a,b):
    op=input("Choose an operation:(+,-,*,/,%)")
    if op=='+':
        result=a+b
        print(a,"+",b,"=",result)
    elif op=='-':
        result=a-b
        print(a,"-",b,"=",result)
    elif op=='*':
        result=a*b
        print(a,"*",b,"=",result)
    elif op=='/':
        if b==0:
            print("division by zero is not possible")
        else:
            result=a/b
            print(a,"/",b,"=",result)
    elif op=='%':
        if b==0:
            print("division by zero is not possible")
        else:
            result=a%b
            print(a,"%",b,"=",result)
    else:
        print("Invalid Operation")
    return

a=float(input("Enter First Number:"))
b=float(input("Enter Second Number:"))
calculate(a,b)
