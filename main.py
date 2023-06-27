# Напишите рекурсивную функцию, которая принимает одномерный массив из 100 целых чисел заполненных
# случайным образом и находит позицию, с которой начинается последовательность из 10 чисел, сумма которых минимальна.
# import math
# import random
#
#
# def find_min_sum_index(numbers, start_index, end_index, min_sum=math.inf, min_index=0):
#     if end_index < len(numbers):
#         current_sum = sum(numbers[start_index:end_index + 1])
#
#         if current_sum < min_sum:
#             min_sum = current_sum
#             min_index = start_index
#
#         start_index += 1
#         end_index += 1
#
#         print(f"Min sum: {min_sum} Current sum: {current_sum}")
#
#         return find_min_sum_index(numbers, start_index, end_index, min_sum, min_index)
#
#     return min_index
#
#
# nums = [random.randint(1, 10) for num in range(100)]
# print(nums)
# result = find_min_sum_index(nums, 0, 1)
# print(result)

###
import random
import math
# # from random import *
# from random import randint, choice

# print(random.randint(1, 100))  # от 1 до 100
# print(random.random())
# print(random.choice("qwerty"))
# print(random.randrange(10))  # от нуля до 9
# print(random.randrange(2, 10))  # от 2 до 9
# print(random.randrange(2, 10, 2))  # от 2 до 9 через один (каждый второй)
# nums = [1, 2, 3, 4, 5]
# random.shuffle(nums)  # перемешиваем значения списка
# print(nums)

##
# print(-math.inf)
# print(math.inf)
# print(math.ceil(10.2))
# print(math.floor(10.999))
# print(math.factorial(5))
# print(math.pow(2, 3))
# print(math.sqrt(9))

##
# from decimal import *
#
# number = 0.1 + 0.1 + 0.1
# print(number)
# number = Decimal("0.1")
# number = number + number + number
# print(number)
#
# number = Decimal("0.333")
# number = number.quantize(Decimal("1.00"))
# print(number)
#
# number = Decimal("0.333")
# number = number.quantize(Decimal("1.0000"))
# print(number)
#
# number = Decimal("12.123456789")
# number = number.quantize(Decimal("1.000"))
# print(number)
#
# number = Decimal("12.5555")
# number = number.quantize(Decimal("1.000"))
# print(number)
#
# number = Decimal("12.9999")
# number = number.quantize(Decimal("1.000"))
# print(number)
#
# # округление происходит до ближайшего четного числа, если округляемая часть равна 5
# number = Decimal("12.025")
# number = number.quantize(Decimal("1.00"), ROUND_HALF_EVEN)
# print(number)
#
# number = Decimal("12.035")
# number = number.quantize(Decimal("1.00"), ROUND_HALF_EVEN)
# print(number)

###
# datetime
# import datetime as dt
#
# print(dt.date.today())
# print(dt.date(2022, 11, 10))
# print(dt.time())
# print(dt.time(10, 13, 15))
# print(dt.time(10, 13))
# #
# print(dt.datetime.now())
# dt_now = dt.datetime.now()
# print(f"{dt_now.day}/{dt_now.month}/{dt_now.year} {dt_now.hour}:{dt_now.minute}:{dt_now.second}:{dt_now.microsecond}")
# #
# print(dt.datetime)
# #
# my_date = dt.datetime.strptime("12/03/2020", "%d/%m/%Y")
# print(my_date)

# https://www.programiz.com/python-programming/datetime/strftime

# from datetime import datetime, timezone, timedelta
#
# # naive
# naive = datetime.now()
# print("Naive DateTime:", naive)
#
# # UTC aware
# UTC = datetime.now(timezone.utc)
# print("UTC DateTime", UTC)
#
# # Creating a datetime with JST (Japan) TimeZone
# jst_dateTime = datetime.now(timezone(timedelta(hours=+9), 'JST'))
# print("In JST::", jst_dateTime)

#####

# Генераторы коллекций
# list comprehension

# newlist = [expression for item in iterable (if condition)]

# iterable: перебираемый источник данных, в качестве которого может выступать список, множество, последовательность,
# либо даже функция, которая возвращает набор данных, например, range()
#
# item: извлекаемый из источника данных элемент
#
# expression: выражение, которое возвращает некоторое значение. Это значение затем попадает в генерируемый список
#
# condition: условие, которому должны соответствовать извлекаемые из источника данных элементы.
# Если элемент НЕ удовлетворяет условию, то он НЕ выбирается. Необязательный параметр.

# # v1
# numbers = [-1, 2, -3, 4, -5, 6, -7, 7]
# numbers_positive = []
# for num in numbers:
#     if num > 0:
#         numbers_positive.append(num)
#
# print(numbers_positive)
# #
# # # v2
# numbers_positive_2 = [num for num in numbers if num > 0]
# print(numbers_positive_2)

# #
# nums = [n for n in range(10)]
# print(nums)
#
# #
# nums = [n for n in range(10) if n % 2 == 0]
# print(nums)
#
# #
# users = {1: 'John', 2: 'Peter', 3: 'Max'}
# names = [name for name in users.values()]
# print(names)
#
# #
# users_data = [f"{key}: {users[key]}" for key in users.keys() if key > 2]
# print(users_data)
#
# #
# numbers = [-1, 2, -3, 4, -5, 6, -7, 7]
# numbers_positive_2 = tuple([num * 2 for num in numbers if num > 0])
# print(numbers_positive_2)
#
# #
# numbers = [-1, 2, -3, 4, -5, 6, -7, 7]
# new_numbers = [num * 2 if num > 5 else num for num in numbers if num > 0]
# print(new_numbers)
#
# # #
# my_dict = {i: i ** 2 for i in range(10)}
# print(my_dict)
#
# #
# my_set = {i for i in range(10)}
# print(my_set)

