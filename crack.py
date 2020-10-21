password = "UdymtsnxAjwdJfXd"
limit = 5

for i in range(len(password)):
    print("-----")
    for j in range(127):
        kar = chr(j)
        if (kar.isupper()):
            result = chr((ord(kar) + limit - 65) % 26 + 65)
        else:
            result = chr((ord(kar) + limit - 97) % 26 + 97)

        print(kar + " " + result)