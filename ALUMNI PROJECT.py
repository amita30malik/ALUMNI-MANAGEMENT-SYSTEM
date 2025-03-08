print("================================ ALUMNI MANAGEMENT SYSTEM===============================")
import os
import platform
import mysql.connector as am
import greetmodule
con= am.connect(host="localhost",user="root",password="root",database="aldb")
print(con)
cur=con.cursor()

def RegisterAlumni():
    L=[]
    fname=input("ENTER YOUR FIRST NAME :")
    L.append(fname)
    lname=input("ENTER YOUR LAST NAME :")
    L.append(lname) 
    dob=input("ENTER DOB IN YYYY-MM-DD FORMAT : ")
    L.append(dob)
    gender=input("ENTER YOUR GENDER :")
    L.append(gender)
    add_c=input("ENTER YOUR CORRESPONDENCE ADDRESS :")
    L.append(add_c)
    add_of=input("ENTER YOUR OFFICIAL ADDRESS :")
    L.append(add_of)
    email=input("ENTER YOUR EMAIL ADDRESS Ex: aa@gmail.com: ")
    L.append(email) 
    mob=input("ENTER YOUR MOBILE NO : ") 
    L.append(mob) 
    cur_c=input("ENTER THE CITY NAME YOU STAY : ") 
    L.append(cur_c) 
    com=input("ENTER COMPANY/ORGANIZATION YOU ARE WORKING : ")
    L.append(com) 
    desg=input("ENTER YOUR DESIGNATION IN COMPANY/ORGANIZATION : ")
    L.append(desg) 
    start_y=input("ENTER YOUR SESSION START YEAR IN COLLEGE: ")
    L.append(start_y) 
    start_e=input("ENTER YOUR SESSION END YEAR IN COLLEGE : ")
    L.append(start_e) 
    branch=input("ENTER YOUR BRANCH IN COLLEGE : ") 
    L.append(branch) 
    alu_id="al"+fname[0:2]+lname[0:2]+mob[0:4] 
    L.insert(0,alu_id)
    alumni=(L)
    sql="insert into alureg(alu_id,first_name,last_name,dob,gender,add_corr,add_offc,email_add,mob_no,curr_city,curr_company,desg,session_from,session_to,branch) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" 
    cur.execute(sql,alumni) 
    con.commit() 
    print("You Have Been Succesfully Registered: This is You AlumniID ,Use This For  Further Correspondence") 
    print(alu_id)
 
def ViewAlumniDetails(): 
     print("Select the search criteria to View Details : ") 
     print("1. Fname") 
     print("2. Lname") 
     print("3. Company") 
     print("4. Stream") 
     print("5. City") 
     print("6. Session Start") 
     print("7. To View All Records") 
     ch=int(input("Enter the choice : ")) 
     if ch==1 : 
          s=input("Enter First Name to Be Searched For") 
          rl=(s,) 
          sql="select * from alureg where First_name like %s" 
          cur.execute(sql,rl) 
     elif ch==2: 
          s=input("Enter Last Name to Be Searched For") 
          rl=(s,) 
          sql="select * from alureg where Last_name like %s" 
          cur.execute(sql,rl) 
     elif ch==3: 
          s=input("Enter Company Name to Be Searched For") 
          rl=(s,) 
          sql="select * from alureg where curr_company=%s" 
          cur.execute(sql,rl) 
     elif ch==4: 
          s=input("Enter Stream : ") 
          rl=(s,) 
          sql="select * from alureg where Branch=%s" 
          cur.execute(sql,rl) 
     elif ch==5: 
          s=input("Enter City : ") 
          rl=(s,) 
          sql="select * from alureg where curr_city=%s" 
          cur.execute(sql,rl) 
     elif ch==6: 
          s=input("Enter Session Start Year ") 
          rl=(s,) 
          sql="select * from alureg where session_from=%s" 
          cur.execute(sql,rl) 
     elif ch==7: 
          sql="select * from alureg" 
          cur.execute(sql) 
     res=cur.fetchall() 
     print("The Alumni Details are as Follows") 
     print("(alu_id,First_name,Last_name,DOB,Gender,Add_corr,Add_offc,email_add,mob_no,curr_city,curr_company,Desg,Session_from,Session_to,Branch)") 
     for x in res: 
            print(x) 


def EditAlumni(): 
  alu_id=input("Enter Alumni ID to be edited : ")
  sql="select * from alureg where alu_id=%s" 
  ed=(alu_id,) 
  cur.execute(sql,ed) 
  res=cur.fetchall() 
  for x in res: 
    print(x) 
  print("") 
  fld=input("Enter the field which you want to edit : ") 
  val=input("Enter the value you want to set : ") 
  sql="Update alureg set " + fld +"='" + val + "' where alu_id='" + alu_id + "'"
  sq=sql 
  cur.execute(sql) 
  print("Editing Done : ") 
  print("After correction the record is : ") 
  sql="select * from alureg where alu_id=%s" 
  ed=(alu_id,) 
  cur.execute(sql,ed) 
  res=cur.fetchall() 
  for x in res: 
    print(x) 
  con.commit()


