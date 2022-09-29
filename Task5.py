# Реализуйте алгоритм перемешивания списка (метод random.shuffle 
# использовать нельзя, но другие методы из библиотеки random - можно).

list = [1, 15, 23, 97, 5]
list_copy = list[:]
print(list)

from random import randint

n = len(list_copy)
for i in range(n):
    j = randint(0, n - 1) # получение случайного индекса
    temp = list_copy[i]
    list_copy[i] = list_copy[j]
    list_copy[j] = temp
print(list_copy)
