import random as rnd
import math
from concurrent.futures import ThreadPoolExecutor

x0 = 1
y0 = 2
r0 = 5
pi_num = math.pi
a0 = 0
b0 = 2
integral_theory = 6.0


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


def CALC_SERIA_PI(ExpNmb):
    SERIA = []
    for f in range(5):
        SERIA.append(CALC_PI(x0, y0, r0, ExpNmb))
        ExpNmb = ExpNmb * 10
    return SERIA



def CALC_EPS(SERIA):
    Eps = []
    for i in range(len(SERIA)):
        Eps.append(abs((SERIA[i] - pi_num) / pi_num))
    return Eps



def CALC_EPS_S(f, seria1, seria2, seria3, seria4, seria5, num):
    Eps_S = abs(((seria1[f] + seria2[f] + seria3[f] + seria4[f] + seria5[f]) / 5 - num) / num)
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

def CALC_SERIA_INTEGRAL(ExpNmb):
    SERIA = []
    for f in range(5):
        SERIA.append(CALC_INTEGRAL(a0, b0, ExpNmb))
        ExpNmb = ExpNmb * 10
    return SERIA


print(f"Дана окружность с координатами центра {x0} и {y0} и радиусом {r0}")
print(f"Теоретическое значение числа Пи: {pi_num}")
print(f"Число Пи равно {CALC_PI(1, 2, 5, 10 ** 4)}")


# Запускаем 5 потоков, каждый из которых создает серию экспериментов из функции CALC_SERIA
with ThreadPoolExecutor() as calc_pi_serias:
    SERIA_1 = calc_pi_serias.submit(CALC_SERIA_PI, 10 ** 4).result()
    SERIA_2 = calc_pi_serias.submit(CALC_SERIA_PI, 10 ** 4).result()
    SERIA_3 = calc_pi_serias.submit(CALC_SERIA_PI, 10 ** 4).result()
    SERIA_4 = calc_pi_serias.submit(CALC_SERIA_PI, 10 ** 4).result()
    SERIA_5 = calc_pi_serias.submit(CALC_SERIA_PI, 10 ** 4).result()


print(f"Вектор серии экспериментов SERIA_1: {SERIA_1}")
print(f"Вектор серии экспериментов SERIA_2: {SERIA_2}")
print(f"Вектор серии экспериментов SERIA_3: {SERIA_3}")
print(f"Вектор серии экспериментов SERIA_4: {SERIA_4}")
print(f"Вектор серии экспериментов SERIA_5: {SERIA_5}")

# Запускаем 5 потоков, каждый из которых считает погрешности для каждой серии экспериментов соответственно
with ThreadPoolExecutor() as calc_pi_eps:
    Eps1 = calc_pi_eps.submit(CALC_EPS, SERIA_1).result()
    Eps2 = calc_pi_eps.submit(CALC_EPS, SERIA_2).result()
    Eps3 = calc_pi_eps.submit(CALC_EPS, SERIA_3).result()
    Eps4 = calc_pi_eps.submit(CALC_EPS, SERIA_4).result()
    Eps5 = calc_pi_eps.submit(CALC_EPS, SERIA_5).result()

print(f"Погрешность для 1й серии экспериментов:{Eps1}")
print(f"Погрешность для 2й серии экспериментов:{Eps2}")
print(f"Погрешность для 3й серии экспериментов:{Eps3}")
print(f"Погрешность для 4й серии экспериментов:{Eps4}")
print(f"Погрешность для 5й серии экспериментов:{Eps5}")

# Запускаем 5 потоков, каждый из которых считает погрешность для усредненных средних значений,
# для разных значений числа экспериментов соответственно
with ThreadPoolExecutor() as cals_pi_eps_s:
    Eps_S_e4 = cals_pi_eps_s.submit(CALC_EPS_S, 0, SERIA_1, SERIA_2, SERIA_3, SERIA_4, SERIA_5, pi_num).result()
    Eps_S_e5 = cals_pi_eps_s.submit(CALC_EPS_S, 1, SERIA_1, SERIA_2, SERIA_3, SERIA_4, SERIA_5, pi_num).result()
    Eps_S_e6 = cals_pi_eps_s.submit(CALC_EPS_S, 2, SERIA_1, SERIA_2, SERIA_3, SERIA_4, SERIA_5, pi_num).result()
    Eps_S_e7 = cals_pi_eps_s.submit(CALC_EPS_S, 3, SERIA_1, SERIA_2, SERIA_3, SERIA_4, SERIA_5, pi_num).result()
    Eps_S_e8 = cals_pi_eps_s.submit(CALC_EPS_S, 4, SERIA_1, SERIA_2, SERIA_3, SERIA_4, SERIA_5, pi_num).result()

