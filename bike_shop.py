# --- продавцы, смены
# время работы: 5 дней в неделю, c 12 до 8
# на смене по 3 сотрудника сменяются 2 через 2
#  по 1 менеджер каждые 3 дня, даже в выходные

'''
дата: 01.30.2022
сотрудники: вася, маша, гриша
менеджер: аня
'''
import datetime


class Parent():
    def time(self):
        start = datetime.datetime.strptime("01-05-2021", "%d-%m-%Y")
        end = datetime.datetime.strptime("15-05-2021", "%d-%m-%Y")
        date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end - start).days)]
        keys = []
        for date in date_generated:
            keys.append(date.strftime("%d-%m-%Y"))
        return keys


class Workers1(Parent):

    def __init__(self, name):
        self.name = name


    def timetable(self):
        self.work1 = 'Vasya, Masha, Grisha'
        self.work2 = 'Olga, Sergey, Petr'
        list1 = [self.work1, self.work1, self.work2, self.work2, self.work1, 'd', 'd', self.work1, self.work2,
                 self.work2, self.work1, self.work1, 'd', 'd']
        timetable = dict(zip(self.time(), list1))
        # print(timetable)
        return timetable


Vasya = Workers1('Vasya')
Masha = Workers1('Masha')
Grisha = Workers1('Grisha')
Olga = Workers1('Olga')
Sergey = Workers1('Sergey')
Petr = Workers1('Petr')

print(Vasya.timetable())


class Manager(Parent):

    def __init__(self, name):
        self.name = name


    def timetable(self):
        n = 15
        list2 = []
        a = 3
        x = 'Anna'
        y = 'Oleg'
        while n > 0:
            while a != 0:
                list2.append(x)
                a -= 1
            a = 3
            while a != 0:
                list2.append(y)
                a -= 1
            n -= 3
            a = 3

        timetable = dict(zip(self.time(), list2))
        # print(timetable)
        return timetable


Oleg = Manager('Oleg')
Anna = Manager('Anna')
print(Anna.timetable())

# def week():
#
#     counter = int(input("Введите количество недель, которые хотите просмотреть: "))
#     week = {}
#     n = 1
#     while len(week) < counter:
#         week[n] = [5, 2]
#         n += 1
#     print(week)
#
# week()