database = {}
user_name = 'Username '
#checks if username is in dattabase
def check_user(user):
    return user in database.keys()
#for login
def login():
    user = input(user_name)
    if not check_user(user):
        return 0
    password = input("Password: ")
    if password == database[user]["password"]:
        return user
    else:
        return -1
#for register
def register():
    user = input(user_name)
    if check_user(user):
        return -1
    password = input("New Password: ")
    secret = input("Now enter your secrete phrase for safekeeping: ")
    database[user] = {"password": password, "secret": secret}
    return 1
def choice():
    print("\nWhat would you like to do?")
    print("1)register ")
    print("2) login")
    print("3) Exit\n")
    v = int(input("> "))
    print("")
    return v
while True: #loop runs forever till break
    answer = choice()
    match answer:
        case 1:

            username= register()
            if username == 0:
                print("error: username not found")
            elif username == -1:
                print("error: incorrect password")
            else:
                print(f"\nWelcome back, {username}!")
                print("Your secret phrase is:")
                print(database[username],"secret")
            continue
        case 2:
            username=login()
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