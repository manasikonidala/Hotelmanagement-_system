import random
import tkinter

from tkinter import *
from functools import partial

from tabulate import tabulate

class Manager():


    def mainmenu(food,main_menu_list=[]):
        key=list(food.keys())
        n=len(food)
        for i in range(0,n):
            s_no=(i+1)
            fd=key[i]
            price=food[fd][0]
            quant=food[fd][1]
            row=[s_no,fd,price,quant]
            main_menu_list.append(row)
        emp_row=['','','','']
        main_menu_list.append(emp_row)
        return main_menu_list

    def specialmenu(food,no_of_dishes,special_menu_list=[]):
        food_dup=food
        key=list(food_dup.keys())
        n=len(food_dup)
        for i in range(0,no_of_dishes):
            j=random.randint(0,n-1)
            n-=1
            s_no=(i+1)
            fd=key[j]
            price=food_dup[fd][0]
            quant=food_dup[fd][1]
            row=[s_no,fd,price,quant]
            special_menu_list.append(row)
            del(food_dup[fd])
            del(key[j])
        emp_row=['','','','']
        special_menu_list.append(emp_row)
        return special_menu_list

    def menu_manager(main_menu_list,special_menu_list):
        print("Main Menu:")
        print()
        head=['S.No','Name','Price','Quantity']
        print(tabulate(main_menu_list, headers=head, tablefmt="pretty"))
        print()

        print("Today's Special Menu:")
        print()
        head=['S.No','Name','Price','Quantity']
        print(tabulate(special_menu_list, headers=head, tablefmt="pretty"))
        print()
        inp=input("Do you want to change anything in today's special menu?(y/n): ")
        if inp=='y':
            while True:
                print()
                inp=input("Enter the dish's name you would like to change: ")
                j=None
                for i in special_menu_list:
                    if i[1]==inp:
                        j = input("\nEnter the new dish's name: ")
                        i[1] = j
                        i[2] = int(input("Enter the price of the new dish: "))
                        i[3] = int(input("Enter the available quantity of the new dish: "))
                        print("\nThe New Menu:")
                        print()
                        print(tabulate(special_menu_list, headers=head, tablefmt="pretty"))
                        print()
                if j==None:
                    print("\nThe dish is not in today's special menu.Please enter a valid dish name!!")
                else:
                    inp1=input("Are you satisfied with the menu?(y/n): ")
                    if inp1=='y':
                        break
                    else:
                        continue


class Client():
    
    def menu_client(main_menu_list,special_menu_list):
        head=['S.No','Name','Price']

        c_main_menu_list=[]
        for i in main_menu_list:
            j=[i[0],i[1],i[2]]
            c_main_menu_list.append(j)
        print("Main Menu:")
        print()
        print(tabulate(c_main_menu_list, headers=head, tablefmt="pretty"))
        print()

        c_special_menu_list=[]
        for i in special_menu_list:
            j=[i[0],i[1],i[2]]
            c_special_menu_list.append(j)
        print("Today's Special Menu:")
        print()
        print(tabulate(c_special_menu_list, headers=head, tablefmt="pretty"))
        print()


                    
    def ordr(main_menu_list,special_menu_list):
        order=[]
        sno=0
        total1=0
        while True:
            inp=input("Enter the dish name you would like to order: ")
            for i in range(len(main_menu_list)):
                found=0
                if main_menu_list[i][1]==inp:
                    sno+=1
                    qua=int(input("Enter the quantity of the dish you would like to order: "))
                    print()
                    quacheck=main_menu_list[i][3]
                    if qua<=quacheck and main_menu_list[i][3]-qua>0:
                        found+=1
                        main_menu_list[i][3]-=qua
                        pri=main_menu_list[i][2]
                        price=pri*qua
                        total1+=price
                        dish=main_menu_list[i][1]
                        row=[sno,dish,qua,price]
                        order.append(row)
                        break
                    else:
                        print("The quantity of the food is limited and yours exceeds the limit!!\nPlease order another dish or the same dish with lesser quantity.\n")

            if found==0:
                for i in range(len(special_menu_list)):
                    found=0
                    if special_menu_list[i][1]==inp:
                        sno+=1
                        qua=int(input("Enter the quantity of the dish you would like to order: "))
                        print()
                        quacheck=special_menu_list[i][3]
                        if qua<=quacheck and special_menu_list[i][3]-qua>0:
                            found+=1
                            special_menu_list[i][3]-=qua
                            pri=special_menu_list[i][2]
                            price=pri*qua
                            total1+=price
                            dish=special_menu_list[i][1]
                            row=[sno,dish,qua,price]
                            order.append(row)
                            break
                        else:
                            print("The quantity of the food is limited and yours exceeds the limit!!\nPlease order another dish or the same dish with lesser quantity.\n")

            if found==0:
                print("The dish is not there in today's Menu.\n")
                    
            inp1=input("Would you like to order anything else?(y/n): ")
            print()
            if inp1=='y'or inp1=='Y':
                continue
            else:
                row1=['','','','']
                row2=['','','Total amount =',total1]
                order.append(row1)
                order.append(row2)
                break

        return order

