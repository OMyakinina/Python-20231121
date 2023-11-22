"""
Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
Соберите информацию о содержимом в виде объектов namedtuple. 
Каждый объект хранит:
* имя файла без расширения или название каталога, 
* расширение, если это файл, 
* флаг каталога, 
* название родительского каталога. 
В процессе сбора сохраните данные в текстовый файл используя логирование.
"""

import os
import logging
from collections import namedtuple

logging.basicConfig(filename='last.log', level=logging.INFO)

FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent_directory'])

def get_directory_info(directory_path):
    try:
        directory_content = os.listdir(directory_path)

        for item in directory_content:
            item_path = os.path.join(directory_path, item)
            is_directory = os.path.isdir(item_path)
            parent_directory = os.path.basename(directory_path)

            if is_directory:
                file_info = FileInfo(name=item, extension='', is_directory=True, parent_directory=parent_directory)
            else:
                name, extension = os.path.splitext(item)
                file_info = FileInfo(name=name, extension=extension, is_directory=False, parent_directory=parent_directory)

            logging.info(file_info)

    except Exception as e:
        logging.error(f'Ошибка при получении информации о содержимом директории: {str(e)}')

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Пожалуйста, укажите путь до директории")
    else:
        directory_path = sys.argv[1]
        get_directory_info(directory_path)
