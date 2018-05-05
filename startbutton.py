import tkinter as tk
import button2new as bt
import update as up

class Example(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        new_win_button = tk.Button(self, text="CHECK",
                                   command=self.new_window)
        new_win_button1 = tk.Button(self, text="UPDATE",
                                   command=self.new_window1)
        new_win_button.pack(side="top", padx=20, pady=20)
        new_win_button1.pack(side="bottom", padx=20, pady=20)


    def new_window(self):
        bt.driver()

    def new_window1(self):
        up.update()



if __name__ == "__main__":
    root = tk.Tk()
    Example(root).pack(fill="both", expand=True)

    root.mainloop()