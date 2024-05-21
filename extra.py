import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.geometry("700x500")
window.title("Sequences")
start_entry = tk.Entry(window, fg="black", bg="white", width=50)
step_entry = tk.Entry(window, fg="black", bg="white", width=50)
stop_entry = tk.Entry(window, fg="black", bg="white", width=50)

label_start = tk.Label(window, text="Start:")
label_step = tk.Label(window, text="Step:")
label_stop = tk.Label(window, text="Stop:")

label_start.pack()
start_entry.pack()
label_step.pack()
step_entry.pack()
label_stop.pack()
stop_entry.pack()


class MyRange:
    def __init__(self, start, stop, step):
        self.start = start
        self.step = step
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.step > 0:
            if self.start >= self.stop:
                raise StopIteration
            else:
                item = self.start
                self.start += self.step
                return item
        elif self.step < 0:
            if self.start <= self.stop:
                raise StopIteration
            else:
                item = self.start
                self.start += self.step
                return item


start1 = int(start_entry.get())
step1 = int(step_entry.get())
stop1 = int(stop_entry.get())
obj = MyRange(start1, stop1, step1)
my_list = []


def show_numbers():
    for i in obj:
        my_list.append(i)
        messagebox.showinfo(my_list)


show_button = tk.Button(window, text="Show the sequence", fg="white", bg="green", command=show_numbers)
show_button.pack()
window.mainloop()
