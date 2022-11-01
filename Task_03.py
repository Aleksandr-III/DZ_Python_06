# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# было

from random import randint

n = int(input('Введите количество элементов: '))
x = int(input('Введите минмальное значение: '))
y = int(input('Введите максимальное значение: '))
numbers = []
for i in range(n):
    numbers.append(randint(x, y))
print(numbers)


# # можно 1 вариант

l = numbers[0::2]
print(f'Числа в нечётных позициях {l}')
print(f'Сумма элементов на нечётных позициях {sum(l)}')


# # или 2 вариант

summ = 0
for i in range(0, len(numbers), 2):
        summ += numbers[i]       
print(f"{numbers} сумма элементов на нечётных позициях: {summ}")

# стало


numbers_list = numbers
sum_odd = sum(numbers_list[item] for item in range(0, len(numbers_list), 2))
odd_el = str([numbers_list[item] for item in range(0, len(numbers_list), 2)]).strip('[]')
print(f'{numbers_list} список\n{odd_el} элементы на нечётный позициях\nравна {sum_odd}.')