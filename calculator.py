def add(a,b):
    return a+b
def subtract (a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
        return "error! divison by zero"
    return a/b
print("....simple calculator.....")
print("select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("enter choice(1/2/3/4):")
num1 = float(input("entre first number:"))
num2 = float(input("entre second number:"))

if choice == '1':
    print("result:", add(num1,num2))
elif choice == '2':
    print("result:",subtract(num1,num2))
elif choice == '3':
    print("result:",multiply(num1,num2))
elif choice =='4':
    print("result:",divide(num1,num2))
else:
    print("invalid input") 
          