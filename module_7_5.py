import os
import time


directory = "."

for root, dirs, files in os.walk(directory): # обход каталога
    for file in files:
        filepath = os.path.join(root, file)  # формирование полного пути к файлу
        filetime = os.path.getmtime(filepath) # время последнего изменения файла
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(filepath) # размер файла
        parent_dir = os.path.dirname(filepath) # родительская директория файла

print(f'Обнаружен файл: {file},\n'
      f'Путь: {filepath},\n'
      f'Размер: {filesize} байт,\n'
      f'Время изменения: {formatted_time},\n'
      f'Родительская директория: {parent_dir}')
