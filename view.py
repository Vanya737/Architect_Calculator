# view.py

def display_result(result):
    print(f"Результат: {result}")

def get_user_input():
    num1 = float(input("Введите первое число: "))
    operator = input("Введите операцию (+, -, *, /): ")
    num2 = float(input("Введите второе число: "))
    return num1, operator, num2

def get_user_s():
    num_1 = float(input("Введите первую сторону: "))
    num_2 = float(input("Введите вторую сторону: "))
    return num_1, num_2

def get_pum():
    num_1 = float(input("Введите диаметр окружности: "))
    return num_1

def pir_cb():
    num_1 = float(input("Введите сторону: "))
    return num_1