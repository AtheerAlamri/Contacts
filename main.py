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
        print("\033[32mThe contact has been added successfully!\033[00m\n")
    else:
        print("\033[91mThis is invalid number\033[00m\n")


def search_contact(info):
    if info.isnumeric() and len(info) == 10:
        name = [key for key, value in contact_list.items() if value == info]
        print("\033[32mFound it, the {} contact name is: {}\033[00m\n".format(info, name))
    elif info.isalpha():
        number = contact_list.get(info)
        print("\033[32mFound it, the {}'s contact number is : {}\033[00m\n".format(info, number))
    else:
        print("\033[91mSorry, the number is not found!\033[00m\n")


def all_contact():
    print("\033[32mContacts: {}\033[00m\n".format(json.dumps(contact_list, sort_keys=False, indent=4)))


if __name__ == '__main__':

    print("\033[93m------------------------------------------\n"
          "   >>>   Welcome to contacts   <<<\033[00m\n")

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
                print("\n\033[93m Thank you \n"
                      "\033[01m>>> Bye <<<\033[00m")
                break

            start = True

            while start:

                ans = input("\033[34m>>> Do you want another service? <<<\n"
                            ">>>           Y/N ? \033[00m")

                if ans in ['n', 'N', 'No', 'no', 'NO']:
                    start = False
                    print("\n\033[93m Thank you \n"
                          "\033[01m>>> Bye <<<\033[00m")
                    exit()
                elif ans in ['y', 'Y', 'Yes', 'yes', 'YES']:
                    start = False
                    continue
                else:
                    start = True
                    print("\n\033[91m ... Wrong answer try again!...\033[00m\n")

        else:
            print("\n\033[91m ... WRONG CHOICE!! Please try again!...\033[00m\n")
