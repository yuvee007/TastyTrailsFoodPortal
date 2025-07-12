import mysql.connector as sql


#ADDING FOOD OPTION FOR ADMIN
def add_food():
 db=sql.connect(host="localhost",user="root",passwd="yuvee29107",database="foodportal")
 cur=db.cursor()
 choice='y'
 while choice in 'yY':
  s_no=int(input("Enter the Food ID:"))
  f_n=input("Enter the Food name:")
  f_p=int(input("Enter the Price of Food:"))
  print('''Choose from the following food types:
1 = Main course
2 = Appetizers
3 = Beverages
4 = Desserts''')
  ft=int(input("Enter the Food Type by number: "))
  fc=input("Enter food category: (Veg/NonVeg)")
  if ft==1:
   cur.execute("Insert into Main_Course values({},'{}',{}, '{}')".format(s_no,f_n,f_p,fc))
   db.commit()
  elif ft==2:
   cur.execute("Insert into Appetizer values({},'{}',{}, '{}')".format(s_no,f_n,f_p,fc))
   db.commit()
  elif ft==3:
   cur.execute("Insert into Beverages values({}, '{}',{})".format(s_no,f_n,f_p))
   db.commit()
  elif ft==4:
   cur.execute("Insert into Desserts values({}, '{}',{})".format(s_no,f_n,f_p))
   db.commit()
  print("NEW FOOD ADDED SUCCESSFULLY!")
  choice=input("Do you wish to add more? (Y/N): ")


#UPDATING FOOD & PRICE OPTION FOR ADMIN
def update_food():
 db=sql.connect(host="localhost",user="root",passwd="yuvee29107",database="foodportal")
 cur=db.cursor()
 print('''MENU CATEGORIES:
1. Main Course
2. Appetizers
3. Beverages
4. Desserts''')
 tables=['Main_Course', 'Appetizers', 'Beverages', 'Desserts']
 choice=int(input("Enter your choice: "))
 if choice==1:
  table=tables[0]
 elif choice==2:
  table=tables[1]
 elif choice==3:
  table=tables[2]
 elif choice==4:
  table=tables[3]
 print('''1. Update food name.
2. Update food price.''')
 us=int(input("Enter your choice :"))
 if us==1:
  fnid=int(input("Enter the Food ID whose food name you want to update :"))
  fna=input("Enter the updated Food Name: ")
  cur.execute("Update {} set Name='{}' where Food_ID={}".format(table,fna,fnid))
  print("UPDATED SUCCESSFULLY")
  db.commit()
 elif us==2:
  fnic=int(input("Enter the Food ID whose food price you want to update: "))
  fnf=input("Enter the updated Food Price: ")
  cur.execute("update {} set Price={} where Food_ID={}".format(table,fnf,fnic))
  print("UPDATED SUCCESSFULLY")
  db.commit()
 print("You have been Redirected to the Admin page.")
 ad_login()


#VIEWING ORDER HISTORY OPTION FOR ADMIN
def view_orders():
 db=sql.connect(host="localhost",user="root",passwd="yuvee29107",database="foodportal")
 cur=db.cursor()
 month=input("Enter current month in numbers: ")
 cur.execute("select * from orders where month(Date)='{}'".format(month))
 print("Details of all orders are:")
 details=cur.fetchall()
 for i in details:
  print("*=*=*=*=*=*=*=*=*=*=*=*=*=*=*")
  print("Food name: ",i[0])
  print("Food price: ",i[1])
  print("Total price: ",i[2])
  print("Phone No: ",i[3])
  print("Address: ",i[4])
  print("*=*=*=*=*=*=*=*=*=*=*=*=*=*=*")


#DELETING FOOD OPTION FOR ADMIN
def delete_food():
 db=sql.connect(host="localhost",user="root",passwd="yuvee29107",database="foodportal")
 cur=db.cursor()
 print('''MENU CATEGORIES:
1. Main Course
2. Appetizers
3. Beverages
4. Desserts''')
 choice=int(input("Enter your choice according to number: "))
 if choice==1:
  table='Main_Course'
 elif choice==2:
  table='Appetizers'
 elif choice==3:
  table='Beverages'
 elif choice==4:
  table='Desserts'
 fid=int(input("Enter the Food ID of the food you want to delete: "))
 cur.execute("delete from {} where Food_ID={}".format(table,fid))
 print("FOOD ITEM DELETED SUCCESSFULLY")
 db.commit()
 print("You have been Redirected to the Admin page.")
 ad_login()


# FOOD ITEMS TO SHOW CUSTOMER
def menu():
 db=sql.connect(host="localhost",user="root",passwd="yuvee29107",database="foodportal")
 cur=db.cursor()

 t=['MAIN_COURSE', 'APPETIZERS', 'BEVERAGES', 'DESSERTS']
 for i in range(len(t)):
  table=t[i]
  cur.execute("select * from {}".format(table))
  w=cur.fetchall()
  print("-------------", table, "---------------")
  for z in w:
   if i==0 or i==1:
    print("Food ID: ",z[0],"-- Food Name: ",z[1],"-- Price: ",z[2],"-- Food type: ",z[3] )
   elif i==2 or i==3:
    print("Food ID: ",z[0],"-- Food Name: ",z[1],"-- Price: ",z[2])
 db.commit()
 ui=input("Do you want to order food: (Y/N)")
 if ui=="Y" or ui=="y":
  order()
 else:
  print('''Thank you.
You have been Redirected to the Main Page.''')
  return


