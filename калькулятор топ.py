def main():
    print ("Это калькулятор который написан на языке программирования Python")
    while True:
        print ("Выберите действие которое хотите совершить:\n"
        "Сложить: +\n"
        "Вычесть: -\n"
        "Умножить: *\n"
        "Поделить: /\n"
        "Выйти q\n")
        Action = input("Действие: ")
        if Action == "q":
            print ("Программа завершена")
            break
        if Action in ("+", "-", "*", "/"):
            x = float(input("x= "))
            y = float(input("y= "))
            if Action == "+":
                print ("%.2f + %.2f = %.2f" % (x, y, x+y))
            elif Action == "-":
                print ("%.2f - %.2f = %.2f" % (x, y, x-y))
            elif Action == "*":
                print ("%.2f * %.2f = %.2f" % (x, y, x*y))
            elif Action == "/":
                if y != 0:
                    print('%.2f / %.2f = %.2f' % (x, y, x/y))
            else:
                print ("Деление на ноль невозможно")


if __name__ == "__main__":
    main()