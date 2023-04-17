#!/usr/bin/env python3

from os.path import basename, splitext
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os.path
from pylab import plot, show

class MyEntry(tk.Entry):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)

        if not "textvariable" in kw:
            self.variable = tk.StringVar()
            self.config(textvariable=self.variable)
        else:
            self.variable = kw["textvariable"]

    @property
    def value(self):
        return self.variable.get()

    @value.setter
    def value(self, new: str):
        self.variable.set(new)


class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "Foo"

    def __init__(self):
        super().__init__(className=self.name)

        self.title(self.name)

        self.bind("<Escape>", self.quit)

        self.pathEntry = MyEntry(self, text="Soubor")
        self.pathEntry.pack()

        self.btnChoice = tk.Button(self, text="...", command=self.choice)
        self.btnChoice.pack()

        self.btnShow = tk.Button(self, text="Vykreslit", command=self.show)
        self.btnShow.pack()

        self.btn = tk.Button(self, text="Konec", command=self.quit)
        self.btn.pack()


    def choice(self):
        self.pathEntry.value = filedialog.askopenfilename()

    def show(self):
        if not os.path.isfile(self.pathEntry.value):
            messagebox.showerror("Error!", "Soubor neexistuje!")
            return
        x_axis = []
        y_axis = []
        with open(self.pathEntry.value) as f:
            while line := f.readline():
                x, y = line.split()
                x_axis.append(float(x))
                y_axis.append(float(y))
            plot(x_axis, y_axis)
            
            show()

    def quit(self, event=None):
        super().quit()
app = Application()
app.mainloop()
