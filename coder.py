#Russell Ryan

def encode(password):  # encodes a string
    outer = ''  # sets variable that will store the encoded password as a string

    for element in password:  # goes through every digit in the password
        if len(element) == 8:
            part = (int(element) + 3) % 10  # shifts the digit up by three numbers
            outer += str(part)  # adds the new digit to the encoded password
    return outer


def main():
    stored = None  # stores the encoded password in option 1 for use in option 2
    while True:
        print("Menu")  # displays the three options available to users
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        select = int(input("Please enter an option: "))
        if select == 1:
            passcode = str(input("Please enter your password to encode: "))  # inputs the password to be encoded
            stored = encode(passcode)  # stores the now-encoded password for later
            print("Your password has been encoded and stored!")
        elif select == 2:  # decodes the encoded password
            pass
        elif select == 3:  # ends the program
            exit()


if __name__ == '__main__':
    main()
