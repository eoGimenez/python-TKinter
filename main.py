from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox

operador = ""
food_prices = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
drink_prices = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
dessert_prices = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]


def click_button(number):
    global operador
    operador = operador + number
    calculator_view.delete(0, END)
    calculator_view.insert(END, operador)


def clear():
    global operador
    operador = ""
    calculator_view.delete(0, END)


def result():
    global operador
    resultado = str(eval(operador))
    calculator_view.delete(0, END)
    calculator_view.insert(END, resultado)
    operador = ""


def check_button():
    counter = 0
    for x in foods_frames:
        if foods_placeholder[counter].get() == 1:
            foods_frames[counter].config(state=NORMAL)
            if foods_frames[counter].get() == "0":
                foods_frames[counter].delete(0, END)
            foods_frames[counter].focus()
        else:
            foods_frames[counter].config(state=DISABLED)
            foods_text[counter].set('0')
        counter += 1
    counter = 0
    for x in drinks_frames:
        if drinks_placeholder[counter].get() == 1:
            drinks_frames[counter].config(state=NORMAL)
            if drinks_frames[counter].get() == "0":
                drinks_frames[counter].delete(0, END)
            drinks_frames[counter].focus()
        else:
            drinks_frames[counter].config(state=DISABLED)
            drinks_text[counter].set('0')
        counter += 1
    counter = 0
    for x in desserts_frames:
        if desserts_placeholder[counter].get() == 1:
            desserts_frames[counter].config(state=NORMAL)
            if desserts_frames[counter].get() == "0":
                desserts_frames[counter].delete(0, END)
            desserts_frames[counter].focus()
        else:
            desserts_frames[counter].config(state=DISABLED)
            desserts_text[counter].set('0')
        counter += 1


def total():
    sub_total_food = 0
    for index, each in enumerate(foods_text):
        sub_total_food += (float(each.get()) * food_prices[index])

    sub_total_drink = 0
    for index, each in enumerate(drinks_text):
        sub_total_drink += (float(each.get()) * drink_prices[index])

    sub_total_dessert = 0
    for index, each in enumerate(desserts_text):
        sub_total_dessert += (float(each.get()) * dessert_prices[index])

    sub_total = sub_total_food + sub_total_drink + sub_total_dessert
    taxes = sub_total * .07
    total = sub_total + taxes
    var_price_food.set(f"$ {round(sub_total_food, 2)}")
    var_price_drink.set(f"$ {round(sub_total_drink, 2)}")
    var_price_dessert.set(f"$ {round(sub_total_dessert, 2)}")
    var_subtotal.set(f"$ {round(sub_total, 2)}")
    var_taxes.set(f"$ {round(taxes, 2)}")
    var_total.set(f"$ {round(total, 2)}")


def ticket():
    text_ticket.delete(1.0, END)
    ticket_num = f"N# - {random.randint(1000,9999)}"
    date = datetime.datetime.now()
    date_ticket = date.strftime('%d/%m/%Y - %H:%M')
    text_ticket.insert(
        END, f'Datos:\t{ticket_num}\t\t{date_ticket}\n')
    text_ticket.insert(END, "*" * 59 + "\n")
    text_ticket.insert(END, "Items\t\tCant.\tCosto Items\n")
    text_ticket.insert(END, "-" * 71 + "\n")
    counter = 0
    for food_t in foods_text:
        if food_t.get() != "0":
            text_ticket.insert(
                END, f'{food_array[counter]}\t\t{food_t.get()}\t'
                f'${int(food_t.get()) * food_prices[counter]}\n')
        counter += 1
    counter = 0
    for drink_t in drinks_text:
        if drink_t.get() != "0":
            text_ticket.insert(
                END, f'{drinks_array[counter]}\t\t{drink_t.get()}\t'
                f'${int(drink_t.get()) * drink_prices[counter]}\n')
        counter += 1
    counter = 0
    for dessert_t in foods_text:
        if dessert_t.get() != "0":
            text_ticket.insert(
                END, f'{dessert_array[counter]}\t\t{dessert_t.get()}\t'
                f'${int(dessert_t.get()) * dessert_prices[counter]}\n')
        counter += 1

    text_ticket.insert(END, "-" * 71 + "\n")
    text_ticket.insert(
        END, f'Costo de la comidas: \t\t\t{var_price_food.get()}\n')
    text_ticket.insert(
        END, f'Costo de la bebidas: \t\t\t{var_price_drink.get()}\n')
    text_ticket.insert(
        END, f'Costo de la postres: \t\t\t{var_price_dessert.get()}\n')
    text_ticket.insert(END, "-" * 71 + "\n")
    text_ticket.insert(
        END, f'Costo de la subtotal: \t\t\t{var_subtotal.get()}\n')
    text_ticket.insert(
        END, f'Costo de la impuestos: \t\t\t{var_taxes.get()}\n')
    text_ticket.insert(END, f'Costo de la total: \t\t\t{var_total.get()}\n')
    text_ticket.insert(END, "*" * 59 + "\n")
    text_ticket.insert(END, "\tGracias por su visita")


