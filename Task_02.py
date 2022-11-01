
# Задание 1 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23

# Было

# x = input('Введите число: ')
# sum_ = 0
# for i in x:
#     if i != '.':
#         sum_ += int(i)
# print(f'Сумма введёных чисел {sum_}')


# Стало

sum_digits = lambda number: 0 if number == 0 else (number % 10) + sum_digits (number//10)
print(sum_digits(int(input('Введите число: '))))
