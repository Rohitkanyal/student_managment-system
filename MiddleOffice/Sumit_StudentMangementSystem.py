def add():
    name = input("Enter Name :- ")
    age = int(input("Enter Age :- "))
    phone_number = int(input("Enter Phone Number :-"))

    print("New Student is added")


def delete():
    name = input("Enter Name of Student:- ")
    print("Delete Student")


def search():
    name = input("Enter Name of Student:- ")
    print("It should display student Name", name)


def header():
    print('''********* \nWainganga \n***********''')


def choice():
    print(''' 1.Add New Student\n 2.Delete Student\n 3.Search Student''')
    choice = int(input("Enter You choice :- "))
    return choice


if __name__ == "__main__":
    cho = choice()
    if cho == 1:
        header()
        add()
    elif cho == 2:
        header()
        delete()
    elif cho == 3:
        header()
        search()
    else:
        print("Invalid Choice")
