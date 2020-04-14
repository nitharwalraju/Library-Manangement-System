from tkinter import *
import datetime
import pymysql
window = Tk()
window2 = Tk()

def fetch_data(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()

con = pymysql.connect("localhost", "root", "root", "library", cursorclass=pymysql.cursors.DictCursor)
mycursor = con.cursor()
# mycursor.execute("CREATE TABLE IF NOT EXISTS book_master(book_id INT AUTO_INCREMENT PRIMARY KEY,title VARCHAR(50), no_of_copies INT, price INT)")
# mycursor.execute("CREATE TABLE IF NOT EXISTS Members(member_id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(50), phone varchar(10), address varchar(150))")
# mycursor.execute("CREATE TABLE IF NOT EXISTS Transactions(trans_id INT AUTO_INCREMENT PRIMARY KEY,member_id INT,book_id INT,issue_date varchar(150), date_of_return varchar(150), fine INT)")

# query = "INSERT INTO book_master (title, no_of_copies, price) VALUES(%s,%s,%s)"
# values = (
#      ("java : The complete reference", 20, 669),
#      ("php : The complete reference", 2, 600),
#      ("python : The complete reference", 7, 599),
#      ("let us c", 18, 450)
#  )
# mycursor.executemany(query, values)

# query1 = "INSERT INTO Members (name, phone, address) values(%s,%s,%s)"
# values1 = [
#      ("Raju", "9660562011", "Vki, Jaipur"),
#      ("Mansi", "7745863872","Khatipura, Jaipur"),
#      ("Bhanu ", "6725483327", "Sodala, Japur"),
#      ("Ashok", "9742318223", "Murlipura,Jaipur")
#  ]
# mycursor.executemany(query1, values1)
# con.commit()

book_master_data = fetch_data(mycursor, "select  * from book_master")
members_data = fetch_data(mycursor, "select  * from Members")
transactions_data = fetch_data(mycursor, "select  * from Transactions")

def dataset():
    book_master_data = fetch_data(mycursor, "select  * from book_master")
    members_data = fetch_data(mycursor, "select  * from Members")
    transactions_data = fetch_data(mycursor, "select  * from Transactions")

window.title("Issue Window")
transaction_id = Label(window,text="Transaction ID : ")
tran_id = Label(window,text="Auto")

member_id = Label(window, text="Member ID : ")
mem_id = Entry(window)

name_l = Label(window, text="Name : ")
name_e = Label(window, text="Auto")

book_id_l = Label(window, text="Book ID : ")
book_id_e = Entry(window)

title_l = Label(window, text="Title : ")
title_e = Label(window, text="Auto")

book_author_l = Label(window, text = "Book's Author : ")
book_author_e = Label(window, text="Auto")

date_of_ret_l = Label(window,text = "Date of Return :")
date_of_ret_e = Label(window, text="Auto")


def display_data():
    m_id = mem_id.get()
    b_id = book_id_e.get()

    valid_m, valid_b = False, False

    if int(m_id)<=len(members_data) and int(m_id)>0:
        name_e['text'] = members_data[int(m_id)-1]['name']
        valid_m = True
    else:
        name_e['text'] = 'Invalid Member ID'

    if int(b_id)<=len(book_master_data) and int(b_id)>0:
        title_e['text'] = book_master_data[int(b_id)-1]['title']
        book_author_e['text'] = '-'
        valid_b = True
    else:
        title_e['text'] = 'Invalid Book ID'
        book_author_e['text'] = 'Invalid Book ID'

    if valid_m and valid_b:
        date_of_ret_e['text'] = (datetime.datetime.now().date() + datetime.timedelta(days=7)).strftime("%d-%m-%Y")
        query2= "INSERT INTO  Transactions (member_id, book_id, issue_date, date_of_return, fine) values(%s,%s,%s,%s,%s)"
        values2=[
            (
                m_id,
                b_id,
                datetime.datetime.now().strftime("%d-%m-%Y"),
                (datetime.datetime.now().date() + datetime.timedelta(days=7)).strftime("%d-%m-%Y"),
                0
            )
        ]
        mycursor.executemany(query2, values2)
        con.commit()
        curr_trans = fetch_data(mycursor, "SELECT MAX(trans_id) FROM Transactions")[0]['MAX(trans_id)']
        tran_id['text'] = curr_trans
        dataset()
    
#buttons
issue = Button(window,text=" Issue ", command=display_data)
cancel = Button(window,text=" Cancel ",command=window.destroy)
close = Button(window,text=" Close ",command=window.destroy)

transaction_id.grid(row=0,column=0,sticky=E)
tran_id.grid(row=0,column=2,sticky=W)

member_id.grid(row=1,column=0, sticky=E)
mem_id.grid(row=1,column=2, sticky=W)

name_l.grid(row=2,column=0, sticky=E)
name_e.grid(row=2,column=2, sticky=W)

book_id_l.grid(row=3,column=0, sticky=E)
book_id_e.grid(row=3,column=2, sticky=W)

title_l.grid(row=4,column=0, sticky=E)
title_e.grid(row=4,column=2, sticky=W)

book_author_l.grid(row=5,column=0, sticky=E)
book_author_e.grid(row=5,column=2, sticky=W)

date_of_ret_l.grid(row=6,column=0, sticky=E)
date_of_ret_e.grid(row=6,column=2, sticky=W)

issue.grid(row=7,column=0, sticky=NSEW)
cancel.grid(row=7,column=1, sticky=NSEW)
close.grid(row=7,column=2, sticky=NSEW)


# window 2

window2.title("Transaction Window")

transaction_id1: Label = Label(window2,text="Transaction ID : ")
tran_id1 = Entry(window2,text="Auto")

member_id1 = Label(window2, text="Member ID : ")
mem_id1 = Label(window2, text="Auto")

name_l1 = Label(window2, text="Name : ")
name_e1 = Label(window2, text="Auto")

book_id_l1 = Label(window2, text="Book ID : ")
book_id_e1 = Label(window2, text="Auto")

title_l1 = Label(window2, text="Title : ")
title_e1 = Label(window2, text="Auto")

book_author_l1 = Label(window2, text = "Book's Author : ")
book_author_e1 = Label(window2, text="Auto")

date_of_issue1= Label(window2, text = "Date of Issue : ")
date_of_issue_e1 = Label(window2, text="Auto")

date_of_rec1 = Label(window2, text="Date of Receive : ")
date_of_rec_e1 = Label(window2, text="Auto")

fine1 = Label(window2,text="Fine : ")
fine_e1 = Label(window2, text="Auto")

def display():
    t_id = tran_id1.get()
    data = fetch_data(mycursor,"select * from Transactions where trans_id =" + t_id)
    transactions_data = fetch_data(mycursor, "select  * from Transactions")
    
    if len(data)>0:
        mem_id1['text'] = transactions_data[int(t_id)-1]['member_id']
        name_e1['text'] = members_data[int(transactions_data[int(t_id)-1]['member_id'])-1]['name']
        book_id_e1['text'] = transactions_data[int(t_id)-1]['book_id']
        title_e1['text'] = book_master_data[int(transactions_data[int(t_id)-1]['book_id'])-1]['title']
        book_author_e['text'] = '-'
        date_of_issue_e1['text']= transactions_data[int(t_id)-1]['issue_date']
        date_of_rec_e1['text'] = datetime.datetime.now().strftime("%d-%m-%Y")
        diff = datetime.datetime.now() - datetime.datetime.strptime(transactions_data[int(t_id)-1]['issue_date'], "%d-%m-%Y")
        fine_e1['text'] = '0' if diff.days<=7 else str(diff*10)
        
    else:
        mem_id1['text'] = 'Invalid Transcation ID'
        name_e1['text'] = 'Invalid Transcation ID'
        book_id_e1['text'] = 'Invalid Transcation ID'
        title_e1['text'] = 'Invalid Transcation ID'
        book_author_e1['text'] = '-'
        date_of_issue_e1['text']='-'
        date_of_rec_e1['text']='-'
        fine_e1['text']='-'

#buttons
save = Button(window2,text=" Show ", command=display)
cancel1 = Button(window2,text=" Cancel ",command=window2.destroy)
close1 = Button(window2,text=" Close ",command=window2.destroy)

transaction_id1.grid(row=0,column=0,sticky=E)
tran_id1.grid(row=0,column=2,sticky=W)

member_id1.grid(row=1,column=0, sticky=E)
mem_id1.grid(row=1,column=2, sticky=W)

name_l1.grid(row=2,column=0, sticky=E)
name_e1.grid(row=2,column=2, sticky=W)

book_id_l1.grid(row=3,column=0, sticky=E)
book_id_e1.grid(row=3,column=2, sticky=W)

title_l1.grid(row=4,column=0, sticky=E)
title_e1.grid(row=4,column=2, sticky=W)

book_author_l1.grid(row=5,column=0, sticky=E)
book_author_e1.grid(row=5,column=2, sticky=W)

date_of_issue1.grid(row=6, column=0, sticky=E)
date_of_issue_e1.grid(row=6, column=2, sticky=W)

date_of_rec1.grid(row=7, column=0, sticky=E)
date_of_rec_e1.grid(row=7, column=2, sticky=W)

fine1.grid(row=8, column=0, sticky=E)
fine_e1.grid(row=8, column=2, sticky=W)

save.grid(row=9,column=0, sticky=NSEW)
cancel1.grid(row=9,column=1, sticky=NSEW)
close1.grid(row=9,column=2, sticky=NSEW)

window2.mainloop()
window.mainloop()