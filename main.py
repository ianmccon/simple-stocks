from random import random, normalvariate
from datetime import datetime, timedelta
from math import pow
from operator import mul
import sys


stocks = {
    'TEA': {
        'type': 'Common',
        'last_dividend': 0,
        'fixed_dividend': 0.0,
        'par_value': 100,
        'price': 100
    },
    'POP': {
        'type': 'Common',
        'last_dividend': 8,
        'fixed_dividend': 0.0,
        'par_value': 100,
        'price': 100
    },
    'ALE': {
        'type': 'Common',
        'last_dividend': 23,
        'fixed_dividend': 0.0,
        'par_value': 60,
        'price': 60
    },
    'GIN': {
        'type': 'Preferred',
        'last_dividend': 8,
        'fixed_dividend': 0.02,
        'par_value': 100,
        'price': 100
    },
    'JOE': {
        'type': 'Common',
        'last_dividend': 13,
        'fixed_dividend': 0.0,
        'par_value': 250,
        'price': 250
    }}

trades = {
    'TEA': [],
    'POP': [],
    'ALE': [],
    'GIN': [],
    'JOE': []
}


def cls(num=20):
    print "\n" * num


def record_trade(stock_name, no_shares, trade_type):
    price_change = normalvariate(random(), 10)
    price = stocks[stock_name]['price'] + price_change
    trades[stock_name].append({
        'timestamp': datetime.now(),
        'sale type': trade_type,
        'amount': no_shares,
        'price': round(price, 2)
    })
    stocks[stock_name]['price'] = round(price, 2)

    print trades


def trade_stock(stock_name):
    cls(num=2)

    y = True
    while y is True:
        print "The %s share price is %sp" % (stock_name, stocks[stock_name]['price'])
        shares_choice = raw_input("How many shares do you want to trade :")
        try:
            no_shares = int(shares_choice)
            y = False
        except ValueError:
            cls(num=2)
            print "Please enter a number"

    z = True
    while z is True:
        trade_choice = raw_input("Do you wish to buy or sell [b/s] :")
        if trade_choice == 'b':
            z = False
            trade_type = 'BUY'
        elif trade_choice == 's':
            z = False
            trade_type = 'SELL'
        else:
            cls(num=2)
            print "please enter [b/s] :"

    record_trade(stock_name, no_shares, trade_type)


def dividend_yield(stock_name):
    if stocks[stock_name]['type'] == 'Common':
        return "Dividend yield for %s is %s" % (stock_name, stocks[stock_name]['last_dividend'] / stocks[stock_name]['price'])
    else:
        return "Dividend yield for %s is %s" % (stock_name, stocks[stock_name]['fixed_dividend'] * stocks[stock_name]['par_value'] / stocks[stock_name]['price'])

def pe_ratio(stock_name):
    return "P/E ratio for %s is %s" % (stock_name, stocks[stock_name]["price"] / stocks[stock_name]["last_dividend"] if stocks[stock_name]["last_dividend"] else "None")

def stock_price(stock_name):
    start_time = datetime.now() - timedelta(minutes=15)
    recent_trades = [x for x in trades[stock_name] if x['timestamp'] > start_time]

    sum_values = sum(map(lambda x: float(x['amount']) * x['price'], recent_trades))
    sum_amount = sum(map(lambda x: float(x['amount']), recent_trades))
    try:
        return "The stock price for %s is %s" % (stock_name, round(sum_values / sum_amount, 2))
    except ZeroDivisionError:
        return "Please make some trades first"


def calculate_all_share_index():
    prices = map(lambda x: x["price"], stocks.values())
    product = reduce(mul, prices)
    return "GBCE All Share Index: %s" % pow(product, 1 / float(len(stocks.values())))


def trading_menu(stock_name, stock):
    x = True
    while x is True:
        cls(num=2)
        print 30 * '-'
        print "   TRADE  %s STOCK" % stock_name
        print 30 * '-'
        print "1. Calculate the dividend yield"
        print "2. Calculate the P/E Ratio"
        print "3. Record a trade"
        print "4. Calculate Stock Price"
        print '5. Back to main menu...'
        print 30 * '-'

        choice = raw_input('Enter your choice [1-5] : ')
        choice = int(choice)

        if choice == 1:
            cls(num=2)
            print dividend_yield(stock_name)
        elif choice == 2:
            cls(num=2)
            print pe_ratio(stock_name)
        elif choice == 3:
            cls(num=2)
            trade_stock(stock_name)
        elif choice == 4:
            cls(num=2)
            print stock_price(stock_name)
        elif choice == 5:
            x = False
            cls(num=2)
            main_menu()
        else:
            print "Invalid number. Try again..."


def main_menu():
    choice = True
    while choice is True:
        print 30 * '-'
        print "   MAIN - MENU"
        print 30 * '-'
        print "1. TEA"
        print "2. POP"
        print "3. ALE"
        print "4. GIN"
        print "5. JOE"
        print "6. Calculate the GBCE All Share Index"
        print "7. QUIT"
        print 30 * '-'

        stock_choice = raw_input("Which stock do you want to trade [1-5] :")
        stock_choice = int(stock_choice)

        if stock_choice == 1:
            choice = False
            stock = stocks['TEA']
            stock_name = 'TEA'
            trading_menu(stock_name, stock)
        elif stock_choice == 2:
            choice = False
            stock = stocks['POP']
            stock_name = 'POP'
            trading_menu(stock_name, stock)
        elif stock_choice == 3:
            choice = False
            stock = stocks['ALE']
            stock_name = 'ALE'
            trading_menu(stock_name, stock)
        elif stock_choice == 4:
            choice = False
            stock = stocks['GIN']
            stock_name = 'GIN'
            trading_menu(stock_name, stock)
        elif stock_choice == 5:
            choice = False
            stock = stocks['JOE']
            stock_name = 'JOE'
            trading_menu(stock_name, stock)
        elif stock_choice == 6:
            choice = False
            print calculate_all_share_index()
        elif stock_choice == 7:
            choice = True
            sys.exit()
        else:
            cls()
            print "Please make a valid selection "


main_menu()

