import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Password Generator")
root.iconbitmap('icon.ico')
root.option_add("*tearOff", False) # This is always a good idea
root.geometry("800x400")
root.columnconfigure(index=0, weight=1)
root.columnconfigure(index=1, weight=1)
root.columnconfigure(index=2, weight=1)
root.rowconfigure(index=0, weight=1)
root.rowconfigure(index=1, weight=1)
root.rowconfigure(index=2, weight=1)
root.resizable(False,False)# Create a style
style = ttk.Style(root)

# Import the tcl file
root.tk.call("source", "proxttk-dark.tcl")

# Set the theme with the theme_use method
style.theme_use("proxttk-dark")

d = tk.IntVar(value=2)
MainFrame = ttk.Frame(root, padding=(40, 0, 0, 1))
MainFrame.grid(row=0, column=1, padx=0, pady=(50,10), sticky="nsew", rowspan=3)
MainFrame.columnconfigure(index=0, weight=1)
# Label
headline = ttk.Label(MainFrame, text="Password Generator",font="colortube" ,justify="center",foreground="white")
headline.grid(row=0, column=0, pady=50, columnspan=2)  
# Entry
fpass = ttk.Entry(MainFrame)
fpass.insert(0, "Password...")
fpass.grid(row=2, column=0, padx=200, pady=0, sticky="ew")

combo_list = ["How Many Symbols", "8", "9" , "10", "11", "12", "13", "14"]

howmanysymbols = ttk.Combobox(MainFrame,values=combo_list)
howmanysymbols.current(0)
howmanysymbols.grid(row=10, column=0, padx=250, pady=10, sticky="ew")

root.mainloop()