def save():
    info_ticket = text_ticket.get(1.0, END)
    file = filedialog.asksaveasfile(mode="w", defaultextension=".txt")
    file.write(info_ticket)
    file.close()
    messagebox.showinfo("Información", "Su recibo ha sido guardado")


def reset():
    text_ticket.delete(0.1, END)
    for text in foods_text:
        text.set('0')
    for text in drinks_text:
        text.set('0')
    for text in desserts_text:
        text.set('0')

    for frame in foods_frames:
        frame.config(state=DISABLED)
    for frame in drinks_frames:
        frame.config(state=DISABLED)
    for frame in desserts_frames:
        frame.config(state=DISABLED)

    for v in foods_placeholder:
        v.set(0)
    for v in drinks_placeholder:
        v.set(0)
    for v in desserts_placeholder:
        v.set(0)
    var_price_food.set('')
    var_price_drink.set('')
    var_price_dessert.set('')
    var_subtotal.set('')
    var_taxes.set('')
    var_total.set('')


# definimos la APP
app = Tk()

# size app && fixed
app.geometry('1180x630+0+0')
app.resizable(0, 0)

# customs
app.title("Operational Systems")
app.config(bg="coral")

# header
header = Frame(app, bd=1, relief=SUNKEN)
header.pack(side=TOP)

title = Label(header, text="Sistema de Facturacion", fg="azure4",
              font=("Arial", 48), bg="coral", width=27)
title.grid(row=0, column=0)

# left side
left_side = Frame(app, bd=1, relief=SUNKEN)
left_side.pack(side=LEFT)

# left down
left_down = Frame(left_side, bd=1, relief=SUNKEN, bg="azure4", padx=50)
left_down.pack(side=BOTTOM)

# food
food_p = LabelFrame(left_side, text="Comida", font=("Arial", 19, "bold"),
                    bd=1, relief=SUNKEN, fg="coral")
food_p.pack(side=LEFT)


# drinks
drink_p = LabelFrame(left_side, text="Bebidas", font=("Arial", 19, "bold"),
                     bd=1, relief=SUNKEN, fg="coral")
drink_p.pack(side=LEFT)


# dessert
dessert_p = LabelFrame(left_side, text="Postres", font=("Arial", 19, "bold"),
                       bd=1, relief=SUNKEN, fg="coral")
dessert_p.pack(side=LEFT)

# right side
right_side = Frame(app, bd=1, relief=SUNKEN)
right_side.pack(side=RIGHT)

# calculator
calculator_p = Frame(right_side, bd=1, relief=SUNKEN, bg="coral")
calculator_p.pack()

# ticket
ticket_p = Frame(right_side, bd=1, relief=SUNKEN, bg="coral")
ticket_p.pack()

# buttons
buttons_p = Frame(right_side, bd=1, relief=SUNKEN, bg="coral")
buttons_p.pack()

# product lists

food_array = ["Pollo", "Cordero", "Salmón", "Merluza",
              "Pizza1", "Pizza2", "Pizza3", "Hamburguesa"]
drinks_array = ["Agua", "Soda", "Jugo", "Cola",
                "Vino1", "Vino2", "Cerveza1", "Cerveza2", ]
dessert_array = ["Helado", "Fruta", "Brownie",
                 "Flan", "Mousse", "Pastel1", "Pastel2", "Pastel3"]

