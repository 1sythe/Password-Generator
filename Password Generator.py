import tkinter as tk
from tkinter import ttk
import random
import string




root = tk.Tk()
root.title("Password Generator")
root.iconbitmap('icon.ico')
root.option_add("*tearOff", False)
root.geometry("800x400")
root.columnconfigure(index=0, weight=1)
root.columnconfigure(index=1, weight=1)
root.columnconfigure(index=2, weight=1)
root.rowconfigure(index=0, weight=1)
root.rowconfigure(index=1, weight=1)
root.rowconfigure(index=2, weight=1)
root.resizable(False, False)
style = ttk.Style(root)
strength = tk.IntVar()
length = tk.StringVar()

root.tk.call("source", "proxttk-dark.tcl")
style.theme_use("proxttk-dark")

d = tk.IntVar(value=2)
MainFrame = ttk.Frame(root, padding=(40, 0, 0, 1))
MainFrame.grid(row=0, column=1, padx=0, pady=(50, 10), sticky="nsew", rowspan=3)
MainFrame.columnconfigure(index=0, weight=1)

headline = ttk.Label(MainFrame, text="Password Generator", font="colortube", justify="center", foreground="white")
headline.grid(row=0, column=0, pady=10, columnspan=2)

fpass = ttk.Entry(MainFrame)
fpass.insert(0, "Password...")
fpass.grid(row=2, column=0, padx=200, pady=0, sticky="ew")

combo_list = ["How Many Symbols", "8", "9", "10", "11", "12", "13", "14"]

howmanysymbols = ttk.Combobox(MainFrame, values=combo_list)
howmanysymbols.current(0)
howmanysymbols.grid(row=10, column=0, padx=250, pady=10, sticky="ew")

lettersonly = ttk.Radiobutton(MainFrame, text="Letters only", variable=strength, value=1)
numbersonly = ttk.Radiobutton(MainFrame, text="Numbers only", variable=strength, value=2)
lettersandnumbers = ttk.Radiobutton(MainFrame, text="Letters and numbers", variable=strength, value=3)
lettersnumbersandsymbols = ttk.Radiobutton(MainFrame, text="Letters, numbers and symbols", variable=strength, value=4)

lettersonly.grid(row=20, column=0, padx=270, pady=2, sticky="ew")
numbersonly.grid(row=21, column=0, padx=270, pady=2, sticky="ew")
lettersandnumbers.grid(row=22, column=0, padx=270, pady=2, sticky="ew")
lettersnumbersandsymbols.grid(row=23, column=0, padx=270, pady=2, sticky="ew")

generatebutton = ttk.Button(MainFrame, text="Generate", command=lambda: random_password())
generatebutton.grid(row=25, column=0, padx=270, pady=10, sticky="ew")


def random_password():
    s = strength.get()
    if s == 1:
        symbols = string.ascii_letters
    elif s == 2:
        symbols = string.digits
    elif s == 3:
        symbols = string.ascii_letters + string.digits
    elif s == 4:
        symbols = string.ascii_letters + string.digits + string.punctuation
    else:
        fpass.delete("0", tk.END)
        fpass.insert(0, "Please Select 1 of the options")
        return

    try:
        len = int(howmanysymbols.get())

    except:
        len = 0
        fpass.delete("0", tk.END)
        fpass.insert(0, "Please choose how many symbols you want...")

    if not len == 0:
        genpassword = "".join(random.choice(symbols) for i in range(len))

        fpass.delete("0", tk.END)
        fpass.insert(0, genpassword)


root.mainloop()
