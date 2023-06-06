# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

def mass_(n):
    lst=[]
    for i in range(n):
        lst.append(random.randint(-10,10))
    return lst

n = int(input('введите количество элементов: '))
lst1 = mass_(n)
print(lst1)
maxi = int(input('Задайте максимум диапазон: '))
mini = int(input('Задайте минимум диапазона: '))
for i in range(len(lst1)):
    if mini <= lst1[i] <= maxi:
        print(i)

