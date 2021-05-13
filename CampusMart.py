###############################################################################
## Import required modules
## mysql.connector
##      MySQL Connector/Python enables Python programs to access MySQL
##      databases, using an API that is compliant with the Python Database API
##      Specification v2.0 (PEP 249). It is written in pure Python and does not
##      have any dependencies except for the Python Standard Library.
## tkinter for simple GUI

## Connect to local database
###############################################################################
import tkinter as tk
import mysql.connector as sql
try:
    mydb = sql.connect(host="localhost", user="root", passwd="c00lpa$$w0rd", database='mart')
except:
    print('Error in connecting to the database')

LOG_USER,LOG_CREDIT='',0
###############################################################################    
###############################################################################    
    
    
    
###############################################################################
###############################################################################
def log():
    logscreen = tk.Tk()
    logscreen.title('Authentication Box')
    logscreen.geometry('225x150')
    
    
    def clear_widget(event):
        if username_box == logscreen.focus_get() and username_box.get() == 'Enter Username':
            username_box.delete(0, tk.END)
        elif password_box == password_box.focus_get() and password_box.get() == '     ':
            password_box.delete(0, tk.END)
 
    def repopulate_defaults(event):
        if username_box != logscreen.focus_get() and username_box.get() == '':
            username_box.insert(0, 'Enter Username')
        elif password_box != logscreen.focus_get() and password_box.get() == '':
            password_box.insert(0, '     ')

    def login(*event):
        global LOG_USER,LOG_CREDIT
        mycursor=mydb.cursor()
        mycursor.execute("select * from users")
        myresult=mycursor.fetchall()
        user=username_box.get()
        pswd=password_box.get()
        for i in myresult:
            if i[0]==user and i[1]==pswd:
                LOG_USER=user
                LOG_CREDIT=i[2]
                logscreen.destroy()
                main.destroy()
                print()
                print('-+'*25)
                print('Hello '+str(LOG_USER)+'!')
                print('You have '+str(LOG_CREDIT)+' credits.')
                print('-+'*25)
                print()
                print('-+'*25)
                print('-+'*25)
                print('             Welcome to Campus-Mart!')
                print('-+'*25)
                print('-+'*25)
                screen=tk.Tk()
                screen.title('Campus-Mart')
                screen.configure(background='#40e0d0')
                screen.geometry("375x175")

                temp = tk.Button(screen, font='comic-sans', text = "", padx=20, pady=10)
                temp.grid(row=0, column=0)
                temp.configure(background='#ccff00')
                temp = tk.Button(screen, font='comic-sans', text = "", padx=20, pady=10)
                temp.grid(row=0, column=1)
                temp.configure(background='#ccff00')
                temp = tk.Button(screen, font='comic-sans', text = "", padx=20, pady=10)
                temp.grid(row=0, column=3)
                temp.configure(background='#ccff00')
                temp = tk.Button(screen, font='comic-sans', text = "", padx=20, pady=10)
                temp.grid(row=0, column=4)
                temp.configure(background='#ccff00')
        
        #######################################################################
        #######################################################################
                def buy():
                    global LOG_CREDIT
                    def foo():
                        global LOG_GREDIT
                        print(LOG_CREDIT)
                        pid=int(item.get())
                        mycursor1=mydb.cursor()
                        mycursor1.execute("select * from products where status='available'")
                        myresult=mycursor1.fetchall()
                        prod=(0,)
                        for i in myresult:
                            if i[0]==pid:
                                prod=i
                        try:
                            print('-+'*25)
                            print('Product Key: '+str(prod[0]))
                            print('Product Name: '+str(prod[1]))
                            print('User: '+str(prod[2]))
                            print('Status: '+str(prod[3]))
                            print('Price: '+str(prod[4]))
                            print('-+'*25)
                            return
                        except:
                            print('Product unavailable!')
                            print('-+'*25)
                            
                    def fuu():
                        global LOG_CREDIT
                        pid=int(item.get())
                        mycursor2=mydb.cursor()
                        sqlq = "select * from products WHERE pid = {}".format(pid)
                        mycursor2.execute(sqlq)
                        buydata=mycursor2.fetchall()
                        if LOG_CREDIT<buydata[0][4]:
                            import tkinter.messagebox as sa
                            sorry=sa.showinfo('Insufficient Credits','Not enough credits')
                            buy()
                        else:
                            import tkinter.messagebox as sa
                            sure=sa.askquestion('Order Confirmation','Do you want to proceed?')
                            if sure=='yes':
                                mycursor3=mydb.cursor()
                                print(buydata[0][2],type(buydata[0][2]))
                                getquery="select credit from users where username=\'{}\'".format(buydata[0][2])
                                mycursor3.execute(getquery)
                                usercredit=mycursor3.fetchall()
                                print(usercredit[0][0])
                                addcredit=usercredit[0][0]
                                print(buydata[0][4])
                                addcredit+=buydata[0][4]
                                print(addcredit)
                                updquery="update users set credit ={} where username=\'{}\'".format(addcredit,buydata[0][2])
                                mycursor3.execute(updquery)
                                statusquery = "UPDATE products SET status = 'unavailable' WHERE pid = {}".format(pid)
                                mycursor3.execute(statusquery)
                                mydb.commit()
                                labelResult.config(text="Purchased!")
                                print('-+'*25)
                                print('Purchase Successful!')
                                print('-+'*25)
                                LOG_CREDIT-=buydata[0][4]
                                updquery1="update users set credit ={} where username=\'{}\'".format(LOG_CREDIT,LOG_USER)
                                mycursor3.execute(updquery1)
                                balance=sa.showinfo('Balance','You now have {} credits'.format(LOG_CREDIT))
                                mydb.commit()
                                return
                            else:
                                return
                            
                            
                    print(LOG_CREDIT)
                    mycursor=mydb.cursor()
                    query='select * from products'
                    mycursor.execute(query)
                    myresult=mycursor.fetchall()
                    
                    if myresult:
                        print('Product Key: Product')
                        print('-+'*25)
                        for x in myresult:
                            if x[3]=='available':
                                print(str(x[0])+': '+str(x[1]))
                                print('-+'*25)
                    else:
                        print('No Product Posted')
                                
                    buyscreen=tk.Tk(className=' Campus-Mart-Buy')
                    buyscreen.geometry("300x125")
                    buyscreen.configure(background='#40e0d0')
                                        
                    item=tk.StringVar(buyscreen)
                    
                    label1 = tk.Label(buyscreen, background='#ccff00', text = "Enter Product Key: ").grid(row = 0, column = 0)
                    e1 = tk.Entry(buyscreen, textvariable=item).grid(row = 0, column = 1)
                                  
                    labelResult = tk.Label(buyscreen, background='#40e0d0')
                    labelResult.grid(row=3, column=1)
                    
                    check = tk.Button(buyscreen, background='#c6e2ff', command=foo, text = "Check", activeforeground='green', activebackground='lightgreen', padx=20, pady=10).grid(row=1, column=1)
                    confirm = tk.Button(buyscreen, background='#c6e2ff', command=fuu, text = "Confirm Purchase", activeforeground='green', activebackground='lightgreen', padx=20, pady=10).grid(row=2, column=1)
        #######################################################################
        #######################################################################
        
        
        #######################################################################
        #######################################################################
                def sell():
                    def func():                        
                        name=(pname.get())
                        cost=int(price.get())
                        
                        mycursor=mydb.cursor()
                        mycursor.execute("select * from products")
                        myresult=mycursor.fetchall()
                        
                        if myresult:
                            num=myresult[-1][0]
                            num+=1
                            sqlq1 = "INSERT INTO products (pid, pname, username, status, price) VALUES (%s, %s, %s, %s, %s)"
                            val = (num, name, LOG_USER, 'available', cost)
                            mycursor.execute(sqlq1, val)
                            mydb.commit()
                            labelResult.config(text="Posted!")  
                            return
                        else:
                            sql = "INSERT INTO products (pid, pname, username, status, price) VALUES (%s, %s, %s, %s, %s)"
                            val = (1, name, LOG_USER, 'available', cost)
                            mycursor.execute(sql, val)
                            mydb.commit()
                            labelResult.config(text="Posted!")
                            return


                    sellscreen=tk.Tk(className=' Campus-Mart-Sell')
                    sellscreen.geometry("300x125")
                    sellscreen.configure(background='#40e0d0')
                                                 
                    pname=tk.StringVar(sellscreen)
                    price=tk.StringVar(sellscreen)
                    
                    label1 = tk.Label(sellscreen,background='#ccff00',text = "Product Name: ").grid(row = 0, column = 0)
                    e1 = tk.Entry(sellscreen, textvariable=pname).grid(row = 0, column = 1)
                    label3 = tk.Label(sellscreen,background='#ccff00',text = "Product Price: ").grid(row = 1, column = 0)
                    e3 = tk.Entry(sellscreen, textvariable=price).grid(row = 1, column = 1)
                        
                    labelResult = tk.Label(sellscreen)
                    labelResult.grid(row=3, column=1)
                    labelResult.configure(background='#40e0d0')
                    post = tk.Button(sellscreen, background='#c6e2ff', command=func, text = "Post", activeforeground='green', activebackground='lightgreen', padx=20, pady=10).grid(row=2, column=1)
        #######################################################################
        #######################################################################
                

                temp2 = tk.Button(screen, text="Campus-Mart", font='comic-sans', padx=10, pady=10)
                temp2.grid(row=0, column=2)
                temp2.configure(background='#6897bb')

                buybut = tk.Button(screen, font='comic-sans', command=buy, text = "Buy", activeforeground='green', activebackground='lightgreen', padx=20, pady=10)
                buybut.grid(row=2, column=2)
                buybut.configure(background='#c6e2ff')
                 
                sellbut = tk.Button(screen, font='comic-sans',command=sell, text = "Sell", activeforeground='green', activebackground='lightgreen', padx=20, pady=10)
                sellbut.grid(row=3, column=2) 
                sellbut.configure(background='#c6e2ff')
                  
                screen.mainloop()                

            else:
                if i[0]==user:
                    import tkinter.messagebox as sa
                    invalidpswd=sa.showinfo('Error','Incorrect Password')
                    logscreen.destroy()
 
 
    rows = 0
    while rows < 10:
        logscreen.rowconfigure(rows, weight=1)
        logscreen.columnconfigure(rows, weight=1)
        rows += 1
 
 
    username_box = tk.Entry(logscreen)
    username_box.insert(0, 'Enter Username')
    username_box.bind("<FocusIn>", clear_widget)
    username_box.bind('<FocusOut>', repopulate_defaults)
    username_box.grid(row=1, column=5, sticky='NS')
 
 
    password_box = tk.Entry(logscreen, show='*')
    password_box.insert(0, '     ')
    password_box.bind("<FocusIn>", clear_widget)
    password_box.bind('<FocusOut>', repopulate_defaults)
    password_box.bind('<Return>', login)
    password_box.grid(row=2, column=5, sticky='NS')
 
 
    login_btn = tk.Button(logscreen, text='Login', command=login)
    login_btn.bind('<Return>', login)
    login_btn.grid(row=5, column=5, sticky='NESW')
