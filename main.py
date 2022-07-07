import time
from tkinter import *
from PIL import ImageTk, Image
import sql

schwaninger_img = Image.open("imgs/schwaninger.png")
alma_img = Image.open("imgs/alma.png")
zita_img = Image.open("imgs/zita.png")
ernst_img = Image.open("imgs/ernst.png")
otto_img = Image.open("imgs/otto.png")
gerda_img = Image.open("imgs/gerda.png")
rosa_img = Image.open("imgs/rosa.png")
berta_img = Image.open("imgs/berta.png")
paula_img = Image.open("imgs/paula.png")
emil_img = Image.open("imgs/emil.png")
ida_img = Image.open("imgs/ida.png")
XÆA12_img = Image.open("imgs/elon.png")
ChadSchwaninger_img = Image.open("imgs/chad.png")
unknown_img = Image.open("imgs/unknown.png")

imgs = [alma_img, zita_img, ernst_img, otto_img, gerda_img, rosa_img, berta_img, paula_img, emil_img, ida_img, XÆA12_img, ChadSchwaninger_img]
names = ['Alma','Zita','Otto','Ernst','Gerda','Rosa','Berta','Paula','Emil','Ida','XÆA12', 'ChadSchwaninger']

number = 0
sps = 0
upgrade1 = None
upgrade2 = None
upgrade3 = None
upgrade4 = None
upgrade5 = None
upgrade6 = None
upgrade7 = None
upgrade8 = None
upgrade9 = None
upgrade10 = None
upgrade11 = None
upgrade12 = None

root = Tk()

label1 = Label(root, text="Click to cum", font=("Arial", 30))
label1.grid(column=1, row=4)

label2 = Label(root, text="Sperms Per Second", font=("Arial", 30))
label2.grid(column=2, row=4)


#        ███╗   ███╗ █████╗ ██╗███╗   ██╗
#        ████╗ ████║██╔══██╗██║████╗  ██║
#        ██╔████╔██║███████║██║██╔██╗ ██║
#        ██║╚██╔╝██║██╔══██║██║██║╚██╗██║
#        ██║ ╚═╝ ██║██║  ██║██║██║ ╚████║
#        ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝
def set_sperms(sperms):
    global number
    number = sperms


def set_sps(spermsPerSec):
    global sps
    sps = spermsPerSec


def buy(numberOfKind, upgradeButton, sperms, spermsPerSec):
    kind_amount = sql.get_kind_amount(numberOfKind)
    kind_sps = sql.get_kind_sps(numberOfKind) * sql.get_kind_amount(numberOfKind)
    kind_price = sql.get_kind_price(numberOfKind)

    # sets new sperms and sps
    set_sperms(sperms-kind_price)
    set_sps(spermsPerSec+sql.get_kind_sps(numberOfKind))

    #adds kind in SQL and increases the price by 5%
    sql.set_kind_price(numberOfKind,kind_price+(kind_price*0.07))
    sql.set_kind_amount(numberOfKind,kind_amount+1)

    sql.set_main_sps(sql.get_main_sps()+sql.get_kind_sps(numberOfKind))

    kind_amount = sql.get_kind_amount(numberOfKind)
    kind_sps = sql.get_kind_sps(numberOfKind) * sql.get_kind_amount(numberOfKind)
    kind_price = sql.get_kind_price(numberOfKind)

    # updates button text
    print(1)
    upgradeButton.config(text="[{} Stück] ".format(str(kind_amount)) + names[numberOfKind-1] + "\n SPS: {} \nPreis: {:.1f} Sperms".format(str(kind_sps),kind_price))
    print(2)
    #executes main to disable button when not enouth money
    main()

def check_price_for_upgrade(kind,button):
    global number
    kind_amount = sql.get_kind_amount(kind)
    kind_sps = sql.get_kind_sps(kind) * sql.get_kind_amount(kind)
    kind_price = sql.get_kind_price(kind)

    if sql.get_kind_amount(kind) == 0:
        button.config(image=unknown_img, compound=LEFT)
    elif kind == 1:
        button.config(image=alma_img, compound=LEFT)
    elif kind == 2:
        button.config(image=zita_img, compound=LEFT)
    elif kind == 3:
        button.config(image=ernst_img, compound=LEFT)
    elif kind == 4:
        button.config(image=otto_img, compound=LEFT)
    elif kind == 5:
        button.config(image=gerda_img, compound=LEFT)
    elif kind == 6:
        button.config(image=rosa_img, compound=LEFT)
    elif kind == 7:
        button.config(image=berta_img, compound=LEFT)
    elif kind == 8:
        button.config(image=paula_img, compound=LEFT)
    elif kind == 9:
        button.config(image=emil_img, compound=LEFT)
    elif kind == 10:
        button.config(image=ida_img, compound=LEFT)
    elif kind == 11:
        button.config(image=XÆA12_img, compound=LEFT)
    elif kind == 12:
        button.config(image=ChadSchwaninger_img, compound=LEFT)

    if number < sql.get_kind_price(kind):
        button.config(bg="gray")
        button.config(state=DISABLED)
    else:
        button.config(bg="blue")
        button.config(state=NORMAL)

