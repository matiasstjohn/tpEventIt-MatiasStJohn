from Classes.event import requestEvent
from csv import writer
from Menu.homeadmins import InterfazAdmin


class InterfazUser:
    @property
    def currentUser(self):
        with open('..\\Datasets\\CurrentUser.csv', 'r', newline='') as user:
            for line in user:
                row = line.strip().split(",")
                usuario = row[2]
                return usuario

    @property
    def currentCuil(self):
        with open('..\\Datasets\\CurrentUser.csv', 'r', newline='') as user:
            for line in user:
                row = line.strip().split(",")
                usuario = row[0]
                return str(usuario)

    def contactoDeInteres(self):
        try:
            other_user = input("Escribir el CUIL o celular del que quieras agregar como amigo: ")
            found = False
            with open('..\\Datasets\\User_database.csv', 'r', newline='') as user_database:
                for line in user_database:
                    row = line.strip().split(",")
                    if row[0] == other_user or row[1] == other_user:
                        found = True
                        with open(f'..\\Users\\{row[0]}.csv', 'r', newline='') as user_data:
                            copied_data = list()
                            for line in user_data:
                                row2 = line.strip().split(',')
                                if row2[0] == 'Requests':
                                    row2.append(str(self.currentCuil))
                                copied_data.append(row2)
                        with open(f'..\\Users\\{row[0]}.csv', 'w', newline='') as user_data:
                            data_writer = writer(user_data, lineterminator='\r')
                            for data in copied_data:
                                data_writer.writerow(data)
            if found:
                pass
            else:
                raise ValueError
        except ValueError:
            print("Usuario no encontrado: ")

    def check_requests(self):
        with open('..\\Datasets\\CurrentUser.csv', 'r', newline='') as user_data:
            i = 0
            for line in user_data:
                row = line.strip().split(",")
                if i == 2:
                    count = 1
                    while count < len(row):
                        print(row[count])
                        try:
                            action = input("Desea aceptar la solicitud (Y/N): ")
                            if action.lower() == "n":
                                with open('..\\Datasets\\CurrentUser.csv', 'r', newline='') as current_user:
                                    copied_data = list()
                                    for line in current_user:
                                        row2 = line.strip().split(',')
                                        if row2[0] == 'Requests':
                                            row_index = row2.index(row[count])
                                            del row2[row_index]
                                        copied_data.append(row2)
                                with open(f'..\\Users\\{str(row[count])}.csv', 'r', newline='') as rejected_user:
                                    rejected_data = list()
                                    for line in rejected_user:
                                        row3 = line.strip().split(',')
                                        if row3[0] == str(row[count]):
                                            attempts = int(row3[5])
                                            attempts += 1
                                            row3[5] = str(attempts)
                                            if attempts >= 5:
                                                row3[4] == 'Blocked'
                                                InterfazAdmin.auto_BlockUser(self, row3[0])
                                        rejected_data.append(row3)
                                with open('..\\Datasets\\CurrentUser.csv', 'w', newline='') as current_user:
                                    data_writer = writer(current_user, lineterminator='\r')
                                    for data in copied_data:
                                        data_writer.writerow(data)
                                with open(f'..\\Users\\{str(self.currentCuil)}.csv', 'w', newline='') as current_user:
                                    data_writer = writer(current_user, lineterminator='\r')
                                    for data in copied_data:
                                        data_writer.writerow(data)
                                with open(f'..\\Users\\{str(row[count])}.csv', 'w', newline='') as rejected_user:
                                    data_writer = writer(rejected_user, lineterminator='\r')
                                    for data in rejected_data:
                                        data_writer.writerow(data)
                                count += 1
                            elif action.lower() == "y":
                                with open('..\\Datasets\\CurrentUser.csv', 'r', newline='') as current_user:
                                    copied_data = list()
                                    for line in current_user:
                                        row2 = line.strip().split(',')
                                        if row2[0] == 'Friends':
                                            row2.append(row[count])
                                        elif row2[0] == 'Requests':
                                            row_index = row2.index(row[count])
                                            del row2[row_index]
                                        copied_data.append(row2)
                                with open('..\\Datasets\\CurrentUser.csv', 'w', newline='') as current_user:
                                    data_writer = writer(current_user, lineterminator='\r')
                                    for data in copied_data:
                                        data_writer.writerow(data)
                                with open(f'..\\Users\\{str(self.currentCuil)}.csv', 'w', newline='') as current_user:
                                    data_writer = writer(current_user, lineterminator='\r')
                                    for data in copied_data:
                                        data_writer.writerow(data)
                                with open(f'..\\Users\\{row[count]}.csv', 'r', newline='') as accepted_user:
                                    data_copy = list()
                                    for line in accepted_user:
                                        row3 = line.strip().split(',')
                                        if row3[0] == 'Friends':
                                            row3.append(str(self.currentCuil))
                                        data_copy.append(row3)
                                with open(f'..\\Users\\{row[count]}.csv', 'w', newline='') as accepted_user:
                                    data_writer = writer(accepted_user, lineterminator='\r')
                                    for data in data_copy:
                                        data_writer.writerow(data)
                                count += 1
                            else:
                                raise ValueError
                        except ValueError:
                            print("wrong input, try again")
                i += 1

    def reportEvent(self):
        return requestEvent()


intUser = InterfazUser()
