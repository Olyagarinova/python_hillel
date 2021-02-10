# ЗАДАЧА-1
# Написать свой декоратор который будет проверять остаток от деления числа 100 на результат работы функции ниже.
# Если остаток от деления = 0, вывести сообщение "We are OK!», иначе «Bad news guys, we got {}» остаток от деления.

from functools import wraps


# def check_decorator(func):
#     @wraps(func)
#     def inner(arg):
#         res = 100 % func(arg)
#         if res == 0:
#             print("We are OK!")
#         else:
#             print(f"Bad news guys, we got {res}")
#     return inner
#
#
# @check_decorator
# def sqr(arg):
#     """The function squares the arg"""
#     return arg**2
#
#
# sqr(3)


# ЗАДАЧА-2
# Написать декоратор который будет выполнять предпроверку типа аргумента который передается в вашу функцию.
# Если это int, тогда выполнить функцию и вывести результат, если это str(),
# тогда зарейзить ошибку ValueError (raise ValueError(“string type is not supported”))


# def check_type_decorator(func):
#     @wraps(func)
#     def inner(a):
#         arg = func(a)
#         value_type = type(arg)
#         if value_type == int:
#             print(arg)
#         elif value_type == str:
#             raise ValueError("string type is not supported")
#     return inner
#
#
# @check_type_decorator
# def test(a):
#     return a*2
#
#
# test(5)
# test("qwerty")




# ЗАДАЧА-3
# Написать декоратор который будет кешировать значения аргументов и результаты работы вашей функции и записывать
# его в переменную cache. Если аргумента нет в переменной cache и функция выполняется, вывести сообщение
# «Function executed with counter = {}, function result = {}» и количество раз сколько эта функция выполнялась.
# Если значение берется из переменной cache, вывести сообщение «Used cache with counter = {}» и
# количество раз обращений в cache.



def my_decorator(func):
    cache = {}

    def wrapper(a):
        if a not in cache:
            return arg(arg)
        else:
            print("Used cache with counter = {}")
    return wrapper

@my_decorator
def test(arg):
    return arg*2


# res = test(arg)
# print(res)

test(2)




