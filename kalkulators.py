from tkinter import *
#Definē pogas ar cipariem
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
#Definē pogu pieskaitīšanai
def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)
#Definē pogu atņemšanai
def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)
#Definē pogu reizināšanai
def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)
#Definē pogu dalīšanai
def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)
#Definē pogu vienadībai(rezultāts)
def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + int(second_number))
    elif math == "subtraction":
        e.insert(0, f_num - int(second_number))
    elif math == "multiplication":
        e.insert(0, f_num * int(second_number))
    elif math == "division":
        e.insert(0, f_num / int(second_number))
#Definē pogu notirišanai
def button_clear():
    e.delete(0, END)
#________________________________________________________________________________________________________________________________________
mansLogs = Tk()
mansLogs.title('Kalkulators')
#________________________________________________________________________________________________________________________________________
#Pievieno pogas kalkulatorā
btn0 = Button(mansLogs, text='0', padx=40, pady=20, command=lambda: button_click(0),bg='lightgray', fg='black')
btn1 = Button(mansLogs, text='1', padx=40, pady=20, command=lambda: button_click(1),bg='lightgray', fg='black')
btn2 = Button(mansLogs, text='2', padx=40, pady=20, command=lambda: button_click(2),bg='lightgray', fg='black')
btn3 = Button(mansLogs, text='3', padx=40, pady=20, command=lambda: button_click(3),bg='lightgray', fg='black')
btn4 = Button(mansLogs, text='4', padx=40, pady=20, command=lambda: button_click(4),bg='lightgray', fg='black')
btn5 = Button(mansLogs, text='5', padx=40, pady=20, command=lambda: button_click(5),bg='lightgray', fg='black')
btn6 = Button(mansLogs, text='6', padx=40, pady=20, command=lambda: button_click(6),bg='lightgray', fg='black')
btn7 = Button(mansLogs, text='7', padx=40, pady=20, command=lambda: button_click(7),bg='lightgray', fg='black')
btn8 = Button(mansLogs, text='8', padx=40, pady=20, command=lambda: button_click(8),bg='lightgray', fg='black')
btn9 = Button(mansLogs, text='9', padx=40, pady=20, command=lambda: button_click(9),bg='lightgray', fg='black')
btn_add = Button(mansLogs, text='+', padx=40, pady=20, command=button_add, bg='orange', fg='black')
btn_subtract = Button(mansLogs, text='-', padx=40, pady=20, command=button_subtract, bg='orange', fg='black')
btn_multiply = Button(mansLogs, text='*', padx=40, pady=20, command=button_multiply, bg='orange', fg='black')
btn_divide = Button(mansLogs, text='/', padx=40, pady=20, command=button_divide, bg='orange', fg='black')
btn_equal = Button(mansLogs, text='=', padx=40, pady=20, command=button_equal, bg='orange', fg='black')
btnC=Button(mansLogs,text='C',padx=40,pady=20, command=button_clear, bg='orange', fg='black')
#________________________________________________________________________________________________________________________________________
#Nosaka atrašanas vietu pogam kalkulatorā
btn7.grid(row=1, column=0)
btn8.grid(row=1, column=1)
btn9.grid(row=1, column=2)

btn4.grid(row=2, column=0)
btn5.grid(row=2, column=1)
btn6.grid(row=2, column=2)

btn1.grid(row=3, column=0)
btn2.grid(row=3, column=1)
btn3.grid(row=3, column=2)

btn0.grid(row=4, column=0)
btn_add.grid(row=1, column=3)
btn_subtract.grid(row=2, column=3)

btn_multiply.grid(row=3, column=3)
btn_divide.grid(row=4, column=3)
btn_equal.grid(row=4, column=2)

btnC.grid(row=4, column=1)

e = Entry(mansLogs, width=15, bd=10, font=("Arial Black", 20), justify="right")
e.grid(row=0, column=0, columnspan=4)

mansLogs.mainloop()