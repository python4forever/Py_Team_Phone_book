import view
import record
import read

data = read.get_data('dataBase.txt', '::')


def last_id():
    id_list = [int(i["id"]) for i in data if i["id"].isdigit()]
    id_list.insert(0, 0)
    return str(max(id_list) + 1)


def search_by_value(value):
    data_to_show = [i for i in data if value in i.values()]
    return data_to_show


def phone_toint_tostr(num):
    number = ''
    for i in num:
        if i.isdigit():
            number += i
    return number


def deleteit(li, dele):
    for i in range(len(li)):
        for j in li[i].values():
            if j != dele:
                li.append(j)

            else:
                print('aha delete it')
    return li


def head_logic():
    user_choice = 0
    while user_choice != 7:
        user_choice = view.options()

        if user_choice == 1:
            view.show_all_data(data)

        elif user_choice == 2:
            new_data = view.new_contact()
            new_data['id'] = last_id()
            data.append(new_data)
            record.write_data(data, 'dataBase.csv')

        elif user_choice == 3:
            li = search_by_value(view.search_contact())
            view.show_all_data(li)

        elif user_choice == 4:
            view.show_all_data(search_by_value(view.search_contact()))  # shows a list of found contacts to user
            by_number = phone_toint_tostr(view.make_achoice_from_list())  # asks a phone-num of the contact
            contact_toedit = search_by_value(by_number)


            the_key = view.edit_contact()  # returns key
            duplicate = contact_toedit[-1]
            record.remove_data(data, 'dataBase.txt', contact_toedit[-1]['phone'])
            duplicate[the_key] = view.edit_to_val()
            data.append(duplicate)
            # record.write_data(data, 'database.csv')
            print('Changes are saved!')

        elif user_choice == 5:
            view.show_all_data(search_by_value(view.search_contact()))  # shows a list of found contacts to user
            by_number = phone_toint_tostr(view.make_achoice_from_list())  # asks a phone-num of the contact
            contact_toremove = search_by_value(by_number)
            record.remove_data(data, 'dataBase.csv', contact_toremove[-1]['phone'])

        elif user_choice == 6:
            a = view.import_export()
            digit = a[0]
            file_name = a[1] + '.txt'

            if digit == 1:
                record.write_data_exp(data, file_name)
                print(f'{file_name} is ready for export! \n')
            if digit == 2:
                read.get_data("dataBase.csv", ';')
                print('Done!')


