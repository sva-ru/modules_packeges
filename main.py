from application.salary import calculate_salary as cal_sl
from application.db.people import get_employees as empl
from datetime import datetime



if __name__ == '__main__':
    print(f'Текущая дата: {format(datetime.now(), "%d.%m.%Y")}')
    print(cal_sl())
    print(empl())
