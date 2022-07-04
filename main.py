import time
from tkinter import *
import sql

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

def check_price_for_upgrade(kind,button):
    global number
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
        label1.config(text=str(number) + " Sperm")
    else:
        label1.config(text=str(number) + " Sperms")

    print("Loaded")
    main()
def sps():
    print("SPS")
    #global number
    #global sps
    #print(sps)
    #number += sps
    #label1.config(text=str(number) + " Sperms")

def click():
    global number
    number += 1

    if(number == 1):
        label1.config(text=str(number) + " Sperm")
    else:
        label1.config(text=str(number) + " Sperms")
    main()


#         ██████╗ ██╗   ██╗██╗
#        ██╔════╝ ██║   ██║██║
#        ██║  ███╗██║   ██║██║
#        ██║   ██║██║   ██║██║
#        ╚██████╔╝╚██████╔╝██║
#         ╚═════╝  ╚═════╝ ╚═╝

#checks if database is available
sql.main()

#sets screensize and title
root.geometry("1536x864")
root.title("SchwanniClick")

# Main click button
clickButton = Button(root, text="CUM", command=lambda: click(), width=50, height=20, bg="red")
clickButton.grid(row=0, column=0, sticky=EW)
#clickButton.place(x=0, y=20)
#clickButton.pack(fill='y', side='left')

# upgrades
upgrade1 = Button(root, text="Upgrade 1", width=50, height=7, bg="blue")
upgrade1.grid(row=1, column=0, sticky=N)

upgrade2 = Button(root, text="Upgrade 2", width=50, height=7, bg="blue")
upgrade2.grid(row=1, column=1, sticky=N)

upgrade3 = Button(root, text="Upgrade 3", width=50, height=7, bg="blue")
upgrade3.grid(row=1, column=2, sticky=N)

upgrade4 = Button(root, text="Upgrade 4", width=50, height=7, bg="blue")
upgrade4.grid(row=1, column=3, sticky=N)

upgrade5 = Button(root, text="Upgrade 5", width=50, height=7, bg="blue")
upgrade5.grid(row=2, column=0, sticky=N)

upgrade6 = Button(root, text="Upgrade 6", width=50, height=7, bg="blue")
upgrade6.grid(row=2, column=1, sticky=N)

upgrade7 = Button(root, text="Upgrade 7", width=50, height=7, bg="blue")
upgrade7.grid(row=2, column=2, sticky=N)

upgrade8 = Button(root, text="Upgrade 8", width=50, height=7, bg="blue")
upgrade8.grid(row=2, column=3, sticky=N)

upgrade9 = Button(root, text="Upgrade 9", width=50, height=7, bg="blue")
upgrade9.grid(row=3, column=0, sticky=N)

upgrade10 = Button(root, text="Upgrade 10", width=50, height=7, bg="blue")
upgrade10.grid(row=3, column=1, sticky=N)

upgrade11 = Button(root, text="Upgrade 11", width=50, height=7, bg="blue")
upgrade11.grid(row=3, column=2, sticky=N)

upgrade12 = Button(root, text="Upgrade 12", width=50, height=7, bg="blue")
upgrade12.grid(row=3, column=3, sticky=N)

save = Button(root, text="SAVE", width=50, height=7, bg="green", command=save)
save.grid(row=4, column=3, sticky=N)
load()
#load = Button(root, text="LOAD", width=50, height=7, bg="green", command=load)
#load.grid(row=0, column=3, sticky=N)

root.after(10, main)
#root.after(1000, sps)
root.state('zoomed')

while(True):
    root.mainloop()

