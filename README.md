# PRODIGY_CS_01
This is a simple Caesar Cipher GUI application built using Python's tkinter library. The application allows users to encrypt and decrypt text using the Caesar Cipher technique, which is a type of substitution cipher where each letter in the plaintext is shifted by a certain number of places down or up the alphabet.

Features
Text Input: Enter the text you want to encrypt or decrypt.
Shift Value: Specify the shift value (the number of positions each letter in the text will be moved).
Encrypt: Encrypt the input text using the specified shift value.
Decrypt: Decrypt the input text using the specified shift value.
Output: View the resulting text after encryption or decryption.
How to Run
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/caesar-cipher-gui.git
cd caesar-cipher-gui
Install the necessary dependencies:

No external libraries are required as the application only uses Python's built-in tkinter and ttk modules.

Run the application:

bash
Copy code
python caesar_cipher_gui.py
Use the Application:

Enter the text you want to encrypt or decrypt in the "Input Text" field.
Enter the shift value in the "Shift Value" field.
Click the "Encrypt" or "Decrypt" button to perform the operation.
The result will be displayed in the "Output Text" field.
Code Overview
encrypt(text, shift): Encrypts the given text by shifting its characters by the specified shift value.
decrypt(text, shift): Decrypts the given text by shifting its characters back by the specified shift value.
CaesarCipherApp: The main class that creates the GUI using tkinter and handles user interactions.
