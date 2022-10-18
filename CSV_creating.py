def creating():
    file = 'Phone_book.csv'
    with open(file, 'w', encoding='utf-8') as data:
        data.write(f'Фамилия;Имя;Номер телефона;Описание\n')
