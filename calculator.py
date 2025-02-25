def add(a,b):
    return a+b

def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

num1=int(input("enter first number"))
num2=int(input("enter second number"))

operation1=input("choose a operation 1.+ \n 2.- \n 3.* \n 4./ \n")
if operation1=='1':
    a = add(num1,num2)
    print(num1, "+", num2, "=", a)
elif operation1=='2':
    a = sub(num1,num2)
    print(num1, "-", num2, "=",a)
elif operation1=='3':
    a = mul(num1,num2)
    print(num1, "*", num2, "=",a)
elif operation1=='4':
    a = div(num1,num2)
    print(num1, "/", num2, "=",a)