def main():
    global sps
    global label2
    check_price_for_upgrade(1,upgrade1)
    check_price_for_upgrade(2,upgrade2)
    check_price_for_upgrade(3, upgrade3)
    check_price_for_upgrade(4, upgrade4)
    check_price_for_upgrade(5, upgrade5)
    check_price_for_upgrade(6, upgrade6)
    check_price_for_upgrade(7, upgrade7)
    check_price_for_upgrade(8, upgrade8)
    check_price_for_upgrade(9, upgrade9)
    check_price_for_upgrade(10, upgrade10)
    check_price_for_upgrade(11, upgrade11)
    check_price_for_upgrade(12, upgrade12)

    label2.config(text=str(str(sps)) + " SPS")


# saves data
def save():
    sql.set_main_sperms(number)
    root.destroy()
    print("Saved")


# Loads saved data
def load():
    global number
    global sps
    global label1
    global label2
    number = sql.get_main_sperms()
    sps = sql.get_main_sps()
    label2.config(text=str(sps) + " SPS")
    if(number == 1):
        label1.config(text="{:.1f} Sperm".format(number))
    else:
        label1.config(text="{:.1f} Sperms".format(number))

    print("Loaded")
    main()



def click():
    global sps
    global number

    number += 1+(sps*0.03)

    if(number == 1):
        label1.config(text="{:.1f} Sperm".format(number))
    else:
        label1.config(text="{:.1f} Sperms".format(number))
    main()


#         ██████╗ ██╗   ██╗██╗
#        ██╔════╝ ██║   ██║██║
#        ██║  ███╗██║   ██║██║
#        ██║   ██║██║   ██║██║
#        ╚██████╔╝╚██████╔╝██║
#         ╚═════╝  ╚═════╝ ╚═╝

#images
schwaninger_img = ImageTk.PhotoImage(Image.open("imgs/schwaninger.png"))
alma_img = ImageTk.PhotoImage(Image.open("imgs/alma.png"))
zita_img = ImageTk.PhotoImage(Image.open("imgs/zita.png"))
ernst_img = ImageTk.PhotoImage(Image.open("imgs/ernst.png"))
otto_img = ImageTk.PhotoImage(Image.open("imgs/otto.png"))
gerda_img = ImageTk.PhotoImage(Image.open("imgs/gerda.png"))
rosa_img = ImageTk.PhotoImage(Image.open("imgs/rosa.png"))
berta_img = ImageTk.PhotoImage(Image.open("imgs/berta.png"))
paula_img = ImageTk.PhotoImage(Image.open("imgs/paula.png"))
emil_img = ImageTk.PhotoImage(Image.open("imgs/emil.png"))
ida_img = ImageTk.PhotoImage(Image.open("imgs/ida.png"))
XÆA12_img = ImageTk.PhotoImage(Image.open("imgs/elon.png"))
ChadSchwaninger_img = ImageTk.PhotoImage(Image.open("imgs/chad.png"))
unknown_img = ImageTk.PhotoImage(Image.open("imgs/unknown.png"))

#checks if database is available
sql.main()

#sets screensize and title
root.geometry("1536x864")
root.title("SchwanniClick")

# Main click button
clickButton = Button(root, command=lambda: click(), width=50, height=160, bg="red", image=schwaninger_img, compound=CENTER)
clickButton.grid(row=0, column=0, sticky=EW)
#clickButton.place(x=0, y=20)
#clickButton.pack(fill='y', side='left')

# upgrades
upgrade1 = Button(root, text="[{} Stück] Alma \n SPS: {} \nPreis: {:.1f} Sperms".format(sql.get_kind_amount(1), sql.get_kind_sps(1)*sql.get_kind_amount(1), sql.get_kind_price(1)), width=352, height=108, bg="blue",
                  command=lambda : buy(1,upgrade1,number,sps),image=alma_img, compound=LEFT)
upgrade1.grid(row=1, column=0, sticky=N)

upgrade2 = Button(root, text="[{} Stück] Zita \n SPS: {} \nPreis: {:.1f} Sperms".format(sql.get_kind_amount(2), sql.get_kind_sps(2)*sql.get_kind_amount(2), sql.get_kind_price(2)), width=352, height=108, bg="blue",
                  command=lambda : buy(2,upgrade2,number,sps),image=zita_img, compound=LEFT)
upgrade2.grid(row=1, column=1, sticky=N)

upgrade3 = Button(root, text="[{} Stück] Otto \n SPS: {} \nPreis: {:.1f} Sperms".format(sql.get_kind_amount(3), sql.get_kind_sps(3)*sql.get_kind_amount(3), sql.get_kind_price(3)), width=352, height=108, bg="blue",
                  command=lambda : buy(3,upgrade3,number,sps),image=otto_img, compound=LEFT)
