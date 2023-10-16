import getpass


def main():
    def user_registration():
        with open('password_list.txt', 'r') as password_file:
            master_password = password_file.readline().strip()

        if master_password == '':
            # one time thing
            master_password = input('Make a new master password: ')
            with open('password_list.txt', 'w') as password_file:
                password_file.write((master_password + '\n'))
            menu()
        else:
            check_password = input('Enter your master password: ')
            check_password_fun(check_password)

    def check_password_fun(password):
        with open('password_list.txt', 'r') as password_file:
            master_password = password_file.readline().strip()
        if master_password == password:
            menu()
        else:
            print('Wrong password!')
            check_password = input('Try again: ')
            check_password_fun(check_password)

    def menu():
        input_number = input('''
-----------------------------------MENU------------------------------------------
| Type (\'1\') Add a new password entry (e.g., for websites, apps, or accounts).  |
| Type (\'2\') View stored passwords.                                             |
| Type (\'3\') Search for a specific password entry.                              |
| Type (\'4\') Update existing password entries.                                  |
| Type (\'5\') Delete password entries.                                           |
| Type (\'6\') Change the master password.                                        |
| Type (\'7\') Exit the application.                                              |
---------------------------------------------------------------------------------
''')
        if input_number == '1':
            new_password()
        elif input_number == '2':
            stored_passwords_fun()
        elif input_number == '3':
            search_for_password()
            menu()
        elif input_number == '4':
            update_password()
        elif input_number == '5':
            delete_password()
        elif input_number == '6':
            old_master = input('''Enter your old password: 
''')
            with open('password_list.txt', 'r') as password_file:
                master_password = password_file.readline().strip()
            if old_master == master_password:
                change_master()
            else:
                print("Wrong password, try again!")
                menu()
        elif input_number == '7':
            quit()
        else:
            wrong_input()

    def new_password():
        site = input('Input site name for your login: ')
        name = input('Input username: ')
        password = input('Input password: ')

        x = (f'''---------------------------
{site}
{name}
{password}
''')
        with open('password_list.txt', 'a') as password_file:
            password_file.write(x)
        menu()

    def stored_passwords_fun():
        with open('password_list.txt', 'r') as password_file:
            password_file.readline()
            for line in password_file:
                print(line.strip())
        menu()

    def search_for_password():
        input_text = input('Search for your login information by site, program or app on which you use it: \n')
        pass_list = []
        with open('password_list.txt', 'r') as password_file:
            for line in password_file:
                pass_list.append(line.strip())
        if input_text not in pass_list:
            wrong_input()
        else:
            login = pass_list.index(input_text)
            print(f'''
Site/app/program:      {pass_list[login]}
Login/e-mail/username: {pass_list[login + 1]}
Password:              {pass_list[login + 2]}''')
            return login

    def update_password():
        login = search_for_password()
        pass_list = []
        with open('password_list.txt', 'r') as password_file:
            for line in password_file:
                pass_list.append(line.strip())
        update_choice = input("""What do you want to update?
Site/app/program name - ('1')
Login/e-mail/username - ('2')
Password              - ('3')
""")
        if update_choice == "1":
            new_input = input("Input new site/app/program name: ")
            pass_list[login] = new_input

        elif update_choice == "2":
            new_input = input("Input new login/e-mail/username: ")
            pass_list[login+1] = new_input

        elif update_choice == "3":
            new_input = input("Input new password: ")
            pass_list[login+2] = new_input
        else:
            wrong_input()

        pass_list_string = ""
        for i in pass_list:
            pass_list_string += i + "\n"
        with open('password_list.txt', 'w') as password_file:
            password_file.write(pass_list_string)
        menu()


    def delete_password():
        login = search_for_password()
        confirmation = input('''
This entry will be deleted, are you sure?
(\'1\')Yes      (\'2\')No
''')
        if confirmation == '1':
            pass_list = []
            with open('password_list.txt', 'r') as password_file:
                for line in password_file:
                    pass_list.append(line.strip())
            del pass_list[login - 1:login + 3]
            pass_list_string = ""
            for i in pass_list:
                pass_list_string += i + "\n"
            with open('password_list.txt', 'w') as password_file:
                password_file.write(pass_list_string)
            menu()
        elif confirmation == "2":
            menu()
        else:
            wrong_input()

    def change_master():
        with open('password_list.txt', 'r') as password_file:
            master_password = password_file.readlines()

        new_list = []

        for i in master_password:
            new_list.append(i)

        new_master_password = input('''Input new master password: 
''')
        new_list[0] = (new_master_password + '\n')
        string = ''
        for a in new_list:
            string += a

        with open('password_list.txt', 'w') as password_file:
            password_file.write(string)
        menu()

    def wrong_input():
        option = input('''
        Wrong input!
Do you want to choose again?
(\'1\')Yes      (\'2\')No
''')
        if option == '1':
            menu()
        else:
            quit()

    user_registration()


if __name__ == '__main__':
    main()