class Bill():
    def bill(order):
        head=['S.No','Name','Quantity','Price']
        print(tabulate(order, headers=head, tablefmt="pretty"))
        print()

class Payment():
    def payment(order):
        root = Tk()
        root.geometry('480x300')
        root.title('Bill')
        OPTIONS = [
            "1",
            "2",
            "3",
            "4"
        ]

        variable = StringVar(root)
        variable.set(OPTIONS[0])  # default value
        label1 = Label(root, text=" Payment ").grid(row=0, column=0)
        label2 = Label(root,
                       text="-------------------------------------------------------------------------------------------------").grid(
            row=1, column=0)
        label3 = Label(root, text=" MODE OF PAYMENT ").grid(row=2, column=0)
        label4 = Label(root, text=" 1-Credit/Debit card ").grid(row=3, column=0)
        label5 = Label(root, text=" 2-Phonepay/Paytm ").grid(row=4, column=0)
        label6 = Label(root, text=" 3-Using UPI ").grid(row=5, column=0)
        label7 = Label(root, text=" 4-Payment through cash ").grid(row=6, column=0)
        label8 = Label(root, text="Enter your payment method").grid(row=7, column=0)

        w = OptionMenu(root, variable, *OPTIONS).grid(row=8, column=0)

        def ok():
            Label(root, text=" We hope you had a good experience ").grid(row=11, column=0)
            Label(root, text=" Thanks for ordering with us ").grid(row=10, column=0)

        button = Button(root, text="OK", command=ok).grid(row=9, column=0)
        mainloop()


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Order():

    def __init__(self):
        self.head = None

    def __str__(self):
        pval = self.head
        p='Order number from latest to oldest  -->  [  '
        while pval is not None:
            val=pval.data
            if (len(val[1]))-1>=3:
                p+=str(val[0])+'  '
            else:
                p+=str(val[0])+'  '
            pval = pval.next
        p+=']'
        return p + '\n'
            
    def insert(self,item):
        newitem = Node(item) 
        newitem.next = self.head
        self.head = newitem

    def find(self, item):
        head = self.head
        val= head.data
        value=val[0]
        pos=0
        if head is not None:
            if value == item:
                self.head = head.next
                head = None
                print("Position of order "+str(item)+" is: 1")
                print("\nThe order's bill:\n")
                Bill.bill(val[1])
                return ''
        while head is not None:
            pos+=1
            val= head.data
            value=val[0]
            if value == item:
                print("Position of order "+str(item)+" is: ",pos)
                print("\nThe order's bill:\n")
                Bill.bill(val[1])
                print()
                break
            prev = head
            head = head.next
        if head == None:
            print("Order not in the list!!\n")
            return

        reins = head.data
        prev.next = head.next
        head = None
        self.insert(reins)

    def delete(self,item):
        head = self.head
        val= head.data
        value=val[0]
        if head is not None:
            if value==item:
                self.head = head.next
                head = None
                return
        while head is not None:
            val= head.data
            value=val[0]
            if value==item:
                break
            prev = head
            head = head.next
        if head == None:
            return
        prev.next = head.next
        head = None




