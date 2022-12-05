# 3'. Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между 
# максимальным и минимальным значением дробной части элементов.

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19 
# (максимальное значение у числа 1.2 , минимальное у 10.01)

newList = [1.1, 1.2, 3.1, 5, 10.01]
print(newList)
for item in newList:
    if type(item) == int:
        newList.remove(item)

intPart = []
for item in newList:
    intPart.append((str(item).split('.')[0]))

fractionPart = []
for i in range(len(newList)):
    fractionPart.append(round(newList[i] - int(intPart[i]), 2))

max = fractionPart[i]
min = fractionPart[i]
for j in range(len(fractionPart)):
    if fractionPart[j] > max:
        max = fractionPart[j]
    if fractionPart[j] < min:
        min = fractionPart[j]
print('Максимальная дробная часть = ', max)
print('Минимальная дробная часть = ', min)
print()
print('Разница между ними =', max - min)