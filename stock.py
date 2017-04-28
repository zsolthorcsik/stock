# Let's win the stock exchange competition with this program
from tkinter import  *
from tkinter import messagebox
import random
money = 100
class User:
    def __init__(self, passmoney):
        self.m = passmoney
    def plus_1(self, passmoney):
        self.m = self.m

class Stock:



    def __init__(self):
        pass
    # CREATES A NEW STOCK
    def newstock(self, price, stock_book):

        stock_book = stock_book
        num = len(stock_book)
        numa = num+1
        you_have_book.update({})
        #Now let's create randomnumbers
        r1 = random.randrange(0, 100)
        r1 -= 50

        r3 = random.randrange(0, 100)
        stock_book[num+1] = {'price': r1+100, 'risk':r3, 'name': "Stock%d" % numa}
        you_have_book.update({stock_book[num + 1]['name']: 0})
        button_book[num+1] = {'buybutton': Button(root, text="Buy", command= lambda num1=num+1:Stock.buy_stock(self,num1)), 'sellbutton': Button(root, text="Sell", command=lambda num2=num+1:Stock.sell_stock(self, num2))}
        button_book[num+1]['buybutton'].grid(row=num+1, column=3)
        button_book[num+1]['sellbutton'].grid(row=num+1, column=4)
        label_book[num+1] = {'namelabel': Label(root, text=stock_book[num+1]['name']), 'pricelabel': Label(root, text=stock_book[num+1]['price']), 'enteramount': Entry(root), 'youhave': Label(root, text="You have %d" % you_have_book[stock_book[num+1]['name']])}
        label_book[num+1]['namelabel'].grid(row=num+1, column=0)
        label_book[num+1]['pricelabel'].grid(row=num+1, column=1)
        label_book[num+1]['enteramount'].grid(row=num+1, column=2)
        label_book[num+1]['youhave'].grid(row=num+1, column=5)
        messagebox.showinfo("IPO announced", "Trading has began on the stock exchange with %s, at a price of %d, and a risk factor of %d" %  (stock_book[num+1]['name'], stock_book[num+1]['price'], stock_book[num+1]['risk']) )
        print(you_have_book)

    #Let's jump to the next time

    def next_round(self, stock_book, button_book):
        stock_book = stock_book
        num = len(stock_book)
        if 0 < num <= 10:
            r4 = random.randrange(60, 100)
        elif num == 0:
            r4=100
        elif 10 <= num < 20:
            r4 = random.randrange(0, 100)
        else:
            r4 = 0

        if r4 > 80:
            new_stock()

        for x in range(1, num+1):
            r1 = random.randrange(1, 101)
            r1 = r1 - 50
            r1 = r1/1000
            r2 = random.randrange(-50, 50)
            r2 /= 100
            stock_book[x]['price'] = stock_book[x]['price']  + ((stock_book[x]['risk']/10)*r2)
            stock_book[x]['price'] = round(stock_book[x]['price'], 2)
            label_book[x]['pricelabel'].config(text=stock_book[x]['price'])


    #THIS IS GONNA BE FOR BUYING STOCKS
    def buy_stock(self, n):
        amount = label_book[n]['enteramount'].get()
        amount = int(amount)
        price = stock_book[n]['price']
        if me.m > amount * price:
            me.m = me.m - price * amount
            moneylabel.config(text="You have %d" % me.m)
            you_have_book[stock_book[n]['name']] = you_have_book[stock_book[n]['name']] + amount
            label_book[n]['youhave'].config(text="You have %d" % you_have_book[stock_book[n]['name']])

        else:
           messagebox.showinfo("Insufficient funds",
                               'Sorry, you do not have enough money to purschace the given amount of securities')


    def sell_stock(self, n):
        amount = label_book[n]['enteramount'].get()
        amount = int(amount)
        price = stock_book[n]['price']
        if amount <= you_have_book[stock_book[n]['name']]:
            you_have_book[stock_book[n]['name']] = you_have_book[stock_book[n]['name']] - amount
            label_book[n]['youhave'].config(text="You have %d" % you_have_book[stock_book[n]['name']])
            me.m += amount * price
            moneylabel.config(text="You have %d" % me.m)
        else:
            messagebox.showinfo("You do not have enough stocks",
                                'Sorry, you do not have enough stock and currently shorting is not supported')

x = Stock()
stock_book = {}
button_book = {}
button_push = {}
label_book = {}
you_have_book = {}
money = 10000
me = User(money)
root = Tk()
root.wm_title("Stock trader")
def next_round():
    me.plus_1(me.m)
    moneylabel.config(text="You have %s" % me.m)
    Stock.next_round(money, stock_book, button_book)
def new_stock():
    x = 1
    Stock.newstock(x, 100+x, stock_book)
    print(stock_book)






#GUIGUIGUIGUIGUI
moneylabel = Label(root, text="You have %s" % money)
moneylabel.grid(row=0, column=1)
next_round_button = Button(root, text="Next round", command=next_round)
next_round_button.grid(row=0, column=2)
next_stock_button = Button(root, text="Next stock", command=new_stock)
#next_stock_button.grid(row=0, column=3)
root.mainloop()








