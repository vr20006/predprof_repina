def read_txt():  # открытие txt файла и чтение в списочное выражение
    f = open('astronaut_time.txt', encoding='utf-8')
    a = [[j for j in i.split('>')] for i in f]
    a = a[1:]
    return a


def add_time_now():  # создание массива для записи в новый файл, с добавлением поля timeNow
    s = read_txt()
    for i in s:
        t = i[3].split(':')
        hours = int(t[0]) + int(i[4])
        i.pop(-1)
        i.append(f'{hours}:{t[1]}:{t[2]}\n')
    return s


def write_csv():  # новый массив записывается в csv-файл
    f = open('new_time.csv', 'w')
    f.write('WatchNumber>numberStation>cabinNumber>timeStop>timeNow>\n')
    for i in add_time_now():
        i = '>'.join(i)
        f.write(i)
    f.close()


write_csv()

for i in open('new_time.csv'): # поиск заданной в задании каюты
    j = i.split('>')
    if j[2] == '98-OYE':
        print(j[-1])
