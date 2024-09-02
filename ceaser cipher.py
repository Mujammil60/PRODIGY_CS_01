import tkinter as tk
from tkinter import ttk

# Caesar Cipher functions
def encrypt(text, shift):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

# GUI application
class CaesarCipherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Caesar Cipher")

        # Text Input
        self.input_label = ttk.Label(root, text="Input Text:")
        self.input_label.grid(column=0, row=0, padx=10, pady=10)
        self.input_text = tk.Text(root, height=5, width=40)
        self.input_text.grid(column=1, row=0, padx=10, pady=10)

        # Shift Value
        self.shift_label = ttk.Label(root, text="Shift Value:")
        self.shift_label.grid(column=0, row=1, padx=10, pady=10)
        self.shift_value = ttk.Entry(root)
        self.shift_value.grid(column=1, row=1, padx=10, pady=10)

        # Encrypt Button
        self.encrypt_button = ttk.Button(root, text="Encrypt", command=self.encrypt_text)
        self.encrypt_button.grid(column=0, row=2, padx=10, pady=10)

        # Decrypt Button
        self.decrypt_button = ttk.Button(root, text="Decrypt", command=self.decrypt_text)
        self.decrypt_button.grid(column=1, row=2, padx=10, pady=10)

        # Output Text
        self.output_label = ttk.Label(root, text="Output Text:")
        self.output_label.grid(column=0, row=3, padx=10, pady=10)
        self.output_text = tk.Text(root, height=5, width=40)
        self.output_text.grid(column=1, row=3, padx=10, pady=10)

    def encrypt_text(self):
        input_text = self.input_text.get("1.0", tk.END).strip()
        shift = int(self.shift_value.get().strip())
        encrypted_text = encrypt(input_text, shift)
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, encrypted_text)

    def decrypt_text(self):
        input_text = self.input_text.get("1.0", tk.END).strip()
        shift = int(self.shift_value.get().strip())
        decrypted_text = decrypt(input_text, shift)
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, decrypted_text)

# Main loop
if __name__ == "__main__":
    root = tk.Tk()
    app = CaesarCipherApp(root)
    root.mainloop()
