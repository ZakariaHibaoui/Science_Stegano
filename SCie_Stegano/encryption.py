import tkinter as tk

from cryptography.fernet import Fernet

key1 = b'u8RAvUKIPE3w3VLklEqXv4466uCeEvlKxCvdvEjxDUs='


def encrypter():
    f = Fernet(key1)
    message = word.get()
    x = message.encode()
    encryption = f.encrypt(x)
    encrypted.delete(0, tk.END)  # clear the entry field
    encrypted.insert(0, encryption)


def decrypter():
    f = Fernet(key1)
    message2 = encrypt.get()
    decryption = f.decrypt(message2.encode())
    decrypt.delete(0, tk.END)  # clear the entry field
    decrypt.insert(0, decryption)


def keycreator():
    global key1
    key1 = Fernet.generate_key()
    key.insert(0, key1)


window = tk.Tk()
window.title("Encrypter/Decrypter")

frame = tk.Frame(master=window, width=500, height=500)
frame.pack()

label1 = tk.Label(master=frame, text='Word')
label1.place(x=10, y=5)

word = tk.Entry(master=frame)
word.place(x=0, y=25)

btn_convert_encrypt = tk.Button(master=frame, text="\N{DOWNWARDS BLACK ARROW}", command=encrypter)
btn_convert_encrypt.place(x=40, y=50)

label2 = tk.Label(master=frame, text='Encrypted')
label2.place(x=10, y=80)

encrypted = tk.Entry(master=frame)
encrypted.place(x=0, y=100)

label3 = tk.Label(master=frame, text='Encrypted')
label3.place(x=250, y=5)

encrypt = tk.Entry(master=frame)
encrypt.place(x=250, y=25)

btn_convert_decrypt = tk.Button(master=frame, text="\N{DOWNWARDS BLACK ARROW}", command=decrypter)
btn_convert_decrypt.place(x=290, y=50)

label4 = tk.Label(master=frame, text='Word')
label4.place(x=250, y=80)

decrypt = tk.Entry(master=frame)
decrypt.place(x=250, y=100)

label5 = tk.Label(master=frame, text='Key')
label5.place(x=170, y=130)

key = tk.Entry(master=frame)
key.place(x=125, y=150)

btn_randmize = tk.Button(master=frame, text="Randmize", command=keycreator)
btn_randmize.place(x=150, y=175)

window.mainloop()