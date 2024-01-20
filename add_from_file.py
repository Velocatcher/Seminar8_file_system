from return_data_file import data_file
from print_data import print_file
import re

def add_from_file():
    data, nf = data_file()
    count_rows = len(data)
    

    if count_rows == 0:
        print("Файл пусто!")
    else:
        number_row = int(input(f"Введите номер строки "
                               f"от 1 до {count_rows}: "))
        while number_row < 1 or number_row > count_rows:
            number_row = int(input(f"Ошибка!"
                                   f"Введите номер строки "
                                   f"от 1 до {count_rows}: "))
        
    if nf == 1:
        nf = 2
    else:
        nf = 1 

    add_line = re.split(";|\n", data[number_row - 1])
    del add_line[-1]
       
       

    with open(f'db/data_{nf}.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()
    # Здесь! Меняем файлы
    now_number_row = len(data) + 1
    print(now_number_row)
    name = add_line[1]
    surname = add_line[2]
    birthdate = add_line[3]
    town = add_line[4]
    with open(f'db/data_{nf}.txt', 'a', encoding='utf-8') as file:
        
         file.write(f'{now_number_row};{name};'
         f'{surname};{birthdate};{town}\n')
    print_file()
    print("Данные успешно записаны!")
