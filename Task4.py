# Задайте числами список из N элементов, заполненных из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в 
# файле file.txt в одной строке одно число.

n = int(input('Введите число '))
list = []
for i in range(-n,n+1):
    list.append(i)
print(list)

with open('file.txt', 'w') as data:
    data.write('1 \n')
    data.write('2 \n')

mult = 1
path = 'file.txt'
data = open(path, 'r')
for line in data:
    mult *= list[int(line)]
print(mult)