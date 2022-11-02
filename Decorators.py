import datetime
import pathlib
from pathlib import Path


def summator(number1, number2):
    return number1 + number2

def logger(function):
    def open_write_file(*args, **kwargs):
        date_time = datetime.datetime.now()
        logger_path = Path(pathlib.Path.cwd(), "information_logger_file.txt")
        with open('information_logger_file.txt', 'a') as ilf:
            result = function(*args, **kwargs)
            ilf.write(f'Дата: {date_time}, Имя: {function}, Аргументы:{args}, Результат: {result}, Путь: {logger_path} \n')
            return result

    return open_write_file


summator = logger(summator)
num1 = summator(1, 1)
num2 = summator(3, 2)
result = summator(num1, num2)
print(result)