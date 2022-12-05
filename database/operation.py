import export_data as exp
import import_data as imp
import view
import logger as log

def button_click():
    choise = view.button()
    while choise != 'q':
        log.log_info(choise)
        if choise == '1':
            exp.export_data()
        elif choise == '2':
            what_find = input('Для поиска по фамилии введите - 1 \nДля поиска по идентификатору введите - 2 \nДля поиска по должности введите - 3 \n')
            if what_find == '1': 
                imp.find_surname(input('Введите фамилию: '))
            if what_find == '2': 
                imp.find_identity(input('Введите идентификатор: '))
            if what_find == '3': 
                imp.find_post(input('Введите должность: '))
        choise = view.button()