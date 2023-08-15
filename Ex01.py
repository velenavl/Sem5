# Напишите функцию, которая принимает на вход строку -
# абсолютный путь до файла. Функция возвращает кортеж
# из трёх элементов: путь, имя файла, расширение файла.
# Ввод: c:/Users/Vladislav/Desktop/deep_to_python/test.txt
# Вывод: ( 'c:/Users/Vladislav/Desktop/deep_to_python/', 'test', '.txt')

import os

string = "Z:\Обмен\Учеба\Погружение в Python\5. Интераторы и генераторы\Sem5\Ex01.py"


def fun(f_path: str) -> tuple:
    path, filename = os.path.split(f_path)
    name, extension = filename.split('.')
    return path, name, extension


print(f'Исходная строка: {string} \nКортеж из пути: {fun(string)}')
