# model.py

def calculate_2(num_1, User):
    if User == 4:
        return num_1 * 4
    elif User == 3:
        return 3.14 * num_1

def calculate_3(num_1, num_2, User):
    if User == 2:
        return num_1 * num_2

def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "БРОСИТЬ!!!"