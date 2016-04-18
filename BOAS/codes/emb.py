#!/usr/bin/python

import serial
import sqlite3
import time


global E1
global idd


def enrol_stu(stu_name):
    conn = sqlite3.connect("/var/www/html/login/emb.db");
    curs = conn.cursor();
    to_db = [stu_name,idd,0,'lnmiit','test@gmail.com',40];
    curs.execute("INSERT INTO STU_DETAILS (NAME,ID,PRESENT,PASSWORD,EMAIL,TOTAL) VALUES (?, ?, ?, ?, ?, ?);", to_db);
    conn.commit()
    print("Student with id %s is enrolled succesfully!!" % idd)


def delete_all():
	conn = sqlite3.connect("/var/www/html/login/emb.db");
	curs = conn.cursor();
	curs.execute("DELETE FROM STU_DETAILS")
	print("All Records Deleted Successfully")
	conn.commit()


def veriffy_stu(idd):
    var_2=[idd]
    var_3=var_2[0]
    conn = sqlite3.connect('/var/www/html/login/emb.db')
    c = conn.cursor()
    c.execute('SELECT PRESENT FROM STU_DETAILS WHERE ID=?', var_2)
    tmp=c.fetchone()
    var_4=tmp[0]+1
    c.execute("UPDATE STU_DETAILS SET PRESENT=? WHERE ID=?", (var_4, var_3))
    print("Student with id %s is verified succesfully!!" % var_3)
    conn.commit()




if __name__ == '__main__':
    
    time.sleep(1)    
    ser = serial.Serial('/dev/ttyUSB0',9600,timeout=.1)
    time.sleep(1)
    try:
    	while True:
    		data=ser.readline()[:-2]
    		if data:
    			a=data.split(",")
    			print(data)
    			if(a[0]=='e'):
    				idd=int(a[1])
    				print a[1]
    				nam=raw_input('Enter a name:')
    				enrol_stu(nam)
    			elif(a[0]=='d'):
    				print(a[0])
    				delete_all()
    			elif(a[0]=='v'):
    				if(int(a[1])==250):
    					print("No Record Found!!!")
    				else:
    					idd=int(a[1])
    					veriffy_stu(idd)
    					   				
    			else:
    				print("Try Again!!!")
    except NameError as e:
    	print("Enter valid details!!")
    except IndexError as e:
    	print("There is some error!!!")
