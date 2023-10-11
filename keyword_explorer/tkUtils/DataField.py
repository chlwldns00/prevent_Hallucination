import tkinter as tk
from tkinter import ttk
from typing import List, Any, Callable

class DataField:
    name = "unset"
    value = None
    tk_label = None
    tk_entry = None
    row:int
    col:int
    wrapper:ttk.Frame

    def __init__(self, parent:'ttk.Frame', row:int, label:str, width:int = 20, password:bool = False, label_width:int = 16, sticky="nsew"):
        self.row = row
        self.wrapper = tk.Frame(parent)
        self.wrapper.grid(column=1, row=row, sticky=sticky)
        self.col = 1
        self.tk_label = tk.Label(parent, text=label, width=label_width, anchor="w")#, background="pink")
        if password:
            self.tk_entry = tk.Entry(self.wrapper, show = "*", width=width, anchor="w")
        else:
            self.tk_entry = tk.Entry(self.wrapper, width=width)


        self.tk_label.grid(column=0, row=row, sticky=(tk.W), padx=5)
        #self.tk_entry.grid(column=1, row=row, sticky=(tk.N, tk.E, tk.W), pady=2, padx=5)
        self.tk_entry.grid(column=0, row=0, sticky=(tk.W), pady=2, padx=5)
        parent.columnconfigure(1, weight=1)

    def add_button(self, name:str, command:Callable, sticky:Any = (tk.N, tk.W)) -> ttk.Button:
        b = ttk.Button(self.wrapper, text=name, command=command)
        b.grid(column=self.col, row=0, sticky=sticky, pady=2, padx=5)
        self.col += 1
        return b

    def tuple_extract(self, obj:Any, index:int=0) -> Any:
        if isinstance(obj, tuple):
            return obj[index]
        return obj

    def get_next_row(self):
        return self.row + 1

    def clear(self):
        self.tk_entry.delete(0, 'end')

    def set_bg_color(self, color:str="white"):
        print("set_bg_color: {}".format(color))
        self.tk_entry.configure(background = color)

    def set_text(self, text:str, pos:int = 0):
        self.tk_entry.delete(0, 'end')
        self.tk_entry.insert(pos, text)

    def get_text(self) -> str:
        return self.tuple_extract(self.tk_entry.get())

    def get_as_int(self, base:int = 10) -> any:
        try:
            return int(self.tuple_extract(self.get_text()), base)
        except:
            return self.get_text()

    def get_as_float(self) -> any:
        try:
            return float(self.get_text())
        except:
            return self.get_text()


    def get_list(self) -> List:
        to_return = self.tk_entry.get()
        rlist = to_return.split(',')
        to_return = []
        for t in rlist:
            to_return.append(t.strip())
        to_return = [x for x in to_return if x] # filter out the blanks
        return to_return