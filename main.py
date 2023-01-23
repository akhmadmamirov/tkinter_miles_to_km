from tkinter import *

window = Tk()
window.title("Mile to Km converter")
window.minsize(width=200, height=170)
window.config(padx=20, pady=20)

def calculate():
    mile = input.get()
    ans = round(float(mile) * 1.6,2)
    res.config(text=str(ans))
#Input
input = Entry()
input.grid(column=1, row=0)


#Miles Label
miles = Label(text="Miles", font=("Arial", 24, "bold"))
miles.grid(column=2, row=0)

#Equal Label
equal = Label(text="is equal to", font=("Arial", 24, "bold"))
equal.grid(column=0, row=1)

#Res Label
res = Label(text="0", font=("Arial", 24, "bold"))
res.grid(column=1, row=1)

#Km Label
km = Label(text="Km", font=("Arial", 24, "bold"))
km.grid(column=2, row=1)

#Button
button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)



window.mainloop()
# def button_clicked():
#     my_label["text"] = input.get()




# window = Tk()
# window.title("My first GUI")
# window.minsize(width=500, height=300)
# window.config(padx=20,pady=30)

# #Label
# my_label = Label(text="This is my text", font=("Arial", 24, "bold"))
# my_label.config(text="New Text ")
# my_label.grid(column=0, row=0)

# #Button
# new_button = Button(text="Click me", command=button_clicked)
# new_button.grid(column=2, row=0)

# #Button
# button = Button(text="Click me", command=button_clicked)
# button.grid(column=1, row=1)



# #Entry
# input = Entry()
# input.grid(column=3,row=2)



