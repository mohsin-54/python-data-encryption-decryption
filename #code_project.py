# -*- coding: utf-8 -*-
"""
Created on Tue Nov 18 00:55:10 2025

@author: hp
"""
# ====== Data Encryption & Decryption Program ======

import os #Optinal
from cryptography.fernet import Fernet

# Using a clear screen function.
def clear_screen():
    os.system('cls')

# Step 1: Generating a key.
key = Fernet.generate_key()
cipher = Fernet(key)
clear_screen()
print("Generated Key:", key.decode())

# Step 2: Starting Main loop.
while True:
    print("Choose an option:")
    print("1. Encrypt text")
    print("2. Decrypt text manually")
    print("3. Exit\n")
    
    choice = input("Enter your choice (1/2/3): ").strip()

# Exiting program.
    if choice == "3":
        print("\nBye! :)")
        clear_screen()
        break

# Taking input from user.
    elif choice == "1":
        txt = input("\nEnter text to encrypt: ").strip()
        if not txt:
            print("No text entered! Enter again.\n")
            continue
        
# Encrypting the given data.
        print("\nGenerated Key:", key.decode())
        print(f"Length of your text: {len(txt)} characters")
        txt_byt = txt.encode()
        en_txt = cipher.encrypt(txt_byt)
        print("\nEncrypted Data:")
        print(en_txt)

        input("\nPress Enter to continue...")
        clear_screen()

# Decrypting the given data.
    elif choice == "2":
        print("\nGenerated Key:", key.decode())
        enc_txt = input("\nEnter your encrypted text to decrypt: ").strip()
        if not enc_txt:
            print("No encrypted text entered! Try again.\n")
            continue

        try:
            dec_txt = cipher.decrypt(enc_txt.encode())
            dec_str = dec_txt.decode()
            print("\nDecrypted Data:")
            print(dec_str)
            print(f"Length of your text: {len(dec_str)} characters")
        except Exception:
            print("Invalid encrypted text or key mismatch!")
        input("\nPress Enter to continue...")
        clear_screen()

    else:
        print("Invalid choice! Please select 1, 2, or 3.\n")
