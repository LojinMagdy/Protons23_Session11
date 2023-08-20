# simple login system with dictionary

database = {}
constantMessage1 = 'Username  '#i wanted to use a constant but had no idea what to do
#checks if username is in dattabase
def checkingCaseOfUserNameInDataBase(x):
    return x in database.keys()
#for login
def fun1():
    x = input(constantMessage1)
    if not checkingCaseOfUserNameInDataBase(x):
        return 0
    y = input("Password: ")
    if y == database[x]["password"]:
        return x
    else:
        return -1
#for register
def register():
    x = input(constantMessage1)
    if checkingCaseOfUserNameInDataBase(x):
        return -1
    y = input("New Password: ")
    z = input("Now enter your secrete phrase for safekeeping: ")
    database[x] = {"password": y, "secret": z}
    return 1
def choice():
    print("\nWhat would you like to do?")
    print("1) ")
    print("2) ")
    print("3) Exit\n")
    answer = int(input("> "))
    print("")
    return answer
while True: #loop runs forever till break
    answer = choice()
    match answer:
        case 1:

            username = register()
            if username == 0:
                print("error: username not found")
            elif username == -1:
                print("error: incorrect password")
            else:
                print(f"\nWelcome back, {username}!")
                print("Your secret phrase is:")
                print(database["username"]["secret"])
            continue
        case 2:
            username=fun1()
            if username == 1:
                print("\nSuccessfuly Registered!")
            elif username==-1:
                print("error: username already exists")
            continue
        case 3:
            print("Thank You")
            break
        case _:
            print("error: invalid input")
