import tkinter

window = tkinter.Tk()
window.title("Kilometers to Miles converter")
window.minsize(width=200, height=100)

def factor_status(factor, usr_input):
    label_miles["text"] = f"{float(usr_input) * factor}"

def button_clicked(event=None):
    user_input = float(input.get())
    button_status = button_2["text"]
    if button_status == "Km to mile":
        factor_status(1.60934, user_input)
    elif button_status == "Mile to km":
        factor_status(0.621371, user_input)
    else:
        factor_status(factor = 0, user_input=0)

def change_label(user_input=0):
    button_status = button_2["text"]
    if button_status == "Km to mile":
        button_2["text"] = "Mile to km"
        #label Górny
        my_label["text"] = "Kilometers: "
        #label Dolny
        na_label["text"] = "Miles: "
        factor_status(1.60934, user_input)
    elif button_status == "Mile to km":
        button_2["text"] = "Km to mile"
        # label Górny
        my_label["text"] = "Miles: "
        # label Dolny
        na_label["text"] = "Kilometers: "
        factor_status(0.621371, user_input)

#Label 'Kilometers'
my_label = tkinter.Label(text="Kilometers: ")
my_label.grid(column=0, row=0, sticky="e")

#Label 'Na'
na_label = tkinter.Label(text="Miles: ", anchor='w')
na_label.grid(column=0, row=1, sticky="e")

#Label 'Mile"
label_miles = tkinter.Label(text=" ")
label_miles.grid(column=1, row =1)
label_miles['text'] = " "

#Input field
input = tkinter.Entry(width=10)
input.bind("<Return>", button_clicked)
input.grid(column=1, row=0)

#Button Przelicz
button = tkinter.Button(text="Przelicz", command=button_clicked)
button.grid(column=0, row=2)

#button Miles to KM
button_2 = tkinter.Button(text="Mile to km", command=change_label)
button_2.grid(column=1, row=2)

window.mainloop()

