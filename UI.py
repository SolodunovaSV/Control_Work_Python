
import File_operation as f



def menu():
    menu = None
    print("\nДобро пожаловать в программу 'Заметки'!. Вам доступны следующие функции:\n\n1 - Чтение списка заметок\n2 - Создание заметки\n3 - Удаление заметки\n4 - Редактирование заметки\n5 - Выбор заметок по дате создания/редактирования\n6 - Выбор заметки по ID\n7 - Выход\n")
    menu = input('Введите номер функции: ')
    while menu not in ('1', '2', '3', '4', '5', '6', '7'):
        print('Некорректный ввод')
        menu = input('Введите номер функции: ')
    match menu:
            case '1':
                f.show_note('all')
            case '2':
                f.add_note()
            case '3':
                f.show_note('all')
                f.id_edit_del_show('del')
            case '4':
                f.show_note('all')
                f.id_edit_del_show('edit')
            case '5':
                f.show_note('date')
            case '6':
                f.show_note('id')
                f.id_edit_del_show('show')
            case '7':
                print("До свидания!")
               


