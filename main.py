import tkinter as tk
from tkinter import ttk


LARGEFONT = ("Verdana", 35)


class tkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.frames = {}

        # Create instances of each frame class and add it to a dict
        for F in (StartPage, Page1, Page2):
            frame = F(self)
            self.frames[F] = frame

        # Show the StartPage initially
        self.show_frame(StartPage)

    def show_frame(self, cont):
        # Hide all frames
        for frame in self.frames.values():
            frame.place_forget()

        # Show the selected frame
        frame = self.frames[cont]
        frame.place(relx=0, rely=0, relwidth=1, relheight=1)


class StartPage(tk.Frame):
    def __init__(self, app):
        tk.Frame.__init__(self, app)
        self.configure(bg='black')  # Set background color

        # Create label and buttons for StartPage
        label = ttk.Label(self, text="Startpage", font=LARGEFONT)
        label.place(relx=0.5, rely=0.2, anchor="center")

        button1 = ttk.Button(self, text="Page 1", command=lambda: app.show_frame(Page1))
        button1.place(relx=0.5, rely=0.5, anchor="center")

        button2 = ttk.Button(self, text="Page 2", command=lambda: app.show_frame(Page2))
        button2.place(relx=0.5, rely=0.8, anchor="center")


class Page1(tk.Frame):
    def __init__(self, app):
        tk.Frame.__init__(self, app)
        self.configure(bg='black')  # Set background color

        # Create label and buttons for Page1
        label = ttk.Label(self, text="Page 1", font=LARGEFONT)
        label.place(relx=0.5, rely=0.2, anchor="center")

        button1 = ttk.Button(self, text="StartPage", command=lambda: app.show_frame(StartPage))
        button1.place(relx=0.5, rely=0.5, anchor="center")

        button2 = ttk.Button(self, text="Page 2", command=lambda: app.show_frame(Page2))
        button2.place(relx=0.5, rely=0.8, anchor="center")


class Page2(tk.Frame):
    def __init__(self, app):
        tk.Frame.__init__(self, app)
        self.configure(bg='black')  # Set background color

        # Create label and buttons for Page2
        label = ttk.Label(self, text="Page 2", font=LARGEFONT)
        label.place(relx=0.5, rely=0.2, anchor="center")

        button1 = ttk.Button(self, text="Page 1", command=lambda: app.show_frame(Page1))
        button1.place(relx=0.5, rely=0.5, anchor="center")

        button2 = ttk.Button(self, text="StartPage", command=lambda: app.show_frame(StartPage))
        button2.place(relx=0.5, rely=0.8, anchor="center")


app = tkinterApp()
app.geometry("600x400")
app.mainloop()
