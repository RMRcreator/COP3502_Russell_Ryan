#Russell Ryan

def encode(password):  # encodes a string
    outer = ''  # sets variable that will store the encoded password as a string
    
    # Check if the password is 8 digits long and contains only integers
    if len(password) != 8 or not password.isdigit():
        raise ValueError("Password should be an 8-digit string containing only integers")
    else:
        for element in password:  # goes through every digit in the password
            if len(password) == 8:
                part = (int(element) + 3) % 10  # shifts the digit up by three numbers
                outer += str(part)  # adds the new digit to the encoded password
    return outer

def decode(encoded_password):
    # Convert the encoded password to a list of integers
    encoded_digits = [int(d) for d in encoded_password]
    
    # Shift each digit down by 3 numbers
    password_digits = [(d - 3) % 10 for d in encoded_digits]
    
    # Convert the password digits back to a string
    password = ''.join(str(d) for d in password_digits)
    
    return password

def main():
    #stored = None  # stores the encoded password in option 1 for use in option 2
    while True:
        print("Menu")  # displays the three options available to users
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")
        select = int(input("Please enter an option: "))
        if select == 1:
            passcode = str(input("Please enter your password to encode: "))  # inputs the password to be encoded
            stored = encode(passcode)  # stores the now-encoded password for later
            print("Your password has been encoded and stored!\n")
        elif select == 2:  # decodes the encoded password
            print(f"The encoded password is {stored}, and the original password is {decode(stored)}.\n")
        elif select == 3:  # ends the program
            False # to prevent infinite loop in emergency case*
            exit()
        else:
            print("Error: Input Valid Number")  # in case user input is outta bounds


if __name__ == '__main__':
    main()