upgrade3.grid(row=1, column=2, sticky=N)

upgrade4 = Button(root, text="[{} Stück] Ernst \n SPS: {} \nPreis: {:.1f} Sperms".format(sql.get_kind_amount(4), sql.get_kind_sps(4)*sql.get_kind_amount(4), sql.get_kind_price(4)), width=352, height=108, bg="blue",
                  command=lambda : buy(4,upgrade4,number,sps),image=ernst_img, compound=LEFT)
upgrade4.grid(row=1, column=3, sticky=N)

upgrade5 = Button(root, text="[{} Stück] Gerda \n SPS: {} \nPreis: {:.1f} Sperms".format(sql.get_kind_amount(5), sql.get_kind_sps(5)*sql.get_kind_amount(5), sql.get_kind_price(5)), width=352, height=108, bg="blue",
                  command=lambda : buy(5,upgrade5,number,sps),image=gerda_img, compound=LEFT)
upgrade5.grid(row=2, column=0, sticky=N)

upgrade6 = Button(root, text="[{} Stück] Rosa \n SPS: {} \nPreis: {:.1f} Sperms".format(sql.get_kind_amount(6), sql.get_kind_sps(6)*sql.get_kind_amount(6), sql.get_kind_price(6)), width=352, height=108, bg="blue",
                  command=lambda : buy(6,upgrade6,number,sps),image=rosa_img, compound=LEFT)
upgrade6.grid(row=2, column=1, sticky=N)

upgrade7 = Button(root, text="[{} Stück] Berta \n SPS: {} \nPreis: {:.1f} Sperms".format(sql.get_kind_amount(7), sql.get_kind_sps(7)*sql.get_kind_amount(7), sql.get_kind_price(7)), width=352, height=108, bg="blue",
                  command=lambda : buy(7,upgrade7,number,sps),image=berta_img, compound=LEFT)
upgrade7.grid(row=2, column=2, sticky=N)

upgrade8 = Button(root, text="[{} Stück] Paula \n SPS: {} \nPreis: {:.1f} Sperms".format(sql.get_kind_amount(8), sql.get_kind_sps(8)*sql.get_kind_amount(8), sql.get_kind_price(8)), width=352, height=108, bg="blue",
                  command=lambda : buy(8,upgrade8,number,sps),image=paula_img, compound=LEFT)
upgrade8.grid(row=2, column=3, sticky=N)

upgrade9 = Button(root, text="[{} Stück] Emil \n SPS: {} \nPreis: {:.1f} Sperms".format(sql.get_kind_amount(9), sql.get_kind_sps(9)*sql.get_kind_amount(9), sql.get_kind_price(9)), width=352, height=108, bg="blue",
                  command=lambda : buy(9,upgrade9,number,sps),image=emil_img, compound=LEFT)
upgrade9.grid(row=3, column=0, sticky=N)

upgrade10 = Button(root, text="[{} Stück] Ida \n SPS: {} \nPreis: {:.1f} Sperms".format(sql.get_kind_amount(10), sql.get_kind_sps(10)*sql.get_kind_amount(10), sql.get_kind_price(10)), width=352, height=108, bg="blue",
                   command=lambda : buy(10,upgrade10,number,sps),image=ida_img, compound=LEFT)
upgrade10.grid(row=3, column=1, sticky=N)

upgrade11 = Button(root, text="[{} Stück] XÆA12 \n SPS: {} \nPreis: {:.1f} Sperms".format(sql.get_kind_amount(11), sql.get_kind_sps(11)*sql.get_kind_amount(11), sql.get_kind_price(11)), width=352, height=108, bg="blue",
                   command=lambda : buy(11,upgrade11,number,sps),image=XÆA12_img, compound=LEFT)
upgrade11.grid(row=3, column=2, sticky=N)

upgrade12 = Button(root, text="[{} Stück] ChadSchwaninger \n SPS: {} \nPreis: {:.1f} Sperms".format(sql.get_kind_amount(12), sql.get_kind_sps(12)*sql.get_kind_amount(12), sql.get_kind_price(12)), width=352, height=108, bg="blue",
                   command=lambda : buy(12,upgrade12,number,sps),image=ChadSchwaninger_img, compound=LEFT)
upgrade12.grid(row=3, column=3, sticky=N)

save = Button(root, text="SAVE+EXIT", width=50, height=7, bg="green", command=save)
save.grid(row=4, column=3, sticky=N)
load()
#load = Button(root, text="LOAD", width=50, height=7, bg="green", command=load)
#load.grid(row=0, column=3, sticky=N)

root.after(10, main)
root.state('zoomed')

while(True):
    root.update()
    time.sleep(0.1)
    number += sps/10
    main()
    label1.config(text="{:.1f} Sperm".format(number))
