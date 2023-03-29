from tabulate import tabulate
import emoji

def options():
    print(emoji.emojize("\nChoose one of the options bellow: "
          "\n:page_with_curl: Type 1 to see all contacts "
          "\n:plus: Type 2 to add a new contact "
          "\n:magnifying_glass_tilted_right: Type 3 to search a contact "
          "\n:pen: Type 4 to edit a contact "
          "\n:cross_mark: Type 5 to delete a contact "
          "\n:counterclockwise_arrows_button: Type 6 to import/ export "
          "\n:bomb: Type 7 to close the programm \n", language='en'))
    num = int(input('Input here: '))
    if 0 < num < 8:
        return num
    else:
        print(emoji.emojize(':red_exclamation_mark:Incorrect number!', language='en'))


def new_contact():
    contact = {'id': '', 'surname': input('Input surname or press "Enter": '), 'name': input('Input name: ')}
    while contact['name'] == '':
        contact['name'] = input('Input name: ')
    contact['patronymic'] = input('Input patronymic or press "Enter": ')
    contact['phone'] = input('Input phone number: ')
    while contact['phone'] == '':
        contact['phone'] = input('Input phone number: ')
    contact['comment'] = input('Type a comment or press "Enter": ') + '\n'
    return contact


def search_contact():
    print('You can search a contact by surname, name, patronymic, comment')
    search_by = input('Input here: ')
    return search_by


def make_achoice_from_list():
    contact_number = input("Input the contact's phone number You want to edit/ delete: ")
    return contact_number


def edit_contact():
    edit_the = int(input('Input 1 to change the surname \nInput 2 to change the name \nInput 3 to change the patronymic'
                         '\nInput 4 to change the phone number \n Input 5 to change the comment: '))
    while 0 > edit_the > 5:
        edit_the = int(
            input('Input 1 to change the surname \nInput 2 to change the name \nInput 3 to change the patronymic'
                  '\nInput 4 to change the phone number \n Input 5 to change the comment: '))

    if edit_the == 1:
        edit_the = 'surname'
    if edit_the == 2:
        edit_the = 'name'
    if edit_the == 3:
        edit_the = 'patronymic'
    if edit_the == 4:
        edit_the = 'phone'
    if edit_the == 5:
        edit_the = 'comment'

    return edit_the


def edit_to_val():
    edit_to = input('Input the value to overwrite the current value:')
    return edit_to


def import_export():
    exp_imp_answer = int(input("Do you want to Export file or Import file: \n"
                               "1. Export file\n"
                               "2. Import file\n"))

    if exp_imp_answer in [1, 2]:
        file_name = input("Enter the name of the file: ")
        return exp_imp_answer, file_name
    else:
        print('Wrong number')
        return 0, ""


def show_all_data(data):
    data_to_show = []

    for i in range(len(data)):
        li = list(data[i].values())
        li.pop(0)
        data_to_show.append(li)

    params = ['Surname', 'name', 'Patronymic', 'Phone number', 'Comment']

    print(tabulate(data_to_show, headers=params, tablefmt="fancy_grid", showindex="never"))