foods_placeholder = []
foods_frames = []
foods_text = []
for index, food in enumerate(food_array):
    # checkButton
    foods_placeholder.append('')
    foods_placeholder[index] = IntVar()
    food = Checkbutton(food_p,
                       text=food.title(),
                       font=("Arial", 18, "bold"),
                       onvalue=1,
                       offvalue=0,
                       variable=foods_placeholder[index],
                       command=check_button)
    food.grid(row=index,
              column=0,
              sticky=W)

    # create frames
    foods_frames.append("")
    foods_text.append("")
    foods_text[index] = StringVar()
    foods_text[index].set("0")
    foods_frames[index] = Entry(food_p,
                                font=("Arial", 18, "bold"),
                                bd=1,
                                width=6,
                                state=DISABLED,
                                textvariable=foods_text[index])
    foods_frames[index].grid(row=index, column=1)

# DRINKS

drinks_placeholder = []
drinks_frames = []
drinks_text = []
for index, drink in enumerate(drinks_array):
    drinks_placeholder.append('')
    drinks_placeholder[index] = IntVar()
    drink = Checkbutton(drink_p,
                        text=drink.title(),
                        font=("Arial", 18, "bold"),
                        onvalue=1,
                        offvalue=0,
                        variable=drinks_placeholder[index],
                        command=check_button)
    drink.grid(row=index,
               column=0,
               sticky=W)

    # create frames
    drinks_frames.append("")
    drinks_text.append("")
    drinks_text[index] = StringVar()
    drinks_text[index].set("0")
    drinks_frames[index] = Entry(drink_p,
                                 font=("Arial", 18, "bold"),
                                 bd=1,
                                 width=6,
                                 state=DISABLED,
                                 textvariable=drinks_text[index])
    drinks_frames[index].grid(row=index, column=1)

# DESSERTS
desserts_placeholder = []
desserts_frames = []
desserts_text = []
for index, dessert in enumerate(dessert_array):
    desserts_placeholder.append('')
    desserts_placeholder[index] = IntVar()
    dessert = Checkbutton(dessert_p,
                          text=dessert.title(),
                          font=("Arial", 18, "bold"),
                          onvalue=1,
                          offvalue=0,
                          variable=desserts_placeholder[index],
                          command=check_button)
    dessert.grid(row=index,
                 column=0,
                 sticky=W)

    # create frames
    desserts_frames.append("")
    desserts_text.append("")
    desserts_text[index] = StringVar()
    desserts_text[index].set("0")
    desserts_frames[index] = Entry(dessert_p,
                                   font=("Arial", 18, "bold"),
                                   bd=1,
                                   width=6,
                                   state=DISABLED,
                                   textvariable=desserts_text[index])
    desserts_frames[index].grid(row=index, column=1)

# prices labels

var_price_food = StringVar()
var_price_drink = StringVar()
var_price_dessert = StringVar()
var_subtotal = StringVar()
var_taxes = StringVar()
var_total = StringVar()
# food
labels_prices_food = Label(left_down,
                           text="Costo Comida",
                           font=("Arial", 12, "bold"),
                           bg="azure4",
                           fg="white")
labels_prices_food.grid(row=0, column=0)
text_price_food = Entry(left_down,
                        font=("Arial", 12, "bold"),
                        bd=1,
                        width=10,
                        state="readonly",
                        textvariable=var_price_food)
text_price_food.grid(row=0, column=1, padx=41)

# drinks
labels_prices_drink = Label(left_down,
                            text="Costo Bebida",
                            font=("Arial", 12, "bold"),
                            bg="azure4",
                            fg="white")
labels_prices_drink.grid(row=1, column=0)
text_price_drink = Entry(left_down,
                         font=("Arial", 12, "bold"),
                         bd=1,
                         width=10,
                         state="readonly",
                         textvariable=var_price_drink)
text_price_drink.grid(row=1, column=1, padx=41)

# desserts
labels_prices_dessert = Label(left_down,
                              text="Costo Postre",
                              font=("Arial", 12, "bold"),
                              bg="azure4",
                              fg="white")
