import os
import time


def process_directory(target_directory):
    for root, dirs, files in os.walk(target_directory):
        for file in files:
            print(format_file_info(root, file))


def format_file_info(root, file):
    file_path = os.path.join(root, file)
    file_time = os.path.getmtime(file_path)
    formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(file_time))
    file_size = os.path.getsize(file_path)
    parent_dir = os.path.dirname(file_path)

    return (f"Обнаружен файл: {file}, Путь: {file_path}, Размер: {file_size} байт, "
            f"Время изменения: {formatted_time}, Родительская директория: {parent_dir}")


if __name__ == "__main__":
    main_directory = "."  
    process_directory(main_directory)
