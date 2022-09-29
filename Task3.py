# Задайте список из n чисел последовательности (1+1/n)^n выведите на экран
#  их сумму.

n = int(input('n: '))
list =[]
sum = 0
for i in range(1, n + 1):
    i = round((1 + 1 / i)**i, 3) # округлила до 3 знака
    list.append(i)
    sum += i
print(list)
print(sum)