# Метод списка Описание
# list.append(x) Добавляет элемент х в конец списка
# list.extend(L) Добавляет все элементы списка L в конец
# списка
# list.insert(i,x) Вставляет элемент x в позицию перед индексом
# i в списке
# list.remove(x) Удаляет первый элемент х из списка
# list.pop(i) Удаляет элемент с индексом i и возвращает его
# list.index(x) Возвращает индекс первого элемента х в списке
# list.count(x) Возвращает количество вхождений элемента x
# в список
# list.sort() Сортирует элементы списка по возрастанию
# list.reverse() Обращает порядок следования элементов

num = [1,2,3,4,5,4]
# добавим в конец
num.append(100)
print(num)

num1 = [55, 66, 77, 88, 99]
num.extend(num1)
print(num)
# добавить
num.insert(2, 9999)
print(num)
# сколько раз встраечается 4
n1 = num.count(4)
print(n1)
# удалим 9999
num.remove(9999)
print(num)
# удалим последний , если написать в скобках индекс удаляющего
num.pop()
print(num)
# сортировка
num.sort()
print(num)
num.reverse()
print(num)
# удалить 0 элемент
del num[0]
print(num)

# копирование списка
ori = [4,4,4,4,4,5,5,5,5,6,6,6,6]
copy = ori.copy()
copy1 = tuple(ori)
copy2 = ori[:]
# посчитаем колличество
len = len(copy2)
print(len)
# поиск в списке
print(4 in copy2)

sh = " молоко "
# убрать пробелы
sh.strip()
sh1 = sh.strip()
# Первая заглавная
print(sh1.capitalize())
# Большие
print(sh1.upper())
# Маленькие
print(sh1.lower())
print(sh1.isupper())