labels_prices_dessert.grid(row=2, column=0)
text_price_dessert = Entry(left_down,
                           font=("Arial", 12, "bold"),
                           bd=1,
                           width=10,
                           state="readonly",
                           textvariable=var_price_dessert)
text_price_dessert.grid(row=2, column=1, padx=41)

# subtotal
labels_subtotal = Label(left_down,
                        text="Subtotal",
                        font=("Arial", 12, "bold"),
                        bg="azure4",
                        fg="white")
labels_subtotal.grid(row=0, column=2)
text_subtotal = Entry(left_down,
                      font=("Arial", 12, "bold"),
                      bd=1,
                      width=10,
                      state="readonly",
                      textvariable=var_subtotal)
text_subtotal.grid(row=0, column=3, padx=41)
# taxes
labels_taxes = Label(left_down,
                     text="Impuestos",
                     font=("Arial", 12, "bold"),
                     bg="azure4",
                     fg="white")
labels_taxes.grid(row=1, column=2)
text_taxes = Entry(left_down,
                   font=("Arial", 12, "bold"),
                   bd=1,
                   width=10,
                   state="readonly",
                   textvariable=var_taxes)
text_taxes.grid(row=1, column=3, padx=41)
# Total
labels_total = Label(left_down,
                     text="Total",
                     font=("Arial", 12, "bold"),
                     bg="azure4",
                     fg="white")
labels_total.grid(row=2, column=2)
text_total = Entry(left_down,
                   font=("Arial", 12, "bold"),
                   bd=1,
                   width=10,
                   state="readonly",
                   textvariable=var_total)
text_total.grid(row=2, column=3, padx=41)


# botones
array_buttons = ["Total", "Recibo", "Guardar", "Resetear"]
created_buttons = []
for index, button in enumerate(array_buttons):
    button = Button(buttons_p,
                    text=button.title(),
                    font=("Arial", 14, "bold"),
                    fg="white",
                    bg="azure4",
                    bd=1,
                    width=9)
    created_buttons.append(button)
    button.grid(row=0,
                column=index)

created_buttons[0].config(command=total)
created_buttons[1].config(command=ticket)
created_buttons[2].config(command=save)
created_buttons[3].config(command=reset)

# ticket
text_ticket = Text(ticket_p,
                   font=("Arial", 12, "bold"),
                   bd=1,
                   width=50,
                   height=10)
text_ticket.grid(row=0, column=0)

# calculator

calculator_view = Entry(calculator_p,
                        font=("Arial", 16, "bold"),
                        width=38,
                        bd=1)
calculator_view.grid(row=0,
                     column=0,
                     columnspan=4)
calc_buttons = ["7", "8", "9", "+", "4", "5", "6",
                "-", "1", "2", "3", "x", "R", "B", "0", "/"]
row_calc = 1
column_calc = 0
buttons_saved = []
for button in calc_buttons:
    button = Button(calculator_p,
                    text=button.title(),
                    font=("Arial", 16, "bold"),
                    fg="white",
                    bg="azure4",
                    bd=1,
                    width=8)
    buttons_saved.append(button)
    button.grid(row=row_calc,
                column=column_calc)
    if column_calc == 3:
        row_calc += 1
    column_calc += 1
    if column_calc == 4:
        column_calc = 0

buttons_saved[0].config(command=lambda: click_button("7"))
buttons_saved[1].config(command=lambda: click_button("8"))
buttons_saved[2].config(command=lambda: click_button("9"))
buttons_saved[3].config(command=lambda: click_button("+"))
buttons_saved[4].config(command=lambda: click_button("4"))
buttons_saved[5].config(command=lambda: click_button("5"))
buttons_saved[6].config(command=lambda: click_button("6"))
buttons_saved[7].config(command=lambda: click_button("-"))
buttons_saved[8].config(command=lambda: click_button("1"))
buttons_saved[9].config(command=lambda: click_button("2"))
buttons_saved[10].config(command=lambda: click_button("3"))
buttons_saved[11].config(command=lambda: click_button("*"))
buttons_saved[14].config(command=lambda: click_button("0"))
buttons_saved[15].config(command=lambda: click_button("/"))
buttons_saved[13].config(command=clear)
buttons_saved[12].config(command=result)

# Loop de la APP
app.mainloop()
