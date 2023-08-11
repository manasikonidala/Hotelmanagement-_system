import streamlit as st
import pandas as pd
import threading
import csv, random
import pandas as pd
import tabulate

class Manager:
    def mainmenu(food,main_menu_list=[]):
        key=list(food.keys())
        n=len(food)
        for i in range(0,n):
            fd=key[i]
            price=food[fd][0]
            quant=food[fd][1]
            row=[fd,price,quant]
            main_menu_list.append(row) 
        return main_menu_list

    def specialmenu(food,no_of_dishes,special_menu_list=[]):
        food_dup=food
        key=list(food_dup.keys())
        n=len(food_dup)
        for i in range(0,no_of_dishes):
            j=random.randint(0,n-1)
            n-=1
            fd=key[j]
            price=food_dup[fd][0]
            quant=food_dup[fd][1]
            row=[fd,price,quant]
            special_menu_list.append(row)
            del(food_dup[fd])
            del(key[j])    
        return special_menu_list

    def writemain(main_menu_list):
        with open("mainmenu.csv","w") as f:
            writer=csv.writer(f)
            writer.writerow(['Name','Price','Quantity'])
            for i in main_menu_list:
                writer.writerow(i)
        f.close()

    def writespecial(special_menu_list):
        with open("specialmenu.csv","w") as f1:
            writer=csv.writer(f1)
            writer.writerow(['Name','Price','Quantity'])
            for i in special_menu_list:
                writer.writerow(i)
        f1.close()


class Order():

    def __init__(self):
        self.array = []
        self.length=0

            
    def insert(self,item):
        self.array.append(item)
        self.length+=1

    '''def find(self, item):
        for i in self.array:
            if i[0]==item:
                print()
                Bill.bill(i[1])
                break'''

    def delete(self):
        if self.length>=1:
            self.array.remove(self.array[0])
            self.length-=1

    def __len__(self):
        print()
        return 'The number of orders in queue: ',self.length

class TestThreading(object):

    def __init__(self, interval=1):
        self.interval = interval
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        order_no=1
        while True:
            data="run1()"
            order=[order_no,data]
            Order.insert(order)
            close=input("Were you happy with our service?(y/n):")
            if close=="y":
                print("We recommend you to share with us your feedback")
                """print("feedback")with link"""
            else:
                print("Please share with us your suggestions")
                """print(feedback)with link"""

            """Go back to manager home"""
            inp1=input("Would you like to take another order?(y/n): ")
            if inp1!='y':
                break
            else:
                order_no


        
soup={'soup_1':[120,50],'soup_2':[200,40],'soup_3':[250,50],'soup_4':[150,50]}
starter={'starter_1':[120,50],'starter_2':[200,40],'starter_3':[250,50],'starter_4':[150,50]}
main_dish={'main_dish_1':[120,50],'main_dish_2':[200,40],'main_dish_3':[250,50],'main_dish_4':[150,50]}
desert={'dessert_1':[120,50],'dessert_2':[200,40],'dessert_3':[250,50],'dessert_4':[150,50]}

sp_soup={'soup_1':[120,50],'soup_2':[200,40],'soup_3':[250,50],'soup_4':[150,50]}
sp_starter={'starter_1':[120,50],'starter_2':[200,40],'starter_3':[250,50],'starter_4':[150,50]}
sp_main_dish={'main_dish_1':[120,50],'main_dish_2':[200,40],'main_dish_3':[250,50],'main_dish_4':[150,50]}
sp_desert={'dessert_1':[120,50],'dessert_2':[200,40],'dessert_3':[250,50],'dessert_4':[150,50]}
main_menu_list=Manager.mainmenu(desert,Manager.mainmenu(main_dish,Manager.mainmenu(starter,Manager.mainmenu(soup))))
special_menu_list=Manager.specialmenu(sp_desert,2,Manager.specialmenu(sp_main_dish,4,Manager.specialmenu(sp_starter,3,Manager.specialmenu(sp_soup,2))))
Manager.writemain(main_menu_list)
Manager.writespecial(special_menu_list)

st.set_page_config(page_title="Welcome",page_icon=":wave:",layout="wide")

st.title("Welcome to Kamat Restaurant")
st.header("Login")
user=st.radio('Select:',('Customer','Manager'),key=1)
    
