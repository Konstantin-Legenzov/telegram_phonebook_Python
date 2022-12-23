from userInterface import get_info


def creating ():
    file = 'Phonebook.csv'
    with open (file, 'w', encoding = 'utf-8') as data:
        data.write(f'Фамилия|Имя|Номер телефона|Описание\n')

def changer ():
    global info
    file = 'Phonebook.csv'
    with open (file, 'a', encoding = 'utf-8') as data:
        data.write(f'{info[0]}|{info[1]}|{info[2]}|{info[3]}\n')
