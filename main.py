from tkinter import *

# definimos la APP
app = Tk()

# size app && fixed
app.geometry('1020x630+0+0')
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
calculator = Frame(right_side, bd=1, relief=SUNKEN, bg="coral")
calculator.pack()

# ticket
ticket = Frame(right_side, bd=1, relief=SUNKEN, bg="coral")
ticket.pack()

# buttons
buttons = Frame(right_side, bd=1, relief=SUNKEN, bg="coral")
buttons.pack()

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
                       variable=foods_placeholder[index])
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
                        variable=drinks_placeholder[index])
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
                          variable=desserts_placeholder[index])
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


# Loop de la APP
app.mainloop()
