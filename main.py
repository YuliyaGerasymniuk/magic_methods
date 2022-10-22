from classes import *


def input_error(func):
    def wrapper(*args):
        try:
            return func(*args)
        except (KeyError, ValueError, IndexError):
            return 'Wrong input, try one more time'

    return wrapper


def hello():
    return "How can I help you?"


@input_error
def add(*args):
    name = Name(args[0][0])
    phone = Phone(args[0][1])

    birthday = Birthday(args[0][2])
    if name.value in address_book.data.keys():
        address_book.data[name.value].add_phone(phone)
    else:
        record = Record(name, phone=phone, birthday=birthday)
        address_book.add_record(record)
    return f'Contact for {name.value} was added'


@input_error
def change(*args):
    name = Name(args[0][0])
    phone_to_change = Phone(args[0][1])
    phone_new = Phone(args[0][2])
    if name.value in address_book.data.keys():
        address_book.data[name.value].change_phone(phone_to_change, phone_new)
    else:
        raise ValueError('No person with this name in the address book')
    return f'Phone {phone_to_change.value} of {name.value} was changed to {phone_new.value} '


@input_error
def phone(*args):
    name = Name(args[0][0])
    if name.value in address_book.keys():
        list_of_phones = [ph.value for ph in address_book[name.value].phones]
        return ', '.join(list_of_phones)


def show_all():
    str_for_print = ''
    for k in address_book.values():
        str_for_print += str(k) + '\n'
    return str_for_print


def show_block():
    res = ''
    for record in address_book.iterator():
        res += record
    return res


def exit_out():
    return "Good bye!"


def days_to_birthday(*args):
    name = Name(args[0][0])
    if name.value in address_book.keys():
        d_t_b = address_book[name.value].days_to_birthday()
        return d_t_b


COMMANDS = {
    hello: ("hello",),
    add: ("add",),
    change: ("change",),
    phone: ("phone",),
    show_all: ("show all",),
    exit_out: ("good bye", "close", "exit"),
    days_to_birthday: ("days",),
    show_block: ("show block",),
}


def processing(customer_input):
    for k in COMMANDS:
        for command in COMMANDS[k]:
            if customer_input.lower().strip().startswith(command):
                list_of_data = customer_input[len(command):].strip().split(" ")
                return k, list_of_data


def main():
    while True:
        customer_input = input(">>>")
        func, data = processing(customer_input)
        print(func(data))
        if func == exit_out:
            break


if __name__ == '__main__':
    r1 = Record(Name("Billy"), Phone("663456789"))
    r2 = Record(Name("Susanna"), Phone("987653434"), Birthday("06.25.1995"))
    r3 = Record(Name("Jonny"), Phone("675433434"))

    ab = AddressBook()

    ab.add_record(r1)
    ab.add_record(r2)
    ab.add_record(r3)

    print(r2.days_to_birthday())

    print(r1.days_to_birthday())

    print(ab)

    for rec in ab.iterator():
        print(rec)

    for rec in ab.iterator(3):
        print(rec)

    for rec in ab.iterator(1):
        print(rec)

    address_book = AddressBook()

    main()
