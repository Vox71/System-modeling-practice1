import random as rnd

x0 = 1
y0 = 2
r0 = 5


def CALC_PI(x, y, r, ExpNmb):
    m = 0
    xmin = x - r
    xmax = x + r
    ymin = y - r
    ymax = y + r

    for i in range(ExpNmb):
        p = rnd.random()
        xp = (xmax - xmin) * p + xmin

        p = rnd.random()
        yp = (ymax - ymin) * p + ymin

        if (xp - x) ** 2 + (yp - y) ** 2 < r ** 2:
            m += 1

    pi = (m / ExpNmb) * 4
    return pi


def CALC_SERIA(ExpNmb):
    SERIA = []
    for f in range(3):
        exp = CALC_PI(x0, y0, r0, ExpNmb)
        SERIA.append(exp)
        ExpNmb = ExpNmb * 10
        print(SERIA[f])
    return SERIA


def CALC_EPS(SERIA):
    Eps = []
    for i in range(len(SERIA)):
        Epsi = abs((SERIA[i] - 3.1415926535) / 3.1415926535)
        Eps.append(Epsi)
    return Eps


def CALC_EPS_S(f):
    S = (SERIA_1[f] + SERIA_2[f] + SERIA_3[f] + SERIA_4[f] + SERIA_5[f]) / 5
    Eps_S = abs((S - 3.1415926535) / 3.1415926535)
    return Eps_S


def function(b):
    f = (b ** 3) + 1
    return f


def CALC_INTEGRAL(a, b, ExpNmb):
    xmin = a
    xmax = b
    ymin = 0
    ymax = function(b)
    m = 0
    for i in range(ExpNmb):
        p = rnd.random()
        x = (xmax - xmin) * p + xmin
        p = rnd.random()
        y = (ymax - ymin) * p + ymin
        if function(x) > y:
            m += 1
    Integral = (m / ExpNmb) * (b - a) * function(b)
    return Integral


print(f"Дана окружность с координатами центра {x0} и {y0} и радиусом {r0}")
print(f"Число Пи равно {CALC_PI(1, 2, 5, 10 ** 4)}")

print(f"Вектор серии экспериментов SERIA_1")
SERIA_1 = CALC_SERIA(10 ** 4)
print(f"Вектор серии экспериментов SERIA_2")
SERIA_2 = CALC_SERIA(10 ** 4)
print(f"Вектор серии экспериментов SERIA_3")
SERIA_3 = CALC_SERIA(10 ** 4)
print(f"Вектор серии экспериментов SERIA_4")
SERIA_4 = CALC_SERIA(10 ** 4)
print(f"Вектор серии экспериментов SERIA_5")
SERIA_5 = CALC_SERIA(10 ** 4)

Eps1 = CALC_EPS(SERIA_1)
print(f"Погрешность для 1й серии экспериментов:\n{Eps1}")
Eps2 = CALC_EPS(SERIA_2)
print(f"Погрешность для 2й серии экспериментов:\n{Eps2}")
Eps3 = CALC_EPS(SERIA_3)
print(f"Погрешность для 3й серии экспериментов:\n{Eps3}")
Eps4 = CALC_EPS(SERIA_4)
print(f"Погрешность для 4й серии экспериментов:\n{Eps4}")
Eps5 = CALC_EPS(SERIA_5)
print(f"Погрешность для 5й серии экспериментов:\n{Eps5}")

Eps_S_e4 = CALC_EPS_S(0)
print(f"Погрешность для усредненных значений для числа экспериментов 10^4 :\n{Eps_S_e4}")
Eps_S_e5 = CALC_EPS_S(1)
print(f"Погрешность для усредненных значений для числа экспериментов 10^5 :\n{Eps_S_e5}")
Eps_S_e6 = CALC_EPS_S(2)
print(f"Погрешность для усредненных значений для числа экспериментов 10^6 :\n{Eps_S_e6}")
# Eps_S_e7 = CALC_EPS_S(3)
# print(f"Погрешность для усредненных значений для числа экспериментов 10^7 :\n{Eps_S_e7}")
# Eps_S_e8 = CALC_EPS_S(4)
# print(f"Погрешность для усредненных значений для числа экспериментов 10^8 :\n{Eps_S_e8}")

Integral = CALC_INTEGRAL(0, 2, 10 ** 4)
print(f"Значение интеграла для f(x) = x^3 + 1 на интервале от 0 до 2:\n{Integral}")
