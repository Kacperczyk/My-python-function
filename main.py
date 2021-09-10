import csv
import linecache
import os

def dictionary_file_reader_choosen_field(path, first_line, last_line):
    with open(path, 'r', newline='', encoding='utf-8') as f:

        fieldnames_field = [f.readline().strip() for x in range(1)]
        for i in range(len(fieldnames_field)):
            fieldnames = fieldnames_field[i].split(';')

        user_choice = ''
        user_choice_of_field = []
        while True:
            if len(user_choice_of_field) == len(fieldnames):
                break
            elif len(user_choice_of_field) < len(fieldnames):
                user_choice = (input(f'List of file fieldnames: {fieldnames} choose which you want to read / or stop : '))
                if user_choice in fieldnames:
                    if user_choice_of_field.count(user_choice) == 0:
                        user_choice_of_field.append(user_choice)
                    else:
                        print('You cannot add the same fieldname twice!')
                elif user_choice not in fieldnames:
                    if user_choice == 'stop':
                        break
                    else:
                        print('Please choose correct fieldname!')

        reader_linecacher = [linecache.getline(path, x).strip() for x in range(first_line, last_line + 1)]
        reader2 = csv.DictReader(reader_linecacher, delimiter=';', fieldnames=fieldnames)
        for row in reader2:
            for column_name in user_choice_of_field:
                print(row[column_name], end=' ')
            print('\n', end='')

    path_of_new_file = r'C:\PyCharm\PythonProject\SeleniumPython'
    if not os.path.exists(path):
        os.makedirs(path)

    request = input('Do you want save choosen lines in file?: ')
    if request == 'yes' or request == 'y':
        new_file_name = input('New csv file name: ')
        with open(os.path.join(path_of_new_file, new_file_name+'.csv'), 'a', newline='', encoding='utf=8')as nf1:
            nf1_fieldnames = [x for x in user_choice_of_field]
            nf1_writer = csv.DictWriter(nf1, delimiter=';', fieldnames=nf1_fieldnames)
            reader_linecacher = [linecache.getline(path, x).strip() for x in range(first_line, last_line + 1)]
            reader2 = csv.DictReader(reader_linecacher, delimiter=';', fieldnames=fieldnames)
            for row in reader2:
                for column_name in user_choice_of_field:
                    nf1_writer.writerow({column_name: row[column_name]})
                    print(row[column_name], end=' ')

dictionary_file_reader_choosen_field(r'C:\PyCharm\PythonProject\SeleniumPython\newfile1.csv', 3, 6)