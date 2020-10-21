# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Class:
    username = [int(325 / 5), (60 + 40), 109, 49, (100 + 6 + 4)]
    password = "UdymtslnxAjwdJfXd"
    limit = 5
    sukses = False

    def __init__(self):
        print('=' * 30)
        print("        Silahkan Masuk")
        print('=' * 30)

    def login(self, username, password):
        if ((self.CheckUser(username) == 0) and (self.CheckPass(password) is False)):
            self.sukses = True
        return self.sukses

    def convert(self, param):
        result = ""
        for i in range(len(param)):
            if (param[i].isupper()):
                result += chr((ord(param[i]) + self.limit - 65) % 26 + 65)
            else:
                result += chr((ord(param[i]) + self.limit - 97) % 26 + 97)
        return result

    def CheckUser(self, username):
        if len(username) == self.limit:
            for i in range(self.limit):
                if (ord(username[i]) == self.username[i]):
                    self.limit -= 1
        return self.limit

    def CheckPass(self, password):
        error = True
        if (len(password) == len(self.password)):
            error = False
            if (password[0].isupper() is True):
                error = False
                if (ord(password[6]) == 51):
                    error = False
                    if (isinstance(int(password[(11 - 5):7]), int) is True):
                        error = False
                        if (self.password == self.convert(password)):
                            error = False

        return error


chall = Class()
if __name__ == '__main__':
    username = input("Username : ")
    password = input("Password : ")
    login = chall.login(username, password)
    if login is True:
        print('=' * 30)
        print("Sukses masuk\nSelamat datang", username)
    else:
        print("Gagal masuk!")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
