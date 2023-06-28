import re
# Написать валидации с помощью регулярных выражений:
#
# - мобильный номер телефона (только цифры, возможное наличие плюса, длина номера)
# Валидация В виде +38 (063) 567-12-23
# def validate_mobile_number(number):
#     pattern ='^\+38\s\(0[1-9]{2}\)\s\d{3}-\d{2}-\d{2}$'
#     pattern_1 = '^\(0[1-9]{2}\)\s\d{3}-\d{2}-\d{2}$'
#     if re.match(pattern, number) or re.match(pattern_1, number):
#         print("It is valid mobile number")
#     else:
#         print("It is not valid mobile number")
#
# try:
#     validate_mobile_number("+38 (063) 567-12-23")
#     validate_mobile_number("(063) 567-12-23")
#     validate_mobile_number("+38 (123) 356-14-15")
# except Exception as error:
#     print(error)
######
# - домашний номер телефона (только цифры и длина номера)

# def validate_home_number(number):
#     pattern = r'^\d{3}-\d{2}-\d{2}$'
#     if re.match(pattern, number):
#         print("It is valid phone number")
#     else:
#         print("It is not valid phone number")
#
# try:
#     validate_home_number("755-64-50")
#     validate_home_number("755-64-50 56")
#     validate_home_number("8684-57-356")
# except Exception as error:
#     print(error)

########
# - email (наличие @, домена: gmail.com например, минимальная длина и максимальная на ваш выбор)

# def validate_email(email):
#     pattern = r'^[\w\.-]{3,15}@[\w\.-]{3,10}\.\w{2,6}$'
#     if re.match(pattern, email):
#         print("It`s valid email")
#     else:
#         print("It`s not valid email")
#
# try:
#     validate_email("Kitty@hello.cat")
#     validate_email(("ki123@hello.ca"))
#     validate_email("A12342@mik.com")
#     validate_email("notvalid@email.c")
#
# except Exception as error:
#     print(error)
#
# - ФИО клиента (3 слова, минимальная длина 2 символа, максимальная длина 20)
# Допустим, что можно вводить ФИО только с большой буквы, т.к. правописание.

# def client_name(name):
#     pattern =r'^[A-Z]{1}[a-z]{1,19}\s[A-Z]{1}[a-z]{1,19}\s[A-Z]{1}[a-z]{1,19}$'
#     if re.match(pattern, name):
#         print(f"Hello, {name}")
#     else:
#         print("Invalid name, please check it.")
#
# try:
#     client_name("Ivanov Ivan Ivanovich")
#     client_name("ivanov ivan ivanovich")
#     client_name("Sooooooooooooloooooong Name Name")
# except Exception as error:
#     print(error)
#
# дополнительно:
#
# - Пароль (минимально: одна большая буква, одна маленькая буква, одна цифра, один символ,
# длина пароля - от 8 до 16 символов)

def password_validation(password):
    # pattern = r'^(?=.+[a-z])(?=.+[A-Z])(?=.+\d)(?=.+\W)[a-zA-Z\d\W]{8,16}$' - с плюсами не работает
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*\W)[a-zA-Z\d\W]{8,16}$'
    # в части (?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*\W) проверяем, что есть хотя бы 1 символ каждого типа
    # в части [a-zA-Z\d\W]{8,16} пишем, что этих символов должно быть от 8 до 16
    if re.match(pattern, password):
        print(f"Your password is confirmed: {password}")
    else:
        print("Please, enter another password")

try:
    password_validation("Password123!")
    password_validation("Som3th1ng@*")
    password_validation("password23")
except Exception as error:
    print(error)
