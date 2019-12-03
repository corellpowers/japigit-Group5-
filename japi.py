"""
Purpose: PD 5
Filename:japi.py
Author: Group 5: Dakota Powers, Corell Powers, Nolan Flatt
Topic: PD 5: API and JSON
Description: Use python and json to print specific api information
"""
import urllib.request
import json

KEY = '&apikey=26GYZPNELHM7E6YW'
FUNCTION = 'function=GLOBAL_QUOTE&'
x = 0


def getStockData(func, symbol, key):
    full_url = 'https://www.alphavantage.co/query?'
    con = urllib.request.urlopen(full_url + func + symbol + key)
    res = con.read().decode()
    print(res)
    x = json.loads(res)
    return x['Global Quote']['05. price']


def main():
    f = open("japi.out", "w+")
    while x != 1:
        entry = input("Enter a stock symbol to check the quote: ")
        symbol = 'symbol=' + entry
        if symbol == 'symbol=quit':
            break
        else:
            f.write("The current price of {} is: ${:.2f}\r\n".format(entry, float(getStockData(FUNCTION, symbol, KEY))))
    f.close()
    f = open("japi.out", "r")
    contents = f.read()
    print(contents)

print("Stock Quotes retrieved successfully!")
main()
master version
