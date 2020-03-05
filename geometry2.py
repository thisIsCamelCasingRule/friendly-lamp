import geometry

def find_third_point(m1: list, s: list, l: int) -> list:
    """
        Выводит третью точку при заданом собственном числе лямбда.
        Проверка на ввод всех данных. На выходе получаем список, его же и возвращаем
    """
    if type(m1) is not list:
        print("Not correct input of m1!!!")
        return
    elif type(s) is not list:
        print("Not correct input of s!!!")
        return
    elif type(l) is not int:
        print("Not correct input of l!!!")
        return

    m3 = [s[0] * l + m1[0], s[1] * l + m1[1], s[2] * l + m1[2]]
    return m3

def enter_the_point(x: float, y: float, z: float) -> list:

        if type(x) is not float:
            print("The point x have to be type of float or int!!!")
            print(type(x))
            return

        if type(y) is not float:
            print("The point y have to be type of float or int!!!")
            return

        if type(z) is not float:
            print("The point z have to be type of float or int!!!")
            return
        v = [x, y, z]
        return v

def enter_the_point_2() -> list:
    """
        Видает список точек после проверки на корректный ввод.
        Тип данних точек - флоат, если нет - идем в эксепшн а затем в цикл
    """
    while True:
        try:
            print("Input the cordinates:\n")

            print("X: ")
            x = float(input())
            print("Y: ")
            y = float(input())
            print("Z: ")
            z = float(input())

            m = [x, y, z]
            if m:
                print("The point was created: ", m)
                return m
        except:
            print("Not correct input")
            continue
