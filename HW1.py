import random


# 1) Сгенерировать dict() из списка ключей ниже по формуле (key : key* key). keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
# ожидаемый результат: {1: 1, 2: 4, 3: 9 …}

# keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# res = {x:x**2 for x in keys}
# print(res)

# ______________________

# 2)Сгенерировать массив(list()). Из диапазона чисел от 0 до 100 записать в результирующий массив только четные числа.

# some_list = [x for x in range(0,100) if not x % 2]
# print(some_list)

# ______________________

# 3)Заменить в произвольной строке согласные буквы на гласные.  
#
# some_str = "abcdefghijklmnopqrstuvwxyz"
# vowels = ('a', 'e', 'i', 'o', 'u')
# consonants = []
# for x in some_str:
#     if x not in vowels:
#         consonants.append(x)
#
# for x in some_str:
#     if x in consonants:
#        some_str = some_str.replace(x, random.choice(vowels))
# print(some_str)


# ______________________

# 4)Дан массив чисел. 

# some_list = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]

# 4.1) убрать из него повторяющиеся элементы

# # Если нужно сохранить порядок
# res = []
#
# for x in some_list:
#     if x not in res:
#         res.append(x)
# some_list = res
# print(some_list)
#
# # Если порядок не принципиален
# some_list = list(set(some_list))
# print(some_list)

# 4.2) вывести 3 наибольших числа из исходного массива

# res = sorted(list(set(some_list)))
# print(res)
#
# res_max = (res[::-1])[:3]
# print(res_max)

# 4.3) вывести индекс минимального элемента массива

# res = some_list.index(min(some_list))
# print(res)

# 4.4) вывести исходный массив в обратном порядке 
# res = some_list[::-1]
# print(res)
# ______________________

# 5) Найти общие ключи в двух словарях: 
#
# dict_one = { 'a': 1,'b': 2,'c': 3,'d': 4 }
# dict_two = { 'a': 6,'b': 7,'z': 20,'x': 40}
#
# res = []
# for key in dict_one.keys():
#     if key in dict_two.keys():
#         res.append(key)
# print(res)

# ______________________

# 6)Дан массив из словарей 
# data = [
#     {'name': 'Viktor', 'city': 'Kiev', 'age': 30},
#     {'name': 'Maksim', 'city': 'Dnepr', 'age': 20},
#     {'name': 'Vladimir', 'city': 'Lviv', 'age': 32},
#     {'name': 'Andrey', 'city': 'Kiev', 'age': 34},
#     {'name': 'Artem', 'city': 'Dnepr', 'age': 50},
#     {'name': 'Dmitriy', 'city': 'Lviv', 'age': 21}]

# 6.1) отсортировать массив из словарей по значению ключа ‘age'

# res = sorted(data, key=lambda i: i['age'])
# print(res)

# 6.2) сгруппировать данные по значению ключа 'city' 
# вывод должен быть такого вида :
# result = { 'Kiev': [ {'name': 'Viktor', 'age': 30 },{'name': 'Andrey', 'age': 34}], 'Dnepr': [ {'name': 'Maksim', 'age': 20 },
# {'name': 'Artem', 'age': 50}],'Lviv': [{'name': 'Vladimir', 'age': 32 }, {'name': 'Dmitriy', 'age': 21}] }


# data = [
#     {'name': 'Viktor', 'city': 'Kiev', 'age': 30},
#     {'name': 'Maksim', 'city': 'Dnepr', 'age': 20},
#     {'name': 'Vladimir', 'city': 'Lviv', 'age': 32},
#     {'name': 'Andrey', 'city': 'Kiev', 'age': 34},
#     {'name': 'Artem', 'city': 'Dnepr', 'age': 50},
#     {'name': 'Dmitriy', 'city': 'Lviv', 'age': 21}]
#
#
#
# res = {}
# for x in data:
#     copy_dict = x.copy()
#     del copy_dict["city"]
#     res.setdefault(x['city'], []).append(copy_dict)
# print(res)
# ______________________

# # 7) У вас есть последовательность строк. Необходимо определить наиболее часто встречающуюся строку в последовательности.
# # Например:
# #
# some_list = ['a', 'a', 'bi', 'bi','bi']
#
# def most_frequent(a):
#
#     a_set = set(a)
#
#     some = 0
#
#
#     for i in a_set:
#         count_item_a = a.count(i)
#         if count_item_a > some:
#             some = count_item_a
#             x = i
#     return x
#
# res = most_frequent(some_list)
# print(res)

# ______________________


# 8) Дано целое число. Необходимо подсчитать произведение всех цифр в этом числе, за исключением нулей.
# Например: Дано число 123405. Результат будет: 1*2*3*4*5=120.

# symbols = 123405
# symbols = list(str(symbols))
#
# res = 1
#
# for x in symbols:
#     x = int(x)
#     if x > 0:
#         res *= x
#
# print(res)

# ______________________

# 9) Есть массив с положительными числами и число n (def some_function(array, n)).
# Необходимо найти n-ую степень элемента в массиве с индексом n. Если n за границами массива, тогда вернуть -1.


# some_list = [1, 4, 2, 3, 33, 9]
#
# def some_function(value, n):
#
#     if (0 <= n) and (n < len(value)):
#         res = value[n]**n
#     else:
#         res = -1
#     return res
#
#
# result = some_function(some_list, 3)
# print(result)

# ______________________

# 10) Есть строка со словами и числами, разделенными пробелами (один пробел между словами и/или числами).
# Слова состоят только из букв. Вам нужно проверить есть ли в исходной строке три слова подряд.
# Для примера, в строке "hello 1 one two three 15 world" есть три слова подряд.
#
# some_value = "hello 1 one two three 15 world"
# a = some_value.split(' ')
#
# word_count = 3
# counter = 0
# counter_res = []
#
# for x in a:
#     if x.isalpha():
#         counter += 1
#     elif not x.isalpha():
#         counter = 0
#     counter_res.append(counter)
#
# if word_count in counter_res:
#     print("Три слова подряд в строке есть")
# else:
#     print("Трех слова подряд в строке нет")