print(f"Погрешность для усредненных значений для числа экспериментов 10^4 :{Eps_S_e4}")
print(f"Погрешность для усредненных значений для числа экспериментов 10^5 :{Eps_S_e5}")
print(f"Погрешность для усредненных значений для числа экспериментов 10^6 :{Eps_S_e6}")
print(f"Погрешность для усредненных значений для числа экспериментов 10^7 :{Eps_S_e7}")
print(f"Погрешность для усредненных значений для числа экспериментов 10^8 :{Eps_S_e8}")

print(f"\n\nЗначение интеграла считаем для f(x) = x^3 + 1 на интервале от 0 до 2.")
print(f"Теоретическое значение интеграла: {integral_theory}")

with ThreadPoolExecutor() as calc_int_serias:
    SERIA_INT_1 = calc_int_serias.submit(CALC_SERIA_INTEGRAL, 10 ** 4).result()
    SERIA_INT_2 = calc_int_serias.submit(CALC_SERIA_INTEGRAL, 10 ** 4).result()
    SERIA_INT_3 = calc_int_serias.submit(CALC_SERIA_INTEGRAL, 10 ** 4).result()
    SERIA_INT_4 = calc_int_serias.submit(CALC_SERIA_INTEGRAL, 10 ** 4).result()
    SERIA_INT_5 = calc_int_serias.submit(CALC_SERIA_INTEGRAL, 10 ** 4).result()

print(f"Вектор серии экспериментов SERIA_INT_1: {SERIA_INT_1}")
print(f"Вектор серии экспериментов SERIA_INT_2: {SERIA_INT_2}")
print(f"Вектор серии экспериментов SERIA_INT_3: {SERIA_INT_3}")
print(f"Вектор серии экспериментов SERIA_INT_4: {SERIA_INT_4}")
print(f"Вектор серии экспериментов SERIA_INT_5: {SERIA_INT_5}")

with ThreadPoolExecutor() as calc_int_eps:
    Eps1_int = calc_int_eps.submit(CALC_EPS, SERIA_INT_1).result()
    Eps2_int = calc_int_eps.submit(CALC_EPS, SERIA_INT_2).result()
    Eps3_int = calc_int_eps.submit(CALC_EPS, SERIA_INT_3).result()
    Eps4_int = calc_int_eps.submit(CALC_EPS, SERIA_INT_4).result()
    Eps5_int = calc_int_eps.submit(CALC_EPS, SERIA_INT_5).result()

print(f"Погрешность для 1й серии экспериментов:{Eps1_int}")
print(f"Погрешность для 2й серии экспериментов:{Eps2_int}")
print(f"Погрешность для 3й серии экспериментов:{Eps3_int}")
print(f"Погрешность для 4й серии экспериментов:{Eps4_int}")
print(f"Погрешность для 5й серии экспериментов:{Eps5_int}")

with ThreadPoolExecutor() as calc_int_eps_s:
    Eps_S_e4_int = calc_int_eps_s.submit(CALC_EPS_S, 0, SERIA_INT_1, SERIA_INT_2, SERIA_INT_3, SERIA_INT_4, SERIA_INT_5, integral_theory).result()
    Eps_S_e5_int = calc_int_eps_s.submit(CALC_EPS_S, 1, SERIA_INT_1, SERIA_INT_2, SERIA_INT_3, SERIA_INT_4, SERIA_INT_5, integral_theory).result()
    Eps_S_e6_int = calc_int_eps_s.submit(CALC_EPS_S, 2, SERIA_INT_1, SERIA_INT_2, SERIA_INT_3, SERIA_INT_4, SERIA_INT_5, integral_theory).result()
    Eps_S_e7_int = calc_int_eps_s.submit(CALC_EPS_S, 3, SERIA_INT_1, SERIA_INT_2, SERIA_INT_3, SERIA_INT_4, SERIA_INT_5, integral_theory).result()
    Eps_S_e8_int = calc_int_eps_s.submit(CALC_EPS_S, 4, SERIA_INT_1, SERIA_INT_2, SERIA_INT_3, SERIA_INT_4, SERIA_INT_5, integral_theory).result()

print(f"Погрешность для усредненных значений для числа экспериментов 10^4 :{Eps_S_e4_int}")
print(f"Погрешность для усредненных значений для числа экспериментов 10^5 :{Eps_S_e5_int}")
print(f"Погрешность для усредненных значений для числа экспериментов 10^6 :{Eps_S_e6_int}")
print(f"Погрешность для усредненных значений для числа экспериментов 10^7 :{Eps_S_e7_int}")
print(f"Погрешность для усредненных значений для числа экспериментов 10^8 :{Eps_S_e8_int}")