###
# Генераторные функции
# Генератор - это объект который сразу при создании не вычисляет значения всех своих элементов
# generator = (i for i in range(3))
# print(generator)
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))  # StopIteration
# close() -> остановка генератора
# throw() -> генератор бросит исключение

# for i in generator:
#     print(i)


# def create_generator():
#     number = 1
#     while True:
#         yield number
#         number += 1
#
#
# my_gen = create_generator()
# print(my_gen)
# try:
#     for i in my_gen:
#         print(i)
#         if i > 10:
#             my_gen.close()
#             # my_gen.throw(Exception("End!"))
# except Exception as e:
#     print(e)

###########
# \d — соответствует любой одной цифре и заменяет собой выражение [0-9];
# \D — исключает все цифры и заменяет [^0-9];
# \w — заменяет любую цифру, букву, а также знак нижнего подчёркивания;
# \W — любой символ кроме латиницы, цифр или нижнего подчёркивания;
# \s — соответствует любому пробельному символу;
# \S — описывает любой непробельный символ.
#
#
# .	Один любой символ, кроме новой строки \n.
# ?	0 или 1 вхождение шаблона слева
# +	1 и более вхождений шаблона слева
# *	0 и более вхождений шаблона слева
# \w	Любая цифра или буква (\W — все, кроме буквы или цифры)
# \d	Любая цифра [0-9] (\D — все, кроме цифры)
# \s	Любой пробельный символ (\S — любой непробельный символ)
# \b	Граница слова
# [..]	Один из символов в скобках ([^..] — любой символ, кроме тех, что в скобках)
# \	Экранирование специальных символов (\. означает точку или \+ — знак «плюс»)
# ^ и $	Начало и конец строки соответственно
# {n,m}	От n до m вхождений ({,m} — от 0 до m)
# a|b	Соответствует a или b
# ()	Группирует выражение и возвращает найденный текст
# \t, \n, \r	Символ табуляции, новой строки и возврата каретки соответственно
#
# Для чего используются регулярные выражения
# для определения нужного формата, например телефонного номера или email-адреса;
# для разбивки строк на подстроки;
# для поиска, замены и извлечения символов;
# для быстрого выполнения нетривиальных операций.
#
# А вот наиболее популярные методы, которые предоставляет модуль:
#
# re.match() - Этот метод ищет по заданному шаблону в начале строки
# re.search() - Метод похож на match(), но ищет не только в начале строки
# re.findall() - Возвращает список всех найденных совпадений.
# У метода findall() нет ограничений на поиск в начале или конце строки.
# re.split() - Этот метод разделяет строку по заданному шаблону
# re.sub() - Ищет шаблон в строке и заменяет его на указанную подстроку.
# Если шаблон не найден, строка остается неизменной
# re.compile() - Мы можем собрать регулярное выражение в отдельный объект, который может быть использован для поиска.
# Это также избавляет от переписывания одного и того же выражения.

import re

# result = re.match(r'he', 'hello world hello')
# print(result)
# print(result.group(0))
# #
# #
# result = re.search(r'world', 'hello world hello') # r - сырая строка
# print(result.start())
# print(result.end())
# #
# #
# result = re.findall(r'he', 'hello world hello')
# print(result)
# #
# #
# result = re.split(r'l', 'hello world hello', maxsplit=1)
# print(result)
# #
# result = re.split(r'l', 'hello world hello')
# print(result)
# #
# #
# pattern = re.compile('hello')
# result = pattern.findall('hello world hello')
# print(result)
#
# result = re.findall(r'.', "It is a long established fact that a reader")
# print(result)
#
# result = re.findall(r'\w', "It is a long established fact that a reader")
# print(result)
#
# result = re.findall(r'\w*', "It is a long established fact that a reader")
# print(result)
#
# result = re.findall(r'\w+', "It is a long established fact that a reader")
# print(result)
#
# result = re.findall(r'\w+$', "It is a long established fact that a reader")
# print(result)
#
# result = re.findall(r'^\w+', "It is a long established fact that a reader")
# print(result)
#
# result = re.findall(r'\w\w', "It is a long established fact that a reader")
# print(result)
#
# result = re.findall(r'\b\w', "It is a long established fact that a reader")
# print(result)
#
# result = re.findall(r'@\w+.\w+', "test1@gmail.com, test2@qqq.com, test3@www.com")
# print(result)
#
# result = re.findall(r'@\w+.(\w+)', "test1@gmail.com, test2@qqq.ua, test3@www.com")
# print(result)
#
# result = re.findall(r'\d{2}-\d{2}-\d{4}', 'Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-017-2004')
# print(result)
# #
# li = ['9999999999', '999999-999', '99999x9999']
#
# for val in li:
#     if re.match(r'[0-9]{1}[0-9]{9}', val) and len(val) == 10:
#         print('yes')
#     else:
#         print('no')

