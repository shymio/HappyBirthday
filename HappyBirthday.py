happy_b = dict()

def welcome():
    print()
    print("----------------------------------")
    print("---  Справочник Дней Рождений  ---")
    print("----------------------------------")



def menu():
    print()
    print("Режимы работы:")
    print("1. Показать все записи")
    print("2. Добавить запись")
    print("3. Редактировать запись")
    print("4. Удалить запись")
    print("5. Сохранить в файл")
    print("6. Очищение всего справочника")
    print("0. Выход")
    print()


def show(happy_b):
    if len(happy_b) == 0:
        print()
        print("---  Справочник Дней Рождений пуст  ---")
    else:
        print()
        print("---  Справочник Дней Рождений   ---")
        print()
        for date in happy_b:
            value = happy_b[date]
            temp = value[0] + " " + value[1] + " " + value[2]
            print(date, ':', temp)


def input_data():
    temp = list()
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    patronymic = input("Введите отчество: ")
    temp.append(last_name)
    temp.append(first_name)
    temp.append(patronymic)
    return temp


def input_record(happy_b):
    date = input("Введите дату рождения: ")
    if date in happy_b:
        print()
        print("---  Такая запись уже сществует  ---")
    else:
        value = input_data()
        happy_b[date] = value
        print()
        print("---  Запись успешно добавлена  ---")



def edit_record(happy_b):
    date = input("Введите дату рождения: ")
    if date in happy_b:
        temp = input_data()
        happy_b[date] = temp
        print()
        print("---  Запись успешно изменена  ---")
    else:
        print()
        print("---  Вы ввели неправильную дату  ---")


def delete_record(happy_b):
    date = input("Введите дату для удаления: ")
    if date in happy_b:
        happy_b.pop(date)
        print()
        print("---  Запись " + date + " успешно удалена  ---")
    else:
        print()
        print("---  Такой записи нет в справочнике  ---")


def export_to_file(happy_b):
    with open("HappyBirthday.csv", "w") as file:
        for date in happy_b:
            value = happy_b[date]
            temp = date + ";" + value[0] + ";" + value[1] + ";" + value[2] + ";" + "\n"
            file.write(temp)


welcome()

while True:
    menu()
    choice = input("Введите режим работы: ")

    if choice == "1":
        show(happy_b)
    elif choice == "2":
        input_record(happy_b)
    elif choice == "3":
        edit_record(happy_b)
    elif choice == "4":
        delete_record(happy_b)
    elif choice == "5":
        export_to_file(happy_b)
    elif choice == "6":
        happy_b.clear()
    elif choice == "0":
        print("До свидания")
        break
    else:
        print("Неправильный режим")