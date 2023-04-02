# # task 1
# health = int(input("введите число для здоровья персонажа "))
# if health <= 0:
#     print("False")
# else:
#     print("True")
# # task 2
# i = int(input("введите число "))
# if i % 2 == 0:
# #     print("Четное")
# # else:
# #     print("Нечетное")
# # Task 3
# # year = int(input("Введите год "))
# # if year % 4 == 0:
# #     if year % 100 == 0:
# #         if year % 400 == 0:
# #             print("высокосный")
# #         else:
# #             print("неВысокосный")
# #     else:
# #         print("Высокосный")
# # else:
# #     print("Невысокосный")
# # if not year % 4 and year % 100 or not year % 400:
# #     print("высокосный")
# # else:
# #     print("невысокосный")
# # text = str(input("Введите текст "))
# # times = int(input("введите количество раз повторения "))
# import sys
#
# i = 1
# # while i <= times:
# #     print(text)
# #     i += 1
# # Task 5
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





