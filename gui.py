import tkinter as tk
from tkinter import ttk

# sudo apt-get install python3-tk

class Gui:
    def __init__(self, valutes_list):

        self.valutes_list = valutes_list

        self.root = tk.Tk()
        self.root.title("Курсы валют ЦБ РФ")
        self.root.geometry("400x300")

        valutes = ["{} | {}".format(valute.char_code, valute.name) for valute in self.valutes_list]
        self.combobox = ttk.Combobox(values=valutes)
        self.combobox.pack(anchor=tk.NW, fill=tk.X, padx=6, pady=6)
        self.combobox.bind("<<ComboboxSelected>>", self.selected)

        self.label_info = ttk.Label()
        self.label_info.pack(anchor=tk.NW, fill=tk.X, padx=5, pady=5)

        self.label_status = ttk.Label()
        self.label_status.pack(anchor=tk.NW, fill=tk.X, padx=5, pady=5)

        self.root.mainloop()

    def selected(self, event):
        # получаем выделенный элемент
        selection = self.combobox.get()
        index = self.combobox.current()

        self.label_info["text"] = self.valutes_list[index].get_info()
        self.label_status["text"] = self.valutes_list[index].get_status()
        print(selection, index, self.valutes_list[index].name)
