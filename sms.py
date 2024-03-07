from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from sqlite3 import *
import requests
import socket
import bs4
import matplotlib.pyplot as plt
import numpy as np


try:
	google = ("www.google.com",80)
	socket.create_connection(google)
	
	res = requests.get("http://ipinfo.io/")
	data = res.json()
	city_name = data['city']

	if city_name == "Thāne":
		city = city_name.replace("ā","a")
	else:
		city = city_name

	a1 = "http://api.openweathermap.org/data/2.5/weather?units=metric"
	a2 = "&appid=c6e315d09197cec231495138183954bd"
	a3 = "&q=" + city 

	web_address = a1 + a2 + a3
	res = requests.get(web_address)
	data1 = res.json()
	temp = data1['main']['temp']

	# resp = requests.get("https://www.brainyquote.com/quote_of_the_day")
	# s = bs4.BeautifulSoup(resp.text, 'lxml')
	# data2 = s.find('img', {"class":"p-qotd"})
	# quote = data2['alt']

	resp = requests.get("https://indianexpress.com/section/technology/")
	s = bs4.BeautifulSoup(resp.text, 'lxml')
	data2 = s.find('h3', {"class":""})
	quote = data2.find('a').text
except OSError as e:
	print("issue", e)





def f1():
	adst.deiconify()
	root.withdraw()

def f2():
	root.deiconify()
	adst.withdraw()

def f3():
	vist_stData.delete(1.0,END)
	vist.deiconify()
	root.withdraw()
	con = None
	try:
		con = connect("sms_database.db")
		cur = con.cursor()
		sql = "select * from students"
		cur.execute(sql)
		data = cur.fetchall()
		msg = " "
		for d in data:
			msg = msg + " rno= " + str(d[0]) + " name= " + str(d[1]) + " marks= " + str(d[2]) + "\n"
		vist_stData.insert(INSERT,msg)
	except Exception as e:
		con.rollback()
		showerror("Issue",e)
	finally:
		if con is not None:
			con.close()
	
def f4():
	root.deiconify()
	vist.withdraw()

def f5():
	upst.deiconify()
	root.withdraw()

def f6():
	root.deiconify()
	upst.withdraw()

def f7():
	dest.deiconify()
	root.withdraw()

def f8():
	root.deiconify()
	dest.withdraw()

def adstSave():
	con = None
	try:
		con = connect("sms_database.db")
		cur = con.cursor()
		sql = "insert into students values('%d','%s','%d')"
		srno = adst_entRno.get()
		if len(srno) == 0:
			showerror("Mistake", "rno should not be empty")
			return
		if not srno.isdigit():
			showerror("Mistake", "rno should be positive integers only")
			adst_entRno.delete(0, END)
			adst_entRno.focus()
			return
		rno = int(srno)


		name = adst_entName.get()
		if not name.isalpha():
			showerror("Mistake","Name should contain alphabets only")
			adst_entName.delete(0,END)
			adst_entName.focus()
			return
		if len(name) < 2:
			showerror("Mistake","Name Should contain minimum two characters")
			return
		
		


		if len(adst_entMarks.get()) == 0:
			showerror("Mistake", "Please Enter Marks")
			return
		if not adst_entMarks.get().isdigit():
			showerror("Mistake", "Marks only in range 0-100")
			adst_entMarks.delete(0, END)
			adst_entRno.focus()
			return
		mks = int(adst_entMarks.get())
		if mks>100:
			showerror("Mistake","Marks cannot be greater than 100")
			adst_entMarks.delete(0, END)
			adst_entMarks.focus()
			return
		if mks<0:
			showerror("Mistake","Marks cannot be less than 0")
			adst_entMarks.delete(0, END)
			adst_entMarks.focus()
			return
		marks = int(mks)

	
		cur.execute(sql % (rno,name,marks))
		con.commit()
		showinfo("Success","Row Inserted")
	except Exception as e:
		con.rollback()
		showerror("Issue", e)
	finally:
		if con is not None:
			con.close()
	adst_entRno.delete(0,END)
	adst_entName.delete(0,END)
	adst_entMarks.delete(0,END)
	adst_entRno.focus()



