import json

contact_list = {
    'Amal': 1111111111,
    'Mohammed': 2222222222,
    'Khadijah': 3333333333,
    'Abdullah': 4444444444,
    'Rawan': 5555555555,
    'Faisal': 6666666666,
    'Layla': 7777777777,
}


def add_contact(name, number):
    if number.isnumeric() and len(number) == 10:
        contact_list.update({name: int(number)})
        print("The contact has been added successfully!\n")
    else:
        print("This is invalid number\n")


def search_contact(info):
    if info.isnumeric() and len(info) == 10:
        name = [key for key, value in contact_list.items() if value == info]
        print("Found it, the {} contact name is: {}\n".format(info, name))
    elif info.isalpha():
        number = contact_list.get(info)
        print("Found it, the {}'s contact number is : {}\n".format(info, number))
    else:
        print("Sorry, the number is not found!\n")


def all_contact():
    print("Contacts: {}\n".format(json.dumps(contact_list, sort_keys=False, indent=4)))


if __name__ == '__main__':

    print("------------------------------------------\n"
          "   >>>   Welcome to contacts   <<<n")

    while True:
        print("1 -> Search\n2 -> Add\n3 -> Browse contact\n4 -> Exit\n")

        choice = int(input("Please Enter your choice: "))

        if choice in [1, 2, 3, 4]:
            if choice == 1:
                search_contact(input("Enter the info.: "))
            elif choice == 2:
                add_contact(input("Enter the name: "), input("Enter the number: "))
            elif choice == 3:
                all_contact()
            elif choice == 4:
                print(" Thank you \n"
                      ">>> Bye <<<")
                break

            start = True

            while start:

                ans = input(">>> Do you want another service? <<<\n"
                            ">>>           Y/N ? ")

                if ans in ['n', 'N', 'No', 'no', 'NO']:
                    start = False
                    print(" Thank you \n"
                          ">>> Bye <<<")
                    exit()
                elif ans in ['y', 'Y', 'Yes', 'yes', 'YES']:
                    start = False
                    continue
                else:
                    start = True
                    print("\n ... Wrong answer try again!...\n")

        else:
            print(" ... WRONG CHOICE!! Please try again!...\n")
