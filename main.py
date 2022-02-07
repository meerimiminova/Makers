from json.tool import main
import schedule
import time
import csv

# db = {}
def write_csv():
    name = input('enter name: ')
    age = input('enter age: ')
    with open('users.csv', 'a') as csv_file:
        writer = csv.writer(csv_file, delimiter = '/')
        writer.writerow(
            (name, age)
        )
        answ = input('yes or no: ')
        if answ == 'y':
            write_csv()
        else:
            print('Stop')

def mailing():
    with open('users.csv', 'r') as csv_file:
        data = csv_file.readlines()
        names = [i.replace('\n', '') for i in data]
        for i in names:
            name = i.split('/')
            if int(name[-1]) >= 18:
                print(f'Скидки сегодня! {name[0]}')

schedule.every(3).seconds.do(mailing)

while True:
    schedule.run_pending()
    time.sleep(1)

mailing()
# write_csv()

# git remote add origin привязка из Code SSH
# git remote -v   -  проверка на привязку
# git pull origin main
# git branch -v  -  ПРОВЕРИТЬ ВЕТКУ
# git branch vetka     -     Создание ветки
# git checkout название ветки     -     переключиться на другую ветку