def upstSave():
	con = None
	try:
		con = connect("sms_database.db")
		cur = con.cursor()
		sql = "update students set name='%s', marks='%d'  where  rno='%d' "
		srno = upst_entRno.get()
		if len(srno) == 0:
			showerror("Mistake", "rno should not be empty")
			return
		if not srno.isdigit():
			showerror("Mistake", "rno should be positive integers only")
			upst_entRno.delete(0, END)
			upst_entRno.focus()
			return
		rno = int(srno)


		name = upst_entName.get()
		if not name.isalpha():
			showerror("Mistake","Name should contain alphabets only")
			upst_entName.delete(0,END)
			upst_entName.focus()
			return
		if len(name) < 2:
			showerror("Mistake","Name Should contain minimum two characters")
			return
		
		


		if len(upst_entMarks.get()) == 0:
			showerror("Mistake", "Please Enter Marks")
			return
		if not upst_entMarks.get().isdigit():
			showerror("Mistake", "Marks only in range 0-100")
			upst_entMarks.delete(0, END)
			upst_entRno.focus()
			return
		mks = int(upst_entMarks.get())
		if mks>100:
			showerror("Mistake","Marks cannot be greater than 100")
			upst_entMarks.delete(0, END)
			upst_entMarks.focus()
			return
		if mks<0:
			showerror("Mistake","Marks cannot be less than 0")
			upst_entMarks.delete(0, END)
			upst_entMarks.focus()
			return
		marks = int(mks)

	
		cur.execute(sql % (name,marks,rno))
		con.commit()
		if cur.rowcount > 0:
			showinfo("Success","Row Updated")
		else:
			showerror("Error","Record does not exist")
	except Exception as e:
		
		showerror("Update Issue", e)
		con.rollback()
	finally:
		if con is not None:
			con.close()
	upst_entRno.delete(0,END)
	upst_entName.delete(0,END)
	upst_entMarks.delete(0,END)
	upst_entRno.focus()


def destSave():
	try:
		con = connect("sms_database.db")
		cur = con.cursor()
		sql = "delete from students where rno = '%d' "
		srno = dest_entRno.get()
		if len(srno) == 0:
			showerror("Mistake", "rno should not be empty")
			return
		if not srno.isdigit():
			showerror("Mistake", "rno should be positive integers only")
			dest_entRno.delete(0, END)
			dest_entRno.focus()
			return
		rno = int(srno)
		cur.execute(sql % (rno))
		con.commit()
		if cur.rowcount > 0:
			showinfo("Success","Row Deleted")
		else:
			showerror("Error","Record does not exist")
	except Exception as e:
		
		showerror("Delete Issue", e)
		con.rollback()
	finally:
		if con is not None:
			con.close()
	dest_entRno.delete(0,END)
	dest_entRno.focus()


def chart():
	try:
		con = connect("sms_database.db")
		cur = con.cursor()
		sql = "select * from students"
		cur.execute(sql)
		data = cur.fetchall()              

		roll = []
		name = []
		mark = []	
	
		for d in data:
			roll.append(d[0])
			name.append(d[1])
			mark.append(d[2])
		x = np.arange(len(name))
		print("mark", mark)
		print("roll", roll)
		plt.bar(x, mark, label='mark', width=0.25)
		plt.bar(x+0.25,roll,label='roll',width=0.25)
		plt.xticks(x,name)
	
		for marks,roll in enumerate(roll):
			plt.text(marks + 0.27  , roll  , str(roll), color='orange',fontweight='bold',ha='center',va='bottom')

		for roll,marks in enumerate(mark):
			plt.text(roll  , marks  , str(marks), color='blue',fontweight='bold',ha='center',va='bottom')
	
		

		plt.xlabel("Names")
		plt.ylabel("Marks")
		plt.title("Batch Information")
		plt.grid()
		plt.legend(shadow=True)
		plt.show()	
	
	except Exception as e:
		showerror("graph issue ",e)
		con.rollback()                      
	finally:
		if con is not None:
			con.close()
		


root = Tk()
root.title("S. M. S.")
root.geometry("1150x500+90+90")

btnAdd = Button(root, text="Add", width=10, font=('arial',18,'bold'),command=f1)
btnView = Button(root, text="View", width=10, font=('arial',18,'bold'),command=f3)
btnUpdate = Button(root, text="Update", width=10, font=('arial',18,'bold'),command=f5)
btnDelete = Button(root, text="Delete", width=10, font=('arial',18,'bold'),command=f7)
btnCharts = Button(root, text="Charts", width=10, font=('arial',18,'bold'),command=chart)

