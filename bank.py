import tkinter as tk
import datetime as dt
import sqlite3


# DATABASE USING SQL

conn = sqlite3.connect('srmist_ktr_bank.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS students
             (name TEXT, username TEXT, phno TEXT, pwd TEXT, regno TEXT)''')

c.execute('''CREATE TABLE IF NOT EXISTS transactions
             (regno TEXT, amount REAL)''')
conn.commit()
conn.close()

# MAIN WINDOW

root = tk.Tk()
root.geometry("800x600")
root.configure(bg="light grey")
root.title("SRM Student Banking")



def bank_time(l1,l2):
    date = dt.datetime.now()
    format_date = f" {date:%a, %b %d %Y}"
    format_time = f" {date:%I:%M:%S %p}"
    l1.config(text=format_date, font=("calibri bold", 12),bg="light grey",)
    l2.config(text=format_time, font=("calibri bold", 12),bg="light grey")
    l1.after(1200, bank_time,l1,l2) 


# REGISTRATION WINDOW 

def register():
    register_window = tk.Toplevel(root)
    register_window.geometry("800x600")
    register_window.configure(bg="light grey")
    register_window.title("Registration Window")

    reglabel = tk.Label(register_window,text="PROVIDE REGISTRATION DETAILS BELOW",fg="white",bg="tomato",width="500",height=2,font=("calibri bold", 18))
    reglabel.pack(pady=1)

    name_label = tk.Label(register_window, text="NAME",bg="light grey",fg="black",font=("calibri bold",12))
    name_label.pack()
    name_entry = tk.Entry(register_window)
    name_entry.pack()

    username_label = tk.Label(register_window, text="USERNAME",bg="light grey",fg="black",font=("calibri bold",12))
    username_label.pack()
    username_entry = tk.Entry(register_window)
    username_entry.pack()

    phno_label = tk.Label(register_window, text="PHONE NUMBER",bg="light grey",fg="black",font=("calibri bold",12))
    phno_label.pack()
    phno_entry = tk.Entry(register_window)
    phno_entry.pack()

    pwd_label = tk.Label(register_window, text="PASSWORD",bg="light grey",fg="black",font=("calibri bold",12))
    pwd_label.pack()
    pwd_entry = tk.Entry(register_window)
    pwd_entry.pack()

    regno_label = tk.Label(register_window, text="REGISTRATION NUMBER",bg="light grey",fg="black",font=("calibri bold",12))
    regno_label.pack()
    regno_entry = tk.Entry(register_window)
    regno_entry.pack()
    
    
# ENTER AND EXIT FUNCTION FOR DATA INPUT AND EXIT WINDOW

    def enter():
        name = name_entry.get()
        username = username_entry.get()
        phno = phno_entry.get()
        pwd = pwd_entry.get()
        regno = regno_entry.get()
        conn = sqlite3.connect('srmist_ktr_bank.db')
        c = conn.cursor()
        c.execute("INSERT INTO students VALUES (?, ?, ?, ?, ?)", (name, username, phno, pwd, regno))
        conn.commit()
        conn.close()
        message_label.config(text="Registration successful!")
        register_window.destroy()

    def exit():
        register_window.destroy()
    
    tk.Label(register_window,text="",bg="light grey").pack(pady=10)
    
    enter_button = tk.Button(register_window, text="ENTER",bg="green",fg="white", command=enter)
    enter_button.pack(pady=5)

    exit_button = tk.Button(register_window, text="EXIT",bg="steel blue",fg="white", command=exit)
    exit_button.pack(pady=5)
    
    tk.Label(register_window,text="",bg="light grey").pack(pady=45)
    
    l1 = tk.Label(register_window, font=("calibri bold", 12), fg="black")
    l1.pack()    
    l2 = tk.Label(register_window, font=("calibri bold", 12), fg="black")
    l2.pack()
    
    bank_time(l1,l2)
    
    
# LOGIN WINDOW

def login():
    
    login_window = tk.Toplevel()
    login_window.geometry("600x500")
    login_window.title("Login Window")
    login_window.configure(bg="light grey")
    loglabel = tk.Label(login_window,text="PROVIDE LOGIN DETAILS BELOW",fg="white",bg="teal",width="500",height=2,font=("calibri bold", 18))
    loglabel.pack(pady=1)
    lbl = tk.Label(login_window,text="",bg="light grey")
    lbl.pack(pady=30)
    username_label = tk.Label(login_window, text="USERNAME",bg="light grey",fg="black",font=("calibri bold",12))
    username_entry = tk.Entry(login_window)
    username_label.pack(pady=5)
    username_entry.pack(pady=5)

    password_label = tk.Label(login_window,text="PASSWORD",bg="light grey",fg="black",font=("calibri bold",12))
    password_entry=tk.Entry(login_window)
    password_label.pack(pady=5)
    password_entry.pack(pady=5)
    
    
# FUNCTION FOR LOGIN DATA INPUT

    def ok():
        username = username_entry.get()
        password = password_entry.get()
        conn = sqlite3.connect('srmist_ktr_bank.db')
        c = conn.cursor()
        c.execute("SELECT * FROM students WHERE username=? AND pwd=?", (username, password))
        result = c.fetchone()
        conn.close()

        if result:
            message_label.config(text="Login successful!")

# OPTIONS WINDOW

            def continue_():
                continue_window = tk.Toplevel(root)
                continue_window.geometry("800x600")
                continue_window.configure(bg="light grey")
                cont_label = tk.Label(continue_window,text="BANKING OPTIONS",fg = "white" ,bg="purple2", width="500", height="2", font=("calibri bold", 25))
                cont_label.pack()
                continue_window.title("Options Menu")
                
# DEPOSIT WINDOW

                def deposit():
                    deposit_window = tk.Toplevel(root)
                    deposit_window.geometry("600x500")
                    deposit_window.configure(bg="light grey")
                    deposit_window.title("Deposit")
                    
                    depo_label=tk.Label(deposit_window,text="DEPOSIT AMOUNT",fg = "white" ,bg="red", width="500", height="2", font=("calibri bold", 25))
                    depo_label.pack()
                    
                    lbl=tk.Label(deposit_window,text="",bg="light grey").pack(pady=10)
                
                    regno_label = tk.Label(deposit_window, text="REGISTRATION NUMBER",bg="light grey",font=("calibri bold",12))
                    regno_label.pack()
                    
                    regno_entry = tk.Entry(deposit_window)
                    regno_entry.pack(pady=5)
                    
                    lbl=tk.Label(deposit_window,text="",bg="light grey").pack(pady=1)
                    
                    password_label = tk.Label(deposit_window, text="PASSWORD",bg="light grey",font=("calibri bold",12))
                    password_label.pack()
                    
                    password_entry = tk.Entry(deposit_window)
                    password_entry.pack(pady=5)
                    
                    lbl=tk.Label(deposit_window,text="",bg="light grey").pack(pady=1)

                    amount_label = tk.Label(deposit_window, text="AMOUNT",bg="light grey",font=("calibri bold",12))
                    amount_label.pack()
                    
                    amount_entry = tk.Entry(deposit_window)
                    amount_entry.pack(pady=5)

                    def save():
                        regno = regno_entry.get()
                        password = password_entry.get()
                        amount = float(amount_entry.get())
                        conn = sqlite3.connect('srmist_ktr_bank.db')
                        c = conn.cursor()
                        c.execute("SELECT * FROM students WHERE regno=? AND pwd=?", (regno, password))
                        result = c.fetchone()

                        if result:
                            c.execute("INSERT INTO transactions VALUES (?, ?)", (regno, amount))
                            conn.commit()
                            conn.close()
                            message_label.config(text="Amount deposited successfully!")
                            deposit_window.destroy()
                        else:
                            message_label.config(text="Invalid credentials")
                            deposit_window.destroy()
                     
                    lbl=tk.Label(deposit_window,text="",bg="light grey").pack()
                    save_button = tk.Button(deposit_window, text="Save",bg="green",fg="white", command=save)
                    save_button.pack()
                    
# WITHDRAW WINDOW

                def withdraw():
                    withdraw_window = tk.Toplevel(root)
                    withdraw_window.geometry("600x500")
                    withdraw_window.configure(bg="light grey")
                    withdraw_window.title("Withdraw")
                    
                    witdrw_label=tk.Label(withdraw_window,text="WITHDRAW AMOUNT",fg = "white" ,bg="green", width="500", height="2", font=("calibri bold", 25))
                    witdrw_label.pack()
                    
                    lbl=tk.Label(withdraw_window,text="",bg="light grey").pack(pady=10)
                
                    regno_label = tk.Label(withdraw_window, text="REGISTRATION NUMBER",bg="light grey",font=("calibri bold",12))
                    regno_label.pack()
                    
                    regno_entry = tk.Entry(withdraw_window)
                    regno_entry.pack(pady=5)
                    
                    lbl=tk.Label(withdraw_window,text="",bg="light grey").pack(pady=1)
                    
                    password_label = tk.Label(withdraw_window, text="PASSWORD",bg="light grey",font=("calibri bold",12))
                    password_label.pack()
                    
                    password_entry = tk.Entry(withdraw_window)
                    password_entry.pack(pady=5)
                    
                    lbl=tk.Label(withdraw_window,text="",bg="light grey").pack(pady=1)

                    amount_label = tk.Label(withdraw_window, text="AMOUNT",bg="light grey",font=("calibri bold",12))
                    amount_label.pack()
                    
                    amount_entry = tk.Entry(withdraw_window)
                    amount_entry.pack(pady=5)
                    
                    def ok():
                        regno = regno_entry.get()
                        password = password_entry.get()
                        amount = float(amount_entry.get())
                        conn = sqlite3.connect('srmist_ktr_bank.db')
                        c = conn.cursor()
                        c.execute("SELECT * FROM students WHERE regno=? AND pwd=?", (regno, password))
                        result = c.fetchone()

                        if result:
                            c.execute("INSERT INTO transactions VALUES (?, ?)", (regno, -amount))
                            conn.commit()
                            conn.close()
                            message_label.config(text="Amount withdrawn successfully!")
                            withdraw_window.destroy()
                        else:
                            message_label.config(text="Invalid credentials")
                            withdraw_window.destroy()
                            
                    lbl=tk.Label(withdraw_window,text="",bg="light grey").pack()
                    
                    ok_button = tk.Button(withdraw_window, text="OK",bg="gold",fg="black", command=ok)
                    ok_button.pack()
                    
# CHECK BALACNCE WINDOW  

                def check_balance():
                    check_balance_window = tk.Toplevel(root)
                    check_balance_window.geometry("600x500")
                    check_balance_window.configure(bg="light grey")
                    check_balance_window.title("Check Balance")
                    
                    chk_label=tk.Label(check_balance_window,text="CHECK BALANCE",fg = "white" ,bg="orange", width="500", height="2", font=("calibri bold", 25))
                    chk_label.pack()
                    
                    lbl=tk.Label(check_balance_window,text="",bg="light grey").pack(pady=10)
                     
                    regno_label = tk.Label(check_balance_window, text="REGISTRATION NUMBER",bg="light grey",font=("calibri bold",12))
                    regno_label.pack()
                    
                    regno_entry = tk.Entry(check_balance_window)
                    regno_entry.pack(pady=5)
                    
                    lbl=tk.Label(check_balance_window,text="",bg="light grey").pack(pady=1)
                    
                    password_label = tk.Label(check_balance_window, text="PASSWORD",bg="light grey",font=("calibri bold",12))
                    password_label.pack()
                    
                    password_entry = tk.Entry(check_balance_window)
                    password_entry.pack(pady=5)  
                    
                    def ok():
                        regno = regno_entry.get()
                        password = password_entry.get()
                        conn = sqlite3.connect('srmist_ktr_bank.db')
                        c = conn.cursor()
                        c.execute("SELECT * FROM students WHERE regno=? AND pwd=?", (regno, password))
                        result = c.fetchone()

                        if result:
                            c.execute("SELECT SUM(amount) FROM transactions WHERE regno=?", (regno,))
                            balance = c.fetchone()[0]
                            conn.close()
# SHOW BALANCE WINDOW                            
                            balance_window = tk.Toplevel(root)
                            balance_window.geometry("250x50")
                            balance_window.configure(bg="light grey")
                            balance_window.title("Your Balance")
                            balance_label = tk.Label(balance_window, text="BALANCE: {}".format(balance),bg="green",fg="white",font=("calibri bold",15))
                            balance_label.pack()
                            check_balance_window.destroy()                                                       
                        else:
    
                           message_label.config(text="Invalid credentials")
                           check_balance_window.destroy()
                           ok_button = tk.Button(check_balance_window, text="OK",bg="green",fg="white", command=ok).pack(pady=15)
                
                    lbl=tk.Label(check_balance_window,text="",bg="light grey").pack()
                      
                    ok_button = tk.Button(check_balance_window, text="OK",bg="green",fg="white", command=ok)
                    ok_button.pack()
                    
                lbl=tk.Label(continue_window,text="",bg="light grey").pack(pady=10)
                
                deposit_button=tk.Button(continue_window,text="DEPOSIT",height="2", width="15",fg="white",bg="red",font=("calibri bold",15),command=deposit)
                deposit_button.pack()
                
                lbl=tk.Label(continue_window,text="",bg="light grey").pack(pady=10)

                withdraw_button=tk.Button(continue_window,text="WITHDRAW",height="2", width="15",fg="white",bg="green",font=("calibri bold",15),command=withdraw)
                withdraw_button.pack()
                
                lbl=tk.Label(continue_window,text="",bg="light grey").pack(pady=10)

                check_balance_button=tk.Button(continue_window,text="CHECK BALANCE",height="2", width="15",fg="white",bg="orange",font=("calibri bold",15),command=check_balance)
                check_balance_button.pack()
                
                lbl=tk.Label(continue_window,text="",bg="light grey").pack(pady=30)
                
                l1 = tk.Label (continue_window, font=("calibri bold", 12), fg="black")
                l1.pack()    
                l2 = tk.Label(continue_window, font=("calibri bold", 12), fg="black")
                l2.pack()
    
                bank_time(l1,l2)

            continue_button=tk.Button(login_window,text="Continue",bg="steel blue",fg="white",command=continue_)
            continue_button.pack(pady=5)
            tk.Label(login_window,text="",bg="light grey").pack(pady=25)
            l1 = tk.Label (login_window, font=("calibri bold", 12), fg="black")
            l1.pack()    
            l2 = tk.Label(login_window, font=("calibri bold", 12), fg="black")
            l2.pack()
    
            bank_time(l1,l2)

        else:
            message_label.config(text="Invalid credentials")

    ok_button=tk.Button(login_window,text="OK",bg="green",fg="white",command=ok)
    ok_button.pack(pady=5)
    
# MAIN WINDOW PART

frntlabel = tk.Label(root,text="WELCOME TO SRMIST KTR STUDENT BANK",fg = "white" ,bg="steel blue", width="500", height="2", font=("calibri bold", 25))
frntlabel.pack(pady=0) 
frntlabel = tk.Label(root,text="",bg="light grey")
frntlabel.pack(pady=50)
register_button = tk.Button(root, text="REGISTER",height="2", width="15",fg="white",bg="tomato",font=("calibri bold",15), command=register,activebackground='teal',activeforeground='white')
register_button.pack()

login_button = tk.Button(root,text="LOGIN", height="2", width="15",fg='white',bg='teal' ,font=("calibri bold", 15), command=login,activebackground='tomato',activeforeground='white')   
tk.Label(root,text="",bg="light grey").pack(pady=5)   
login_button.pack(pady=5)

message_label = tk.Label(root, text="",bg="light grey",fg="red",font=("calibri bold",15))
message_label.pack()

tk.Label(root,text="",bg="light grey").pack(pady=45)

l1 = tk.Label (root, font=("calibri", 12), fg="black")
l1.pack()    
l2 = tk.Label(root, font=("calibri", 12), fg="black")
l2.pack()
    
bank_time(l1,l2)

root.mainloop()