#TO PLACE ORDER
def order():
 db=sql.connect(host="localhost",user="root",passwd="yuvee29107",database="foodportal")
 cur=db.cursor()
 date=input("Enter today's date (YYYY-MM-DD): ")
 c_name=input("Enter your name: ")
 phn=int(input("Enter your phone no.: "))
 adr=input("Enter your Address: ")
 choice='y'
 while choice in 'Yy':
  print('''Choose your menu,
1. Main Course
2. Appetizers
3. Beverages
4. Desserts''')
  c=int(input("Enter the number associated with your choice: "))
  if c==1:
   table='Main_course'
  elif c==2:
   table='Appetizers'
  elif c==3:
   table='Beverages'
  elif c==4:
   table='Desserts'
  f_id=int(input("Enter the Food ID of the item you want to order: "))
  qty=int(input("Enter the quantity: "))
  cur.execute("select * from {} where Food_ID={}".format(table,f_id))
  x=cur.fetchall()
  f_n=x[0][1]
  f_p=x[0][2]
  total=f_p*qty
  print("********BILL********")
  print("Customer name: ", c_name)
  print("Address: ", adr)
  print("Phone No.: ", phn)
  print("Food name: ", f_n)
  print("Food price: ", f_p)
  print("Quantity of food: ", qty)
  print('Total price:', total)
  print("********************")
  choice=input("Do you want to order more: (Y/N)")
 print('''Thanks for ordering food.
Your order has been confirmed.
You have been Redirected to the MAIN PAGE''')
 cur.execute("insert into orders values('{}','{}',{},{},{},{},'{}','{}')".format(c_name,f_n,f_p,qty,total,phn,adr,date))
 db.commit()


#VIEWING YOUR FOOD ORDER HISTORY
def view():
 db=sql.connect(host="localhost",user="root",passwd="yuvee29107",database="foodportal")
 cur=db.cursor()
 name=input("Enter your name: ")
 pno=int(input("Enter your phone no.: "))
 cur.execute("select * from orders where C_Name='{}' and Phone_No={};".format(name,pno))
 rt=cur.fetchall()
 if len(rt)>0:
  print("**********YOUR ORDER DETAILS ARE SHOWN BELOW**********")
  for i in rt:
   print("Food name:",i[1])
   print("Food price:",i[2])
   print("Total price:",i[4])
  print("Phone NO:",i[5])
  print("Address:",i[6])
 else:
  print("YOU HAVE NO ORDER HISTORY.")
 db.commit()


 #CANCELLING YOUR FOOD ORDER
def cancel():
 db=sql.connect(host="localhost",user="root",passwd="yuvee29107",database="foodportal")
 cur=db.cursor()
 name=input("Enter your name: ")
 pno=int(input("Enter your phone no.: "))
 cur.execute("delete from orders where C_Name='{}' and Phone_No={};".format(name,pno))
 print("Your order has been cancelled SUCCESSFULLY.")
 print("You have been redirected to the MAIN PAGE.")
 db.commit()



 #FEEDBACK OPTION FOR CUSTOMER
def feedb():
 db=sql.connect(host="localhost",user="root",passwd="yuvee29107",database="foodportal")
 cur=db.cursor()
 name=input("Enter your Name: ")
 phn=int(input("Enter your Phone No.: "))
 fdb=input("Give us your feedback: ")
 cur.execute("insert into Feedbackk values('{}',{},'{}')".format(name,phn,fdb))
 print("THANKYOU FOR YOUR FEEDBACK.")
 print("You have been Redirected to MAIN PAGE")
 db.commit()


#Customer Login
def main_menu():
 print("----------------------WELCOME----------------------")
 while True:
  print('''1. View Menu
2. Place your Order
3. View Order
4. Cancel your Order
5. Feedback
6. Exit''')
  a=int(input("Enter the Service you want:"))
  if a==1:
   menu()
  elif a==2:
   order()
  elif a==3:
   view()
  elif a==4:
   cancel()
  elif a==5:
   feedb()
  elif a==6:
   break


#PASSWORD FOR ADMIN TO LOGIN 
def ad_panel():
 pas=input("Enter Password: ")
 if pas=='taste_77':
  print("Access granted.")
  ad_login()
 else:
  print('''Incorrect Password.
You have been Redirected to the Main Page.''')
  admin()


#ADMIN LOGIN PAGE
def ad_login():
 while 1:
  print('''1. Add food
2. Update food
3. View order history
4. Delete food
5. Logout''')
  ask=int(input("Enter your Choice: "))
  if ask==1:
   add_food()
  elif ask==2:
   update_food()
  elif ask==3:
   view_orders()
  elif ask==4:
   delete_food()
  elif ask==5:
   return


#HOME PAGE 
def admin():
 while True:
   print('''*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=
WELCOME TO THE TASTY TRAILS RESTAURANT!
1. Admin Login
2. Customer Login
3. EXIT''')
   op=int(input("Enter option: "))
   if op==1:
    ad_panel()
   elif op==2:
    main_menu()
   elif op==3:
    break
admin()
