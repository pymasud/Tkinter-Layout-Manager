from tkinter import *

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=200, pady=200)

#Labels
my_label = Label(text="This is old text", font=("Arial", 24, "bold"))
my_label.config(text="This is new text")
my_label.grid(column=0, row=0)

#New-Button
new_button = Button(text="Click Me", command=button_clicked)
new_button.grid(column=3, row=1)

#Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=2, row=3)


#Entry
input = Entry(width=30)
print(input.get())
input.grid(column=4, row=4)




window.mainloop()