#main program---------------------------------------------------------------------------------------------------------------------------------

def validate(ep,cp):
    if ep.get()=='user' and cp.get()=='2003':
        Label(root,text="Confirmed").grid(row=5,column=1)
        soup = {'Chicken clear soup': [120, 50], 'Tom yum soup': [200, 40], 'Tomato soup': [250, 50], 'Hot and sour soup': [150, 50]}
        starter = {'Paneer Manchurian': [120, 50], 'Crispy baby corn': [200, 40], 'Chicken 65': [250, 50], 'Crispy Vegetables': [150, 50]}
        main_dish = {'Schezhwan Noodles': [120, 50], 'Spicy Chicken Fried Rice': [200, 40], 'Mushroom Hakka Noodles': [250, 50],
                     'Chinese Chopsuey': [150, 50]}
        desert = {'Gulab Jamun': [120, 50], 'Rasmalai': [200, 40], 'Shrikhand': [250, 50], 'Fruit salad': [150, 50]}

        sp_soup = {'Sweet Corn Vegetable soup': [120, 50], 'Mushroom soup': [200, 40], 'Veg. Noodle soup': [250, 50], 'Lemon Coriander soup': [150, 50]}
        sp_starter = {'Veg. in Schezwan Sauce': [120, 50], 'Paneer chilly': [200, 40], 'Vegetable Sizzler': [250, 50], 'Wonton in Garlic Sauce': [150, 50]}
        sp_main_dish = {'Veg Stir Fied noodles': [120, 50], 'Chicken Dum Biryani': [200, 40], 'Mutton Dum Biryani': [250, 50],
                        'Spinach fried rice': [150, 50]}
        sp_desert = {'Angoori rabdi': [120, 50], 'Matka Firni': [200, 40], 'Gulab Jamun with ice cream': [250, 50], 'Mewar kulfi': [150, 50]}

        main_menu_list = Manager.mainmenu(desert, Manager.mainmenu(main_dish,
                                                                   Manager.mainmenu(starter, Manager.mainmenu(soup))))
        special_menu_list = Manager.specialmenu(sp_desert, 2, Manager.specialmenu(sp_main_dish, 4,
                                                                                  Manager.specialmenu(sp_starter, 3,
                                                                                                      Manager.specialmenu(
                                                                                                          sp_soup, 2))))
        print("Manager's Side:\n")
        Manager.menu_manager(main_menu_list, special_menu_list)
        print()
        Orders = Order()
        order_no = 1

        while True:
            print("\nClient's Side:\n")
            print("\nWelcome to Kamat Restaurant!!\n")
            Client.menu_client(main_menu_list, special_menu_list)
            data = Client.ordr(main_menu_list, special_menu_list)

            print("\nOrder Bill:\n")
            Bill.bill(data)
            print("\nPayment:\n")
            Payment.payment(data)
            print()
            print("\nThank you for ordering at Madhu's Restaurant!!\n")
            order = [order_no, data]
            Orders.insert(order)

            close = input("\nDo you want to close the restaurant?(y/n): ")
            if close != 'y':
                order_no += 1
                continue
            else:
                break



    else:
        Label(root,text="invalid").grid(row=5,column=1)

root=Tk()
root.geometry('280x200')
root.title('Login')
label1=Label(root,text="Username: ").grid(row=0, column=0)
ep=StringVar()
dishentry=Entry(root,textvariable=ep).grid(row=0,column=1)
label2=Label(root,text="password: ").grid(row=1, column=0)
cp=StringVar()
dishentry=Entry(root,textvariable=cp,show="*").grid(row=1,column=1)

validate=partial(validate,ep,cp)
check=Button(root,text="Check",command=validate).grid(row=4,column=2)
root.mainloop()