def SearchAlumni(): 
 print("Enter The Alumni ID") 
 alu_id=input("Enter the Alumni ID for the alumni to be viewed : ")
 sql="select * from alureg where alu_id=%s" 
 rl=(alu_id,) 
 cur.execute(sql,rl) 
 res=cur.fetchall() 
 if res==None: 
     print("Record not Found . . . ") 
     return 
 print("The details of the students are : " ) 
 print("(alu_id,First_name,Last_name,DOB,Gender,Add_corr,Add_offc,email_add,mob_no,curr_city,curr_company,Desg,Session_from,Session_to,Branch)") 
 for x in res: 
      print(x)
      
def DeleteAlumni(): 
 alu_id=input("Enter the Alumni ID for the alumni to be deleted : ")
 sql="Delete from alureg where alu_id=%s" 
 rl=(alu_id,) 
 cur.execute(sql,rl) 
 con.commit()
  
def ScheduleEvent(): 
 E=[] 
 ename=input("Enter Event Name to Schedule : ") 
 E.append(ename) 
 edate=input("Enter Event Date in YYYY-MM-DD :") 
 E.append(edate) 
 evenue=input("Enter Venue of Event :") 
 E.append(evenue) 
 estat=input("Enter Event Statut as Completed Or Not Completed :")
 E.append(estat) 
 event=(E)  
 sql="insert into event (event_name,event_date,venue,statut) values (%s,%s,%s,%s)"
 cur.execute(sql,event) 
 con.commit() 
 print("You Have Succesfully Added A Event")
 
def ViewEventDetails(): 
 print("Select the search criteria to View Event Details : ")
 print("1. Event Name") 
 print("2. Venue") 
 print("3. Statut") 
 print("4. To View All Records") 
 ch=int(input("Enter the choice : ")) 
 if ch==1 : 
     s=input("Enter Event Name to Be Searched For")
     rl=(s,) 
     sql="select * from event where event_name like %s"
     cur.execute(sql,rl) 
 elif ch==2: 
     s=input("Enter Venue Name to Be Searched For")
     rl=(s,) 
     sql="select * from event where event like %s"
     cur.execute(sql,rl) 
 elif ch==3: 
     s=input("Enter Statut to Be Searched For")
     rl=(s,) 
     sql="select * from event where statut=%s"
     cur.execute(sql,rl) 
 elif ch==4: 
     sql="select * from event" 
     cur.execute(sql) 
     res=cur.fetchall() 
     print("The Event Details are as Follows") 
     print("(Event_Name,Event_Date,Venue,Statut)") 
     for x in res: 
           print(x) 
  
def DeleteEvent(): 
 ename=input("Enter the Event Name to be deleted : ")
 sql="Delete from event where event_name=%s" 
 rl=(ename,) 
 cur.execute(sql,rl) 
 con.commit() 

def MainMenu(): 
  print("Enter 1 : To Register Alumni") 
  print("Enter 2 : To View Alumni Details ") 
  print("Enter 3 : To Edit Alumni Details ") 
  print("Enter 4 : To Search Alumni ") 
  print("Enter 5 : To delete Alumni") 
  print("Enter 6 : To Add a Event") 
  print("Enter 7 : To Search a Event") 
  print("Enter 8 : To Delete a Event") 
  try: 
    userInput = int(input("Please Select An Above Option: "))
  except ValueError: 
        exit("You Had Entered Wrong Choice") 
  else: 
   print("\n") 
   if(userInput == 1): 
     RegisterAlumni() 
   elif (userInput==2): 
      ViewAlumniDetails() 
   elif (userInput==3): 
      EditAlumni() 
   elif (userInput==4):
      SearchAlumni() 
   elif (userInput==5): 
      DeleteAlumni() 
   elif (userInput==6): 
      ScheduleEvent() 
   elif (userInput==7): 
      ViewEventDetails() 
   elif (userInput==8): 
      DeleteEvent() 
   else: 
       print("Enter correct choice. . . ") 
  
MainMenu() 
def AskChoiceAgain(): 
  AksChcRun = input("\nwant To Run Again Y/n: ") 
  while(AksChcRun.lower() == 'y'): 
       if(platform.system() == "Windows"): 
             print(os.system('cls')) 
       else: 
             print(os.system('clear')) 
       MainMenu() 
       AksChcRun = input("\nwant To Run Again Y/n: ") 
AskChoiceAgain()














