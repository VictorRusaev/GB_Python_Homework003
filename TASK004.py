# 4'. Напишите программу, которая будет преобразовывать 
# десятичное число в двоичное.

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# decimal = int(input('Введите число: '))
# binary = bin(decimal)
# print(binary)

# или

decimal = int(input('Введите число: '))
binary = ''
while decimal > 0:
    binary = str(decimal % 2) + binary
    decimal = decimal // 2
print(binary)