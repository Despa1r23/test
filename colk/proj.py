print( '*' * 15,"Привет, это Калькулятор выполняющий простые вычисления для двух чисел",'*' * 15, sep='')
print("Для выхода введите q в качестве знака операции")
while True:
    sign = input("Введите знак (+,-,*,/): ")
    if sign.lower() == "q" : break

    if sign in ("+","-","*","/"):
        num_1 = float(input("Первое число = "))
        num_2 = float(input("Второе число = "))
        if sign == "+":
            print(num_1 + num_2)
        elif sign == "-":
            print(num_1 - num_2)
        elif sign == "*":
            print(num_1 * num_2)
        elif sign == "/":
            if num_2 != 0:
                print(num_1 / num_2)
            else:
                print("Делить на 0 нельзя")
    else:
        print("Вы ввели неверный знак операции")

