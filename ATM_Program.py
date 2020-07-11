#program insert money machine
#code by Singgih Febriana @July 12 2020 03:02 am
import time
import sys

money=[ ]

#insert_money_Program

def insert_money():
    a=input("how much do your money to add ?")
    x=int(a)
    money.append(x)
    print("succesfully add...",(sum(money)))
    time.sleep(2)
    menu()

#Transfer_Program

def transfermoney():
    x=input("how much do your money transfer ?")
    money_transfer=int(x)
    transfer=(sum(money)-money_transfer)
    money.clear()
    money.append(transfer)

    print("succesfully transfer...",sum(money))
    time.sleep(2)
    menu()

#Checksaldo_Program

def checksaldo():
    if (len(money))>=1:
        time.sleep(2)
        print("\nyour money is $",sum(money))
        time.sleep(1)
        menu()
    else:
        time.sleep(2)
        print("\nyour money is empty")
        time.sleep(1)
        menu()

#Menu_options_program

def menu():
    print("\nMenu check saldo (press 1)\nMenu transfer (press 2)\nMenu insert money (press 3)\nMenu exit (press 4)")
    request_menu=input("\npress number for request ?")
    int_requestmenu=int(request_menu)
    if int_requestmenu==1:
        checksaldo()
    elif int_requestmenu==2:
        transfermoney()
    elif int_requestmenu==3:
        insert_money()
    elif int_requestmenu==4:
        sys.exit()

#password_program

def password():

    asking=input("insert your ATM pin ?")

    x=int(asking)

    if (x==123):
        print("your pin is correct\n")
        time.sleep(2)
        menu()
    elif(x!=123):
        print("your pin is wrong\n")
        asking2=input("do you want to exit ? yes/ no")
        answr="yes"
        if (asking2==answr):
            sys.exit()
            time.sleep(5)