if (user=='Customer'):
    cusname=st.text_input("Enter name of customer",key=2)
    number=st.text_input("Enter phone number",key=3)
    address=st.text_input("Enter address",key=4)
    email=st.text_input("Enter mail",key=5)
    st.subheader("Order")
    df1=pd.read_csv("mainmenu.csv")
    l=df1.values.tolist()
    with open("bill.csv","w") as f:
        writer=csv.writer(f)
        writer.writerow(['Name','Quantity','Amount'])
        st.write('soup_1')
        level = st.text_input("Quantity:",value="0",key=6)
        for i in l:
            if i[0]=='soup_1':
                writer.writerow([i[0],i[1],level])
        st.write('soup_2')
        level1 = st.text_input("Quantity:",value="0",key=7)
        for i in l:
            if i[0]=='soup_2':
                writer.writerow([i[0],i[1],level1])
        st.write('soup_3')
        level2 = st.text_input("Quantity:",value="0",key=8)
        for i in l:
            if i[0]=='soup_3':
                writer.writerow([i[0],i[1],level2])
        st.write('soup_4')
        level3 = st.text_input("Quantity:",value="0",key=9)
        for i in l:
            if i[0]=='soup_4':
                writer.writerow([i[0],i[1],level3])
        st.write('starter_1')
        level4 = st.text_input("Quantity:",value="0",key=10)
        for i in l:
            if i[0]=='starter_1':
                writer.writerow([i[0],i[1],level4])
        st.write('starter_2')
        level5 = st.text_input("Quantity:",value="0",key=11)
        for i in l:
            if i[0]=='starter_2':
                writer.writerow([i[0],i[1],level5])
        st.write('starter_3')
        level6 = st.text_input("Quantity:",value="0",key=12)
        for i in l:
            if i[0]=='starter_3':
                writer.writerow([i[0],i[1],level6])
        st.write('starter_4')
        level7 = st.text_input("Quantity:",value="0",key=13)
        for i in l:
            if i[0]=='starter_4':
                writer.writerow([i[0],i[1],level7])
        st.write('main_dish_1')
        level8 = st.text_input("Quantity:",value="0",key=14)
        for i in l:
            if i[0]=='main_dish_1':
                writer.writerow([i[0],i[1],level8])
        st.write('main_dish_2')
        level9 = st.text_input("Quantity:",value="0",key=15)
        for i in l:
            if i[0]=='main_dish_2':
                writer.writerow([i[0],i[1],level9])
        st.write('main_dish_3')
        level10 = st.text_input("Quantity:",value="0",key=16)
        for i in l:
            if i[0]=='main_dish_3':
                writer.writerow([i[0],i[1],level10])
        st.write('main_dish_4')
        level11 = st.text_input("Quantity:",value="0",key=17)
        for i in l:
            if i[0]=='main_dish_4':
                writer.writerow([i[0],i[1],level11])
        st.write('dessert_1')
        level12 = st.text_input("Quantity:",value="0",key=18)
        for i in l:
            if i[0]=='dessert_1':
                writer.writerow([i[0],i[1],level12])
        st.write('dessert_2')
        level13 = st.text_input("Quantity:",value="0",key=19)
        for i in l:
            if i[0]=='dessert_2':
                writer.writerow([i[0],i[1],level13])
        st.write('dessert_3')
        level14 = st.text_input("Quantity:",value="0",key=20)
        for i in l:
            if i[0]=='dessert_3':
                writer.writerow([i[0],i[1],level14])
        st.write('dessert_4')
        level15 = st.text_input("Quantity:",value="0",key=21)
        for i in l:
            if i[0]=='dessert_4':
                writer.writerow([i[0],i[1],level15])
    if (st.button("Bill")):
        df2=pd.read_csv("bill.csv")
        l=df2.values.tolist()
        with open ("billnew.csv","w") as f:
            writer=csv.writer(f)
            writer.writerow(['Name','Quantity','Amount'])
            totalcost=0
            for i in l:
                if int(i[2])>0:
                    quan=int(i[2])
                    cost=quan*i[1]
                    writer.writerow([i[0],quan,cost])
                    totalcost+=cost
        df1=pd.read_csv("billnew.csv")
        l=df1.values.tolist()
        Order.insert(l)
        st.table(df1)
    payment = st.selectbox("Payment: ",['Credit/Debit card', 'Cash', 'Net banking','Phonepe/Paytm','UPI'],key=33)
    if (st.button("Payment successful")):
        st.balloons()
        st.subheader("Order is confirmed")
        st.text("Thanks for ordering with us")
        st.text("We hope you had a good experience")
    if (st.button("Payment unsuccessful")):
        st.error("Oops,try again!!!!1")

                                
                                        
elif (user=='Manager'):
    pw=st.text_input("Confirm password to enter portal",type="password",key=22)
    if pw=="kamat123":
        st.success("Logged in")
        df=pd.read_csv("mainmenu.csv")
        df1=pd.read_csv("specialmenu.csv")
        st.subheader("MAIN MENU")
        st.table(df)
        st.subheader("SPECIAL MENU")
        st.table(df1)
        change=st.radio("Do you want to change anything in the menu?",("Yes","No"),key=23)
        if change=="Yes":
            count=24
            old=st.text_input("Enter the dish's name you would like to change: ",key=count)
            count=count+1
            j=None
            df3=pd.read_csv("mainmenu.csv")
            l=df.values.tolist()
            for i in l:
                if i[0]==old:
                    i[0]=st.text_input("Enter the new dish's name: ",key=count)
                    count=count+1
                    i[1]= st.text_input("Enter the price of the new dish: ",key=count)
                    count=count+1
                    i[2]= st.text_input("Enter the available quantity of the new dish: ",key=count)
                    count=count+1
            with open ("specialmenunew.csv","w") as f2:
                writer=csv.writer(f2)
                writer.writerow(['Name','Price','Quantity'])
                for i in l:
                    writer.writerow(i)
                f2.close()
            if (st.button("New menu")):
                st.subheader("New Menu")
                df2=pd.read_csv("specialmenunew.csv")
                st.table(df2)


    else:
        st.warning("Only for STAFF")      
        
        
