""" Нерешенные задачи:
    1. Дни недели не совпадают с днями по календарю.
    2. Расписание только на 2 недели, далее нет. Можно было бы использовать цикл и его повторять.
    3. Не обращаемся конкретно к сотруднику/менеджеру, хотя это и не требуется в условии. """

import datetime
class Manufacture():

    def __init__(self):         # можно не задавать параметров
        pass
    #     self.name = name

    def time(self):         # создает список из дат, которые вводятся вручную
        print('Next schedule only for 2 weeks, choose dates.')
        day = int(input("Write start day in format XX: "))
        month = int(input("Write start month in format XX: "))
        year = int(input("Write start year in format XXXX: "))
        day1 = int(input("Write end day in format XX: "))
        month1 = int(input("Write end month in format XX: "))
        year1 = int(input("Write end year in format XXXX: "))
        start = datetime.datetime.strptime(f'{day}-{month}-{year}', "%d-%m-%Y")
        end = datetime.datetime.strptime(f'{day1 + 1}-{month1}-{year1}', "%d-%m-%Y")
        date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end - start).days)]
        keys = []
        for date in date_generated:
            keys.append(date.strftime("%d-%m-%Y"))
        return keys

    def manager(self):      # создает список из рабочих дней менеджеров в формате имя/имя/имя/имя и т.д
        n = 15
        list2 = []          # вот это список
        work_days = 3
        x = 'Manager Anna'
        y = 'Manager Oleg'
        while n > 0:
            while work_days != 0:
                list2.append(x)
                work_days -= 1
            work_days = 3
            while work_days != 0:
                list2.append(y)
                work_days -= 1
            n -= 3
            work_days = 3
        return list2

    def timetable(self):        # создает само расписание
        self.work1 = 'Workers: Vasya, Masha, Grisha'
        self.work2 = 'Workers: Olga, Sergey, Petr'
        list1 = [self.work1, self.work1, self.work2, self.work2, self.work1, 'day off', 'day off', self.work1,
                 self.work2, self.work2, self.work1, self.work1, 'day off', 'day off']
        k = list(zip(list1, self.manager()))        # склеить работников и менеджеров
        new_list = []       # список с работниками и менеджером
        for x in k:
            z = str(x)
            new_list.append(z[1:-1])
        timetable = dict(zip(self.time(), new_list))

        print("График работы работников:  Дата / Работники / Менеджер")
        for keys, values in timetable.items():
            print(keys, values)

Bulochnay = Manufacture()
print(Bulochnay.timetable())


""" нет смысла создавать столько экземпляров класса, т.к. они дальше не используются """
# Vasya = Workers1('Vasya')
# Masha = Workers1('Masha')
# Grisha = Workers1('Grisha')
# Olga = Workers1('Olga')
# Sergey = Workers1('Sergey')
# Petr = Workers1('Petr')

""" все что ниже можно не использовать, мы не трогаем отдельно менеджеров """
# class Manager(Parent):
#
#     def __init__(self, name):
#         self.name = name
#
#     def timetable(self):
#         timetable = dict(zip(self.time(), self.manager()))
#         print("График работы менеджеров:  Дата / Работники")
#         for keys, values in timetable.items():
#             print(keys, values)
#         # print(timetable)

# Oleg = Manager('Oleg')
# Anna = Manager('Anna')

