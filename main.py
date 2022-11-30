# 1) Вводим с клавиатуры целое число X и У.
# Выводим на экран количество чисел между Х и У, которые делятся на 2 и 3
# a = int(input("Введите 1 число: "))
# b = int(input("Введите 2 число: "))
# count = 0
# if a > b:
#     while a > b:
#         a -= 1
#         if a == b:
#             continue
#         if a % 2 == 0 and a % 3 == 0:
#             count += 1
#     print(f'{count} numbers')
# if a < b:
#     while a < b:
#         a += 1
#         if a == b:
#             continue
#         if a % 2 == 0 and a % 3 == 0:
#             count += 1
#     print(f'{count} numbers')

# 2) Вводим с клавиатуры целое число X
# Далее вводим Х целых чисел.
# Необходимо вывести на экран максимальное и второе максимальное число из введенных чисел.

# kol = int(input('Enter the number of digits: '))
# max_num = 0
# sec_num = 0
# for num in range(kol):
#     num = int(input('Enter a number: '))
#     if num > max_num and num > sec_num:
#         temp = max_num
#         sec_num = temp
#         max_num = num
# print(f'{max_num} - Max number')
# print(f'{sec_num} - Second max number')

# 3) Вводим с клавиатуры целое число - это зарплата.
# Нужно вывести в консоль - Минимальное кол-во купюр, которыми можно выдать ЗП.
# И сколько, и каких бухгалтер выдаст 25 рублевых купюр, 10 рублевых, 3 рублевых и 1 рублевых


# salary = int(input('Enter the amount of money: '))
# print(f'{salary} - это зарплата сотрудника ')
# one = salary // 25
# two = salary // 10
# three = salary // 3
# four = salary // 1
# if one < two or one < three or one < four:
#     print(f'{one} - это минимальное кол-во купюр которым можно выдать зп')
# elif two < one or two < three or two < four:
#     print(f'{two} - это минимальное кол-во купюр которым можно выдать зп')
# elif three < one or three < two or three < four:
#     print(f'{three} - это минимальное кол-во купюр которым можно выдать зп')
# else:
#     print(f'{four} - это минимальное кол-во купюр которым можно выдать зп')
# print(f'{one} купюр 25 рублевых')
# print(f'{two} купюр 10 рублевых')
# print(f'{three} купюр 3 рублевых')
# print(f'{four} купюр 1 рублевых')

# 4) Вводим с клавиатуры многозначное число
# Необходимо узнать и сказать последовательность цифр этого числа при просмотре слева направо упорядочена по возрастанию или нет.
# Например 1579 - да ( 1 меньше 5, 5 меньше 7, а 7 меньше 9), 1427 - нет

nums = input('Введите многозначное число: ')
index = len(nums) - 1
while index != 0:
    if nums[index] > nums[index - 1]:
        index -= 1
    else:
        break
if index == 0:
    print('Да')
else:
    print('Нет')
