# controller.py
import model
import view

def run():
    while True:
        User = int(input("Вы хотите воспользоваться калькултором(Введите 1), нахождением S (Введите 2), длина окуржности (Введите 3), периметр квадрата(Введите 4): "))
        if User == 1:
            num1, operator, num2 = view.get_user_input()
            result = model.calculate(num1, num2, operator)
            view.display_result(result)
        elif User == 3:
            num_1 = view.get_pum()
            result = (model.calculate_2(num_1, User))
            view.display_result(result)
        elif User == 4:
            num_1 = view.pir_cb()
            result = (model.calculate_2(num_1, User))
            view.display_result(result)
        else:
            num_1, num_2 = view.get_user_s()
            result = model.calculate_3(num_1, num_2, User)
            view.display_result(result)



