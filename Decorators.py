import datetime

def summator(number1, number2):
    print(number1 + number2)
    return number1 + number2

def logger(function):

    def open_write_file(*args, **kwargs):
        date_time = datetime.datetime.now()
        with open('information_logger_file.txt', 'a') as ilf:
            result = function(*args, **kwargs)
            ilf.write(f'Дата: {date_time}, Имя: {function}, Аргументы:{args}, Результат: {result} \n')

    return open_write_file

summator = logger(summator)
summator(87, 10)

