import csv
import os
print("Бар МОНОБРОВЬ")
print("Добрый вечер, Дорогой Гость! Приветствуем тебя в нашем баре МОНОБРОВЬ!")
print("Для начало давайте познакомимся")
name = input("Введите свое имя: ")
age = int(input("Введите свой возраст: "))
if age >= 18:
    print(f"{name}, предлагаем пройти несколько тестов, чтобы мы создали для Вас идеальный вечер!")
    os.chdir('test')
    list_itogov_nap = []
    list_itogov_food = []
    list_itogov_place = []
    while True:
        print("Список тестов")
        os.chdir('../')
        os.chdir('test')
        names_test = os.listdir(path=".")
        list_name_test = []
        for i in names_test:
            with open(f'{i}', newline='', encoding='utf-8') as f:
                reader = csv.reader(f)
                row1 = next(reader)
                list_name_test.append(row1[0])
        print(*list_name_test, sep='\n')
        name_test = input("Выберите тест - ")
        match name_test:
            case "1":
                bal = 0
                with open('test1.csv', newline='', encoding='utf-8') as csvfile:
                    data = csv.reader(csvfile, delimiter=',')
                    f = 0
                    for row in data:
                        if len(row) > 1:
                            print(row[0])
                            print(*row[1:], sep='\n')
                            answer = int(input("Ответ - "))
                            os.chdir('../otvet')
                            with open('otvet1.csv', newline='', encoding='utf-8') as csvfileotv:
                                f += 1
                                data1 = csv.reader(csvfileotv)
                                row_list = [row for row in data1]
                                bal += int(row_list[f][answer-1])
                if bal == 106:
                    list_itogov_nap.append('B52')
                elif bal == 107:
                    list_itogov_nap.append('Глинтвейн')
                elif bal == 108:
                    list_itogov_nap.append('Айриш кофе')
                elif bal == 111:
                    list_itogov_nap.append('Белый русский')
                elif bal == 112:
                    list_itogov_nap.append('Виски сауэр')
                elif bal == 113:
                    list_itogov_nap.append('Негрони')
                elif bal == 16:
                    list_itogov_nap.append('Венский кофе')
                elif bal == 17:
                    list_itogov_nap.append('Безалкогольный глинтвейн')
                elif bal == 18:
                    list_itogov_nap.append('Чай')
                elif bal == 21:
                    list_itogov_nap.append('Милкшейк')
                elif bal == 22:
                    list_itogov_nap.append('Лимонад')
                elif bal == 23:
                    list_itogov_nap.append('Вода')
            case "2":
                bal = 0
                with open('test2.csv', newline='', encoding='utf-8') as csvfile:
                    data = csv.reader(csvfile, delimiter=',')
                    f = 0
                    for row in data:
                        if len(row) > 1:
                            print(row[0])
                            print(*row[1:], sep='\n')
                            answer = int(input("Ответ - "))
                            os.chdir('../otvet')
                            with open('otvet2.csv', newline='', encoding='utf-8') as csvfileotv:
                                f += 1
                                data1 = csv.reader(csvfileotv)
                                row_list = [row for row in data1]
                                bal += int(row_list[f][answer - 1])
                if bal == 11:
                    list_itogov_food.append('Кимчи')
                elif bal == 12:
                    list_itogov_food.append('Китайские пельмени')
                elif bal == 13:
                    list_itogov_food.append('Пахлава')
                elif bal == 21:
                    list_itogov_food.append('Ассорти брускетт')
                elif bal == 22:
                    list_itogov_food.append('Паста с морепродуктами в томатном соусе')
                elif bal == 23:
                    list_itogov_food.append('Тирамису')
                elif bal == 31:
                    list_itogov_food.append('Салат "Сельдь под шубой"')
                elif bal == 32:
                    list_itogov_food.append('Драники со сметаной')
                elif bal == 33:
                    list_itogov_food.append('Сливовое варенье с грецкими орехами и бренди')
            case "3":
                list_itogov_place = []
                bal = 0
                with open('test3.csv', newline='', encoding='utf-8') as csvfile:
                    data = csv.reader(csvfile, delimiter=',')
                    f = 0
                    for row in data:
                        if len(row) > 1:
                            print(row[0])
                            print(*row[1:], sep='\n')
                            answer = int(input("Ответ - "))
                            os.chdir('../otvet')
                            with open('otvet3.csv', newline='', encoding='utf-8') as csvfileotv:
                                f += 1
                                data1 = csv.reader(csvfileotv)
                                row_list = [row for row in data1]
                                bal += int(row_list[f][answer - 1])
                if bal == 16:
                    list_itogov_place.append('Вам подготовлено вип место в зале для курящих')
                elif bal == 17:
                    list_itogov_place.append('Пройдите в общий зал для курящих')
                elif bal == 21:
                    list_itogov_place.append('Вам подготовлено вип место в зале для некурящих')
                elif bal == 22:
                    list_itogov_place.append('Пройдите в общий зал для некурящих')
                elif bal == 56:
                    list_itogov_place.append('Вам с компанией подготовлено вип место зале для курящих')
                elif bal == 57:
                    list_itogov_place.append('Пройдите с компанией в общий зал для курящих')
                elif bal == 61:
                    list_itogov_place.append('Вам подготовлено вип место в зале для курящих')
                elif bal == 62:
                    list_itogov_place.append('Пройдите с компанией в общий зал для некурящих')
            case _:
                print("Вы ввели неправильный номер вопроса!")
        off = input('Вернуться в меню со списком тестов? 1. Да  2. Нет   ')
        if off == '1':
            continue
        elif off == '2':
            if list_itogov_nap != [] and list_itogov_food != [] and list_itogov_place != []:
                break
            elif list_itogov_nap == [] and list_itogov_food == [] and list_itogov_place == []:
                print("Вы прошли не все тесты. Пройдите 1,2,3 тесты")
                continue
            elif list_itogov_nap == [] and list_itogov_food != [] and list_itogov_place != []:
                print("Вы прошли не все тесты. Пройдите 1 тест")
                continue
            elif list_itogov_nap != [] and list_itogov_food == [] and list_itogov_place != []:
                print("Вы прошли не все тесты. Пройдите 2 тест")
                continue
            elif list_itogov_nap != [] and list_itogov_food != [] and list_itogov_place == []:
                print("Вы прошли не все тесты. Пройдите 3 тест")
                continue
            elif list_itogov_nap == [] and list_itogov_food == [] and list_itogov_place != []:
                print("Вы прошли не все тесты. Пройдите 1 и 2 тесты")
                continue
            elif list_itogov_nap == [] and list_itogov_food != [] and list_itogov_place == []:
                print("Вы прошли не все тесты. Пройдите 1 и 3 тесты")
                continue
            elif list_itogov_nap != [] and list_itogov_food == [] and list_itogov_place == []:
                print("Вы прошли не все тесты. Пройдите 2 и 3 тесты")
                continue
    print(f"{name}, Ваш идеальный вечер:")
    print(*list_itogov_place)
    print("Напитки, подобранные под Ваши предпочтения:")
    print(*list_itogov_nap, sep="\n")
    print("Блюда, подобранные под Ваши предпочтения:")
    print(*list_itogov_food, sep="\n")
    print("Хорошего Вам времениприпровождения в нашем баре!")
    StrA = ", ".join(list_itogov_place)
    StrB = ", ".join(list_itogov_nap)
    StrC = ", ".join(list_itogov_food)
    data = [f"Имя: {name}",
            f'Место: {StrA}',
            f'Напитки: {StrB}',
            f'Блюда: {StrC}']
    os.chdir("../")
    with open('answ_user.txt', mode='a', encoding='utf-8') as file1:
        for line in data:
            file1.write(line+'\n')
else:
    print("Извините, наш бар строго 18+, приходите, когда повзрослеете! До скорых встреч")