#Russell Ryan

def encode(password):
    outer = ''
    str(password)
    for element in password:
        if 0 <= int(element) <= 6:
            part = int(element) + 3
            outer += str(part)
    return outer


def main():
    while True:
        print("Coding Menu")
        print("-----------")
        print("Options:")
        print("1. Decoder")
        print("2. Encoder")
        select = int(input("Select an option: "))
        if select == 1:
            pass
        elif select == 2:
            passcode = str(input("Input password: "))
            print(encode(passcode))


if __name__ == '__main__':
    main()
