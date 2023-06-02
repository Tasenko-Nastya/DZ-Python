# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

# n = input().split()
# m = input().split()
# firs = [int() for i in input().split()]
# sec = [int() for j in input().split()]
# print(*sorted(set(firs).intersection(sec)))

# print(*sorted(set(input().split()) & set(input().split()), key=int))


n = int(input('Введите количество элементов n: '))
# lst = [i for i in range(1, n+1)]
lst1 = []
for i in range(n):
     num = int(input('введите целое число: '))
     lst1.append(num)
print(lst1)

m = int(input('Введите количество элементов m: '))
# lst = [i for i in range(1, n+1)]
lst2 = []
for i in range(m):
     num = int(input('введите целое число: '))
     lst2.append(num)
print(lst2)

print(*sorted(set(lst1).intersection(lst2)))



      
