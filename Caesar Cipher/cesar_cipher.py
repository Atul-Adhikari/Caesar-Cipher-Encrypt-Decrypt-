'''Author :Atul Adhikari'''

#Importing the os module
import os
#function to print welcome message.
def welcome():
    '''Displays the welcome message'''
    print("Welcome to the Caesar Cipher.")
    print("This program encrypts and decrypts text with the Caesar Cipher.")

#Function that takes mode of conversion and message to be encrypted or decrypted
def enter_message():
    '''Returns the mode, message, and shift entered by the user'''
    check=True
    while check:
        mode=input("Would you like to encrypt(e) or decrypt(d): ").lower()
        if mode in {"E", "D"}:
            check=False
        else:
            print("Invalid Mode")
    msg = input(f"What message would you like to {'encrypt' if mode == 'E' else 'decrypt'}: ")

    while True:
        msg = input(
    f"What message would you like to {'encrypt' if mode.lower() == 'e' else 'decrypt'}: "
)

        try:
            shift = int(input("What is the shift number: "))
            if 0 <= shift <= 25:
                break
            print("Invalid Shift")
        except ValueError:
            print("Please enter a number")
    return mode,msg.lower(),shift

#Function to encrypt the message
def encrypt(msg,shiftvalue):
    '''Returns the encrypted message'''
    encryptedmsg=""
    for i in range(len(msg)):
        if msg[i].isalpha():
            encryptedmsg+=chr((ord(msg[i])-65+shiftvalue)%26+65)
        else:
            encryptedmsg=encryptedmsg+msg[i]
    return encryptedmsg

#Function to decrypt the message
def decrypt(msg,shiftvalue):
    '''Returns the decrypted message'''
    return encrypt(msg,-shiftvalue)

#Function that takes file name and conversion mode.
def process_file(fname,conmode,shift):
    '''Returns list after encrypting or decrypting the lines of file.'''
    messages=[]
    with open(fname,"r",encoding="utf-8") as file:
        for line in file:
            line=line.strip()
            if conmode=="E":
                messages.append(encrypt(line.upper(),shift))
            else:
                messages.append(decrypt(line.upper(),shift))
    return messages

#Function to check whether the file exist or not
def is_file(fname):
    '''Returns True is the file exist and returns False if the file doesnot exist'''
    return os.path.isfile(fname)

#Takes a list of strings and write these strings to file results.txt
def write_messages(messages):
    '''Writes all the data from the list(messages) to results.txt. '''
    with open("results.txt","w",encoding="utf-8")as file:
        for eachmsg in messages:
            file.write(eachmsg+"\n")

#ask the user to encrypt/decrypt from console or from file
def message_or_file():
    '''Takes user input to encrypt/decrypt from console or from the file'''
    check=True
    while check:
        mode=input("Would you like to encrypt(e) or decrypt(d): ").upper()
        if mode in {"E","D"}:
            check=False
        else:
            print("Invalid Mode")
    while True:
        source = input("Would you like to read from a file (f) or the console (c)? ").upper()
        if source in ["F", "C"]:
            break
        print("Invalid Source")
    filename=None
    if source=="F":
        while True:
            filename=input("Enter a filename: ")
            if is_file(filename):
                break
            print("Invalid Filename")
    if source=="C":
        message = input(
            f"What message would you like to {'encrypt' if mode == 'E' else 'decrypt'}: ").upper()
        while True:
            try:
                shift = int(input("What is the shift number: "))
                if (shift>=0 and shift<= 25):
                    break
                print("Invalid Shift")
            except ValueError:
                print("Invalid Shift (Please enter a number)")
        return mode,message,filename,shift
    #Gets executed when the while loop condition becomes false.
    else:
        while True:
            try:
                shift = int(input("What is the shift number: "))
                if (shift>=0 and shift<= 25):
                    break
                print("Invalid Shift")
            except ValueError:
                print("Invalid Shift (Please enter a number)")
        return mode,None,filename,shift

#Main function containing the main logic
def main():
    '''Main function to run other functions '''

    #Calling welcome function to display welcome message
    welcome()
    while True:
        mode,message,filename,shift=message_or_file()
        if mode=="E":
            if filename:
                messages = process_file(filename, mode, shift)
                write_messages(messages)
                print("Output written to results.txt")
            else:
                print(encrypt(message, shift))
        else:
            if filename:
                messages = process_file(filename, mode, shift)
                write_messages(messages)
                print("Output written to results.txt")
            else:
                print(decrypt(message, shift))
        choice=input("Would you like to encrypt or decrypt another message? (y/n): ")
        while(choice.lower() not in ["y","n"]):
            print("Invalid choice")
            choice=input("Would you like to encrypt or decrypt another message? (y/n): ")
        if choice.lower()=="n":
            print("Thanks for using the program, Goodbye!")
            break

main()
