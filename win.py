import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Hello World")
root.geometry('600x400')
root.resizable(False, False)

message = tk.Label(root, text ="Hello, World!", fg="blue", font=("Helvetica,14")).pack()
message = tk.Label(root, text ="Click here to Print", fg="blue", font=("Helvetica,14")).pack()

def button1Function(): print("Hello World")
def button2Function(): root.destroy()

b1_button = ttk.Button(root, text="Print", command=button1Function)
b1_button.pack(ipadx=5, ipady=5, expand=True)
b2_button = ttk.Button(root, text="Exit", command=button2Function)
b2_button.pack(ipadx=5, ipady=5, expand=True)

root.mainloop()