###############################################################################
###############################################################################





###############################################################################
###############################################################################
def sign():
    def addrec():
        import tkinter.messagebox as sa
        signuser=user.get()
        signpswd=pswd.get()
        signpswd2=pswd2.get()
        print(signuser,signpswd,signpswd2)
        if signpswd!=signpswd2:
            box=sa.showinfo('error','Passwords don\'t match')
            sign()
        else:           
            mycursor=mydb.cursor()
            
            vals=[signuser,signpswd,0]
            query='INSERT INTO users (username,password,credit) VALUES (%s,%s,%s)'
            
            mycursor.execute(query,vals)
            mydb.commit()
            msg=sa.showinfo('Success','Successfully signed up!')
            main.destroy()
            

    login.destroy()
    signup.destroy()
    
    user=tk.StringVar()
    pswd=tk.StringVar()
    pswd2=tk.StringVar()
    label1 = tk.Label(main,background='#ccff00',text = "user        :").grid(row = 1, column = 0)
    e1 = tk.Entry(main, textvariable=user).grid(row = 1, column = 2)
    
    label2 = tk.Label(main,background='#ccff00',text = "pswd      :").grid(row = 2, column = 0)
    e2 = tk.Entry(main, textvariable=pswd).grid(row = 2, column = 2)
    
    label2 = tk.Label(main,background='#ccff00',text = "confirm :").grid(row = 3, column = 0)
    e2 = tk.Entry(main, textvariable=pswd2).grid(row = 3, column = 2)
    
    add_rec = tk.Button(main, background='#c6e2ff', command=addrec, text = "Sign Up", activeforeground='green', activebackground='lightgreen', padx=20, pady=10).grid(row=4, column=2)
