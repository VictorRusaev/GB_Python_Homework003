# 1'. Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ:

import random
newList = []
for i in range(10):
    newList.append(random.randint(-10, 10))
print(newList)

notEvenList = newList[1::2]
print(sum(notEvenList))