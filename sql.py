'''
Current Functions:
create_table() -> creates whole database
get_kind_price(numberOfKind) -> gets price of an upgrade
'''

import sqlite3
import math
from os.path import exists


#  ██████╗██████╗ ███████╗ █████╗ ████████╗███████╗
# ██╔════╝██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██╔════╝
# ██║     ██████╔╝█████╗  ███████║   ██║   █████╗
# ██║     ██╔══██╗██╔══╝  ██╔══██║   ██║   ██╔══╝
# ╚██████╗██║  ██║███████╗██║  ██║   ██║   ███████╗
#  ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝

def create_table():
    print("Create new database")
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()

    # create main table
    conn.execute("CREATE TABLE IF NOT EXISTS main("
                 "sperms NUMERIC NOT NULL, "
                 "spermspersec NUMERIC NOT NULL, "
                 "prestige INTEGER NOT NULL)")
    # insert default values into main table
    conn.execute("INSERT INTO main(sperms, spermspersec, prestige) VALUES(0, 0, 0)")

    # create upgrades table
    for i in range(1, 13):
        price = math.pow(i, 6)
        sps = ((math.sqrt(price)) / 2) * (i / 2)
        conn.execute("CREATE TABLE IF NOT EXISTS kind" + str(i) +
                     "(amount INTEGER NOT NULL, "
                     "price NUMERIC NOT NULL, "
                     "spermspersec NUMERIC NOT NULL)")
        conn.execute('INSERT INTO kind' + str(i) + " VALUES(0, " + str(price) + ", " + str(sps) + ")")

    conn.commit()
    conn.close()


#        ██████╗ ███████╗████████╗
#       ██╔════╝ ██╔════╝╚══██╔══╝
#       ██║  ███╗█████╗     ██║
#       ██║   ██║██╔══╝     ██║
#       ╚██████╔╝███████╗   ██║
#        ╚═════╝ ╚══════╝   ╚═╝

def get_kind_price(numberOfKind):
    ret = None
    conn = sqlite3.connect('data.db')

    cursor = conn.execute("SELECT price FROM kind" + str(numberOfKind))
    for row in cursor:
        ret = row[0]

    conn.commit()
    conn.close()

    return ret


def get_kind_sps(numberOfKind):
    ret = None
    conn = sqlite3.connect('data.db')

    cursor = conn.execute("SELECT spermspersec FROM kind" + str(numberOfKind))
    for row in cursor:
        ret = row[0]

    conn.commit()
    conn.close()

    return ret


def get_kind_amount(numberOfKind):
    ret = None
    conn = sqlite3.connect('data.db')

    cursor = conn.execute("SELECT amount FROM kind" + str(numberOfKind))
    for row in cursor:
        ret = row[0]

    conn.commit()
    conn.close()

    return ret


def get_main_sperms():
    ret = None
    conn = sqlite3.connect('data.db')

    cursor = conn.execute("SELECT sperms FROM main")
    for row in cursor:
        ret = row[0]

    conn.commit()
    conn.close()

    return ret


def get_main_sps():
    ret = None
    conn = sqlite3.connect('data.db')

    cursor = conn.execute("SELECT spermspersec FROM main")
    for row in cursor:
        ret = row[0]

    conn.commit()
    conn.close()

    return ret


def get_main_prestige():
    ret = None
    conn = sqlite3.connect('data.db')

    cursor = conn.execute("SELECT prestige FROM main")
    for row in cursor:
        ret = row[0]

    conn.commit()
    conn.close()

    return ret


#       ███████╗███████╗████████╗
#       ██╔════╝██╔════╝╚══██╔══╝
#       ███████╗█████╗     ██║
#       ╚════██║██╔══╝     ██║
#       ███████║███████╗   ██║
#       ╚══════╝╚══════╝   ╚═╝

def set_kind_amount(numberOfKind,amount):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()

    conn.execute("UPDATE kind" + str(numberOfKind) + " SET amount = " + str(amount))

    conn.commit()


def set_kind_price(numberOfKind,price):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()

    conn.execute("UPDATE kind" + str(numberOfKind) + " SET price = " + str(price))

    conn.commit()


def set_main_sperms(sperms):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()

    conn.execute("UPDATE main SET sperms = " + str(sperms))

    conn.commit()


def set_main_sps(sps):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()

    conn.execute("UPDATE main SET spermspersec = " + str(sps))

    conn.commit()


def set_main_prestige(prestige):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()

    conn.execute("UPDATE main SET prestige = " + str(prestige))

    conn.commit()


#        ███╗   ███╗ █████╗ ██╗███╗   ██╗
#        ████╗ ████║██╔══██╗██║████╗  ██║
#        ██╔████╔██║███████║██║██╔██╗ ██║
#        ██║╚██╔╝██║██╔══██║██║██║╚██╗██║
#        ██║ ╚═╝ ██║██║  ██║██║██║ ╚████║
#        ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝

def main():
    # if database does not exist build it
    if exists('data.db') == False:
        create_table()