##############################################################################    
###############################################################################





###############################################################################
## Driver Code
## uses tkinter.Tk() function
###############################################################################
main=tk.Tk()
main.title('Login')
main.configure(background='#40e0d0')
main.geometry("375x175")

temp = tk.Button(main, font='comic-sans', text = "", padx=20, pady=10)
temp.grid(row=0, column=0)
temp.configure(background='#ccff00')
temp = tk.Button(main, font='comic-sans', text = "", padx=20, pady=10)
temp.grid(row=0, column=1)
temp.configure(background='#ccff00')
temp = tk.Button(main, font='comic-sans', text = "", padx=20, pady=10)
temp.grid(row=0, column=3)
temp.configure(background='#ccff00')
temp = tk.Button(main, font='comic-sans', text = "", padx=20, pady=10)
temp.grid(row=0, column=4)
temp.configure(background='#ccff00')

temp2 = tk.Button(main, text="Campus-Mart", font='comic-sans', padx=10, pady=10)
temp2.grid(row=0, column=2)
temp2.configure(background='#6897bb')
                
login = tk.Button(main, font='comic-sans', command=log, text = "Login", activeforeground='green', activebackground='lightgreen', padx=20, pady=10)
login.grid(row=2, column=2)
login.configure(background='#c6e2ff')
                 
signup = tk.Button(main, font='comic-sans',command=sign, text = "Sign-Up", activeforeground='green', activebackground='lightgreen', padx=20, pady=10)
signup.grid(row=3, column=2) 
signup.configure(background='#c6e2ff')
                 
main.mainloop()
###############################################################################
###############################################################################