lt = " Location: " + str(city) + " Temperature: " + str(temp)+"°C"
Qotd = " Headline: " + str(quote)
lblLocTemp = Label(root,text=lt,borderwidth=2,relief="ridge",font=('arial',18,'bold'))
lblQOTD = Label(root,text=Qotd, borderwidth=2,relief="solid",font=('arial',18,'bold'))

btnAdd.pack(pady=10)
btnView.pack(pady=10)
btnUpdate.pack(pady=10)
btnDelete.pack(pady=10)
btnCharts.pack(pady=10)
lblLocTemp.pack(pady=10)
lblQOTD.pack()



adst = Toplevel(root)
adst.title("Add St. ")
adst.geometry("500x500+400+100")

adst_lblRno = Label(adst, text="enter rno ", font=('arial',18,'bold'))
adst_lblName = Label(adst, text="enter name ", font=('arial',18,'bold'))
adst_lblMarks = Label(adst, text="enter marks ", font=('arial',18,'bold'))
adst_entRno = Entry(adst, bd=5, font=('arial',18,'bold'))
adst_entName = Entry(adst, bd=5, font=('arial',18,'bold'))
adst_entMarks = Entry(adst, bd=5, font=('arial',18,'bold'))
adst_btnSave = Button(adst, text="Save", font=('arial',18,'bold'),command=adstSave)
adst_btnBack = Button(adst, text="Back", font=('arial',18,'bold'),command=f2)

adst_lblRno.pack(pady=5)
adst_entRno.pack(pady=5)
adst_lblName.pack(pady=5)
adst_entName.pack(pady=5)
adst_lblMarks.pack(pady=5)
adst_entMarks.pack(pady=5)
adst_btnSave.pack(pady=5)
adst_btnBack.pack(pady=5)

adst.withdraw()





vist = Toplevel(root)
vist.title("View St. ")
vist.geometry("500x500+400+100")

vist_stData = ScrolledText(vist, width=35, height=10,font=('arial',18,'bold'))
vist_btnBack = Button(vist, text="Back", font=('arial',18,'bold'),command=f4)

vist_stData.pack(pady=10)
vist_btnBack.pack(pady=10)

vist.withdraw()



upst = Toplevel(root)
upst.title("Update St. ")
upst.geometry("500x500+400+100")

upst_lblRno = Label(upst, text="enter rno ", font=('arial',18,'bold'))
upst_lblName = Label(upst, text="enter name ", font=('arial',18,'bold'))
upst_lblMarks = Label(upst, text="enter marks ", font=('arial',18,'bold'))
upst_entRno = Entry(upst, bd=5, font=('arial',18,'bold'))
upst_entName = Entry(upst, bd=5, font=('arial',18,'bold'))
upst_entMarks = Entry(upst, bd=5, font=('arial',18,'bold'))
upst_btnSave = Button(upst, text="Save", font=('arial',18,'bold'),command=upstSave)
upst_btnBack = Button(upst, text="Back", font=('arial',18,'bold'),command=f6)

upst_lblRno.pack(pady=5)
upst_entRno.pack(pady=5)
upst_lblName.pack(pady=5)
upst_entName.pack(pady=5)
upst_lblMarks.pack(pady=5)
upst_entMarks.pack(pady=5)
upst_btnSave.pack(pady=5)
upst_btnBack.pack(pady=5)

upst.withdraw()



dest = Toplevel(root)
dest.title("Delete St. ")
dest.geometry("500x500+400+100")

dest_lblRno = Label(dest, text="enter rno ", font=('arial',18,'bold'))
dest_entRno = Entry(dest, bd=5, font=('arial',18,'bold'))
dest_btnSave = Button(dest, text="Save", font=('arial',18,'bold'),command=destSave)
dest_btnBack = Button(dest, text="Back", font=('arial',18,'bold'),command=f8)

dest_lblRno.pack(pady=5)
dest_entRno.pack(pady=5)
dest_btnSave.pack(pady=5)
dest_btnBack.pack(pady=5)

dest.withdraw()

root.mainloop()
























































