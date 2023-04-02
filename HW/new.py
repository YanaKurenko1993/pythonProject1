import sys

num1 = int(input("PLease enter first number "))
num2 = int(input("Please enter second number "))
operator = input("PLease enter operator ")
if operator == "+":
    result = num1 + num2
    print(f"{num1} {operator} {num2} = {result}")
elif operator == "-":
    result = num1 - num2
    print(f"{num1} {operator} {num2} = {result}")
elif operator == "*":
    result = num1 * num2
    print(f"{num1} {operator} {num2} = {result}")
elif operator == '/' and num2 == 0:
    try:
        result = num1 / num2
    except ZeroDivisionError:
        print("На ноль делить нельзя")
        sys.exit()
elif operator == "/":
    result = num1 / num2
    print(f"{num1} {operator} {num2} = {result}")

