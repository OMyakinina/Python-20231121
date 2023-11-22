"""Функция получает на вход текст вида: “1-й четверг ноября”, “3-я среда мая” и т.п.
Верните дату в текущем году, соответствующую этому тексту. Логируйте ошибки, если текст не соответсвует формату.
Логгируйте объект именованного кортежа с атрибутами, соответствующими дате, если дата существует"""

import argparse
import logging
import datetime 
from datetime import date, datetime
from collections import namedtuple

# Создаём своё универсальное исключений
class CustomException(Exception):
    "Пользовательское исключение на все слдучаи жизни:)"
    pass

# Логирование
logging.basicConfig(filename="task15_4.log", encoding="utf8", level=logging.DEBUG)
logger = logging.getLogger("log")

# Справочники
MONTH = {
    'января': 1,
    'февраля': 2,
    'марта': 3,
    'апреля': 4,
    'мая': 5,
    'июня': 6,
    'июля': 7,
    'августа': 8,
    'сентября': 9,
    'октября': 10,
    'ноября': 11,
    'декабря': 12
}
WEEKDAYS = {
    'понедельник': 0,
    'вторник': 1,
    'среда': 2,
    'четверг': 3,
    'пятница': 4,
    'суббота': 5,
    'воскресенье': 6
}
# Создаём именованный кортеж
DATE = namedtuple("DATE", "day month year")

# Метод поиска и формирования даты
def get_date(query):
    # Ловим исключения в работе
    try:
        # Начинаем новую сессию в логфайле
        logger.info("START: %s", datetime.now())
        # Разбираем данные пользовательского ввода
        num_week, week_day, month = query.split()
        # Получаем номер недели
        num_week = int(num_week.split("-")[0])

        # Получаем день недели
        week_day = WEEKDAYS.get(week_day)
        if week_day == None:
            raise CustomException("Такого дня недели не существует! Исправте запрос.")
        # Получаем месяц
        month = MONTH.get(month)
        if month == None:
            raise CustomException("Такого месяца не существует! Исправте запрос.")
        
        # Счетчик недель
        count_week = 0
        # Возвращаемая дата
        return_date = None
        tuple_data = None
        # Формируем дату
        for day in range(1, 31+1):
            # Создаём объект даты
            new_date = date(year=datetime.now().year, month=month, day=day)
            # Ищем нужный день недели
            if new_date.weekday() == week_day:
                # Считаем недели
                count_week += 1
                # Ищем нужную неделю
                if count_week == num_week:
                    return_date = new_date
                    tuple_data = DATE(return_date.day, return_date.month, return_date.year)
                    break
        if return_date == None:
            raise CustomException("Дата не найдена, попробуйте изменить содержание запроса.")

    # В случае возникновения исключения в ходе работы
    except Exception as e:
        # Пишем в логфайл
        logger.error("Ошибка: %s", e)
        # Выводим сообщение на экран
        print("Ошибка! Подробности в логфайле.")

    # В случае корректной работы, без исключений
    else:
        # Пишем в логфайл
        logger.info("Искомая дата: %s", tuple_data)
        # Выводим сообщение на экран
        print("Искомая дата: ", return_date)
    finally:
        # Пишем в логфайл
        logger.debug("Данные пользователя: %s", query)

# Тело программы
if __name__ == '__main__':
    # Создаём объект парсера для пользовательского запроса
    parser = argparse.ArgumentParser(description = 'User Query')
    # Создаём переменную запроса
    parser.add_argument('-q', '--query', type = str, help = 'Input user query')
    # Парсим данные
    args = parser.parse_args()
    if args.query:
        # Вызываем метод поиска
        get_date(args.query)
    else:
        # Вызываем метод поиска с запросом данных у пользователя
        get_date(input("Введите текст (пример: “1-й четверг ноября”): "))
