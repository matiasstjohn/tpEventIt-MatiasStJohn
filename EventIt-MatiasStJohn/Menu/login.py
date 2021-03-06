from csv import writer
from Classes.users import Citizen
from Classes.map import seleccionarZona
from Menu.menuadmin import menu_admin
from Menu.homeadmins import intAdmin
from Classes.event import seleccionarTiposEvent
from Classes.sensor import Sensor
from Menu.menusensor import senMenu
from Menu.menuusers import menu_user


class Start:

    def Register(self):
        cuil = Start.checkCuil(self)
        phone_number = Start.checkPhoneNumber(self)
        username = Start.checkUsername(self)
        password = Start.checkPassword(self)
        with open('..\\Datasets\\User_database.csv', 'a', newline='') as user_database:
            user = Citizen(username, password, cuil, phone_number)
            user_data = [cuil, phone_number, user.username, user.password, 'Unblocked', '0']
            data_writer = writer(user_database, lineterminator='\r')
            data_writer.writerow(user_data)
        with open(f'..\\Users\\{cuil}.csv', 'w', newline='') as user_csv:
            user_writer = writer(user_csv, lineterminator='\r')
            user_writer.writerow(user_data)
            friend_list = ['Friends']
            user_writer.writerow(friend_list)
            requests = ['Requests']
            user_writer.writerow(requests)

    def checkCuil(self):
        check = False
        while check == False:
            cuil = input('Please enter your CUIL: ')
            anses_check = Start.checkCuilDatabase(self, cuil)
            if anses_check:
                try:
                    with open('..\\Datasets\\User_database.csv', 'r') as user_database:
                        for i in user_database:
                            row = i.strip().split(',')
                            if cuil == row[0]:
                                print("Cuil already exist, try another one")
                                raise ValueError
                    check = True
                    return cuil

                except ValueError:
                    pass
            else:
                print('Please enter  a valid CUIL.')

    def checkCuilDatabase(self, cuil):
        valid_cuil = False
        with open('..\\Datasets\\Anses_dataset.csv', 'r') as anses_database:
            for line in anses_database:
                row = line.strip().split(',')
                if cuil == row[0]:
                    valid_cuil = True
        return valid_cuil

    def checkPhoneNumber(self):
        check = False
        while check == False:
            try:
                with open('..\\Datasets\\User_database.csv', 'r') as user_database:
                    phone_number = input('Please enter your phone number: ')
                    for line in user_database:
                        row = line.strip().split(',')
                        if phone_number == row[1].strip():
                            print("phone number already exist, try another one")
                            raise ValueError
                        else:
                            check = True
                            return phone_number
                    return phone_number
            except ValueError:
                pass

    def checkUsername(self):
        check = False
        while check == False:
            try:
                with open('..\\Datasets\\User_database.csv', 'r') as user_database:
                    username = input('Enter your username: ')
                    for line in user_database:
                        row = line.strip().split(',')
                        if username == row[2].strip():
                            print("Username already exist, try another one")
                            raise ValueError
                        else:
                            check = True
                            return username
                    return username
            except ValueError:
                pass

    def checkPassword(self):
        check = False
        while check == False:
            password = input('Enter your password: ')
            confirm_password = input('Please re-enter your password:')
            if password != confirm_password:
                print('Passwords do not match, please try again.')
                Start.checkPassword(self)
            else:
                check = True
                return password

    def Login(self):
        log = False
        while not log:
            username = input('Enter Username: ').rstrip()
            password = input('Enter Password: ')
            with open('..\\Datasets\\User_database.csv', 'r') as database:
                try:
                    for line in database:
                        row = line.strip().split(',')
                        if username == row[2].strip():
                            if not intAdmin.checkIfBlocked(username):
                                if password == row[3].strip():
                                    cuil = row[0]
                                    with open(f'..\\Users\\{cuil}.csv', 'r') as user_data:
                                        copied_data = list()
                                        for line in user_data:
                                            row2 = line.strip().split(',')
                                            if row2[0] == cuil:
                                                row2 = row
                                            copied_data.append(row2)
                                            with open('..\\Datasets\\CurrentUser.csv', 'w') as user:
                                                data_writer = writer(user, lineterminator='\r')
                                                for data in copied_data:
                                                    data_writer.writerow(data)
                                    log = True
                                    menu_user.User_mainMenu()
                            else:
                                print('This user is blocked. Please reach an administrator.')
                                log = True

                    if not log:
                        raise ValueError
                except ValueError:
                    print('Username and password do not match. Please try again.')

    def LoginAdmin(self):
        log = False
        while not log:
            username = input('Enter username: ').rstrip()
            password = input('Enter password: ')
            with open('..\\Datasets\\Admin_dataset.csv', 'r') as database:
                try:
                    for line in database:
                        row = line.strip().split(',')
                        if username == row[0].strip():
                            if password == row[1].strip():
                                menu_admin.Admin_mainMenu()
                                log = True
                    if not log:
                        raise ValueError
                except ValueError:
                    print('Username and password do not match. Please try again.')

    def LoginSensor(self):
        tipo = seleccionarTiposEvent()
        zona = seleccionarZona()
        sensor = Sensor.createSensor(tipo, zona)
        return senMenu.sensor_mainMenu(sensor)


menuLogin = Start()
