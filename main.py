#!/usr/bin/env python3
#udah gua fix hmm

import os;
from time import sleep;

#column = int(os.system("stty size|cut -d' ' -f2"))
print("=" * 50)
print("\033[1;36mhi, welcome ngab\033[m".center(62))
print("=" * 50 + "\n")
print("menu\n".center(50))
print("1. cashier")
print("2. calculator")
print("3. list price")
print("0. quit")

a = str()
b = int()
sleep(1)


pilihan = int(input("\nchoose menu: "))

def cashier():
    print("="* 50)
    print("\033[1;36mcashier menu\033[m".center(62))
    print("=" * 50 + "\n")
    print()
    sleep(1)
    item = str(input("enter item name: "))
    item_total = int(input("enter item amount: "))
    give_money = int(input("pay: "))
    try:
	    data_item = {
		#masukan data sperti bawah
                #rokok
        	"djarum super btng":2000,
		}

    except:
        print("\nItem", item, "currently unavailable!")

    price = (data_item[item.lower()] * item_total)
    money_back = (give_money - price)
    kurang = (price - give_money)
    print("-" * 50)
    print("item name: ", item)
    print("item amount: ", item_total)
    print("money:", give_money, "idr")
    print("total item price: ", price, "idr")
    print("\ncounting the change...\n")
    sleep(3)

    if give_money > price:
        print(f"money back: ", money_back, "idr")
        counter_cashier()

    elif give_money == price:
        print('uang anda pas, terimakasih telah berbelanja ')
        counter_cashier()

    else:
        print(f'maaf uang anda tidak cukup, uang anda kurang {kurang}')
        cashier()

def counter_cashier():
	counter = input("back to cashier menu? (y/n): ")
	if counter == "y":
		cashier()
	elif counter == "n":
		print("program exited")
		exit()


def calculator():
	print("="* 50)
	print("\033[1;36mcalculator menu\033[m".center(62))
	print("=" * 50 + "\n")
	print()
	sleep(1)
	first_number = int(input("enter first number: "))
	two_number = int(input("enter two number: "))
	operator = str(input("choose operator (+ - * /): "))
	hasil = 0

	if operator == "+":
		hasil = first_number+two_number
	elif operator == "-":
		hasil = first_number-two_number
	elif operator == "*":
		hasil = first_number*two_number
	elif operator == "/":
		hasil = first_number/two_number
	else:
		print("undefine operator")

	print("\ncounting...\n")
	sleep(3)
	print("hasil: ", hasil)
	counter_calculator()

def counter_calculator():
	counter = input("back to calculator menu? (y/n): ")
	if counter == "y":
		calculator()
	elif counter == "n":
		print("program exited")
		exit()

def list_price():
	print("="* 50)
	print("\033[1;36mlist price menu\033[m".center(62))
	print("=" * 50 + "\n")
	print()
	sleep(1)
	item_search =str(input("search item: "))
	try:
		data = {
                #masukan data sperti bawah
                #rokok
        	"djarum super btng":2000,
		}
		
	except:
		print("\nitem", item_search, "currently unavailable!")

	sleep(1)
	print("-" * 50)
	print("item name: ", item_search)
	print("price: ", data[item_search.lower()])
	counter_list_price()
	
def counter_list_price():
	counter = input(str("back to list price menu? (y/n): "))
	if counter == "y":
		list_price()
	elif counter == "n":
		print("program exited")
		exit()


if pilihan == int(1):
    cashier()
    exit()
elif pilihan == int(2):
    calculator()
    exit()
elif pilihan == int(3):
	list_price()
	exit()
else:
    print("exited")
    exit(0)
