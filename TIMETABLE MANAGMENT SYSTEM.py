 
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import mysql.connector as mysqlcn 


class variableCaldron:
    def __init__(self,initialvalue):
        self.glcass = initialvalue
        self.glclassType=""
        self.gDBUserName="Dbserver"
        self.gDBPassword="db123"
        self.gDBName = "tmsdon"
        self.gColor1= "#303960"
        self.gColor2= "#ea9a96"
        self.gColor3= "#f8b24f"
        self.gColor4= "#e5e5e5"
        self.gSession=""
    def setvalue(self,newvalue):
        self.glcass = newvalue
        
    def getvalue(self):
        return self.glcass

    def setGlClassType(self,newvalue):
        self.glclasstype = newvalue
    def getGlClassType(self):
        return self.glclassType
 

    def getGDBUSER(self):
        return self.gDBUserName 

    def getGDPASSWORD(self):
        return self.gDBPassword

    def getDBNAME(self):
        return self.gDBName 
    
    def getGColor1(self):
        return self.gColor1
 
    def getGColor2(self):
        return self.gColor2
    def getGColor3(self):
        return self.gColor3
    def getGColor4(self):
        return self.gColor4
    def setGSession(self,newvalue):
        self.gSession = newvalue 
    def getGSession(self):
        return self.gSession  
    






 

def populateList(byWhat, byWhichOrWho,lst):
    # populate the list with dash's if any class period not allocated you will
    # a - at least! Enjoy folks
    lst+=["-","-","-","-","-","-"],
    lst+=["-","-","-","-","-","-"],
    lst+=["-","-","-","-","-","-"],
    lst+=["-","-","-","-","-","-"],
    lst+=["-","-","-","-","-","-"],
    lst+=["-","-","-","-","-","-"],
    lst+=["-","-","-","-","-","-"],

    
    mycon = mysqlcn.connect(host="localhost",user=vc.getGDBUSER(),passwd=vc.getGDPASSWORD(),
database="tmsdon")
    
    cursor = mycon.cursor()
    
    
    byWhichOrWho = vc.getvalue()



    
    query = " select A.did as did,A.pid as pid,A.cid as cid,A.tid as tid,\
                 A.sid as sid,d.dayname as dayname,c.classname as classname,\
                 p.pname as pname, concat(t.lastname,',',t.firstname) as tname,\
                 s.subjectname as subjectname\
                 from timetable A inner join days d on d.did = a.did\
                 inner join classes c on c.cid = a.cid\
                 inner join  periods p on p.pid = a.pid\
                 inner join teachers t on t.tid = a.tid\
                 inner join subjects s on s.sid = a.sid\
                where a.cid = {0} order by 1,2 ".format(byWhichOrWho)


    
    cursor.execute( query  )

    resultset = cursor.fetchall()
    

    
    for x in resultset:
        period=x[0]-1
        day=x[1]-1
        lst[day][period]=x[9]

     

    

def reportClassSubmit():
    
    mycon = mysqlcn.connect(host="localhost",user=vc.getGDBUSER(),passwd=vc.getGDPASSWORD(),
database="tmsdon")
    query=("Select cid,classname from classes")
    cursor = mycon.cursor()
    cname = repClassName.get()
    
    
    cursor.execute( query  )
    
    
    localclassid=-1
    resultset = cursor.fetchall()
    for r in resultset:
        if r[1].upper()==cname.upper():
            localclassid = int(r[0])
            
    
    if localclassid ==-1:
        mreport1.set("Sorry Class ID for that classs Not FOUND. Invalid Class Description")
    else:
        mreport1.set("Your Request Successfully Retrived Please Check Next tab for Data")

  
    vc.setvalue(localclassid)
    
    
def reports2():
    screen2 = tk.Toplevel(screen)
    screen2.title("Reports")
    screen2.geometry("800x500")    
    screen2.title("Time Table") 

    global lst
    
    lst = list()
    
    
    # for future  enhancement you can change from class to teacher
    byWhat="Class"
    byWhichOrWho=vc.getvalue()
    
    populateList(byWhat,byWhichOrWho,lst)
    
    dow=["","Mon","Tue","Wed","Thu","Fri","Sat"]
    period=["Period 1","Period 2","Period 3","Period 4","Period 5","Period 6"]
    
    tk.Label(screen2,text="Time Table",bg=vc.getGColor1(),font=("Calibri",16),fg="white",width=72).grid(row=0,
column=0,columnspan=7)
    #tk.Button(screen2,text="Get Data",command=getData(tab2,tabControl,dow,period,byWhat,byWhichOrWho)).grid(row=12,column=0,sticky="W")
    for r in range(1,8):
        for c in range(7):
            
            if r==1:
               if c!=0:
                   tk.Label(screen2,text=dow[c],bg=vc.getGColor2()  ,width=15,height=3).grid(row=r,column=c)
               else:
                   tk.Label(screen2,text=dow[c],bg=vc.getGColor3(),width=15,height=3).grid(row=r,
column=c)
            else:
               if c==0:
                   tk.Label(screen2,text=period[r-2],bg=vc.getGColor2(),width=15,height=3) .grid(row=r,column=c)
               else:
                   tk.Label(screen2,text=lst[r-2][c-1]).grid(row=r,column=c)
    
def reports():
    screen1 = tk.Toplevel(screen)
    screen1.title("Reports")
    screen1.geometry("800x500")    
    screen1.title("Report") 
   
    global mreport1
    global repClassName 
     

    
    
    mreport1 = tk.StringVar()
    
    repClassName = tk.StringVar() 
    


    # ----------------------------------------------- Removed TAB Due to Pack Issue
      #FOR TAB 1 Which Class do you want to retrive
    tk.Label(screen1,text="Time Table for Class",bg=vc.getGColor1() ,font=("Calibri",16), fg="white",width=72 ).grid(row=0,column=0,columnspan=6,sticky="W")
    #Empty Row that spans 6 Columsn
    tk.Label(screen1,text="").grid(row=1,column=0,columnspan=6) 
    #Empty Label omitting First Col
    tk.Label(screen1,text="").grid(row=2,column=0)
    tk.Label(screen1,text="Class Name").grid(row=2,column=1,sticky="W",columnspan=2)
  tk.Entry(screen1,textvariable=repClassName).grid(row=2,column=3,sticky="W",
columnspan=2)
    tk.Label(screen1,text="").grid(row=2,column=5)
    tk.Label(screen1,text="").grid(row=3,column=0,columnspan=6)
    # 
    tk.Label(screen1,text="").grid(row=4,column=0)
    tk.Label(screen1,text="").grid(row=4,column=1,sticky="W",columnspan=2)
    tk.Label(screen1).grid(row=4,column=3,sticky="W",columnspan=2)

    
    #Button
    tk.Label(screen1,text="").grid(row=5,column=0,columnspan=6) 
    tk.Label(screen1,text="").grid(row=6,column=0)
    tk.Button(screen1,text="Submit",command=reportClassSubmit).grid(row=6,column=1,
sticky="W")  
    
    
    #Message Box
    
    tk.Label(screen1,text="").grid(row=7,column=0,columnspan=6)
    tk.Label(screen1,font=("Calibri",14),textvariable=mreport1).grid(row=8,column=0,
columnspan=6)
    
    
    # ------------------------------------------------  TaB 2

    
    

    
    
def teacherSubmit():
    fn = fname.get()
    ln = lname.get()
    print("Teacher Submitted",fn," and ",ln) 
    mycon = mysqlcn.connect(host="localhost",user=vc.getGDBUSER(),passwd=vc.getGDPASSWORD(),
database="tmsdon")
    if mycon.is_connected:
        print("Sucessfully Connected")

    
    mycursor = mycon.cursor()

    sql = "INSERT INTO teachers (lastname, firstname) VALUES (%s, %s)"
    val = (ln, fn)
    mycursor.execute(sql, val)

    mycon.commit()
    
    str1 = "Successfully Inserted "+ln+" with ID=" + str(mycursor.lastrowid)
    m1.set(str1)
    mycon.close()

    
def classSubmit():
    cna = classname.get()
    print("Class Submitted with ",vc.getGDBUSER(), " and ",vc.getGDPASSWORD())

    mycon = mysqlcn.connect(host="localhost",user=vc.getGDBUSER(),passwd=vc.getGDPASSWORD(),
database="tmsdon")
    if mycon.is_connected:
        print("Sucessfully Connected")

    
    mycursor = mycon.cursor()

    sql = "INSERT INTO classes (Classname) VALUES ('"+cna+"');"

    
    
    tabControl.add(tab1, text='Teachers')
    tabControl.add(tab2, text='Classes')
    tabControl.add(tab3,text="Subjects") print(sql)
    mycursor.execute(sql)

    mycon.commit()
    #print("1 record inserted, ID:", mycursor.lastrowid) 
    str1 = "Successfully Inserted "+cna+" with ID=" + str(mycursor.lastrowid)
    m1.set(str1)
    mycon.close()
    #print("Class XIA XIB etc Submitted" , cn)   
    
    m2.set(str1)
    

    
def subjectSubmit():
    sn = subjectname.get()
    
    mycon = mysqlcn.connect(host="localhost",user=vc.getGDBUSER(),passwd=vc.getGDPASSWORD(),
database="tmsdon")
    if mycon.is_connected:
        print("Sucessfully Connected")

    
    mycursor = mycon.cursor()

    sql = "INSERT INTO Subjects (subjectname) VALUES ('"+sn+"');"

    
    print(sql)
    mycursor.execute(sql)

    mycon.commit()
    #print("1 record inserted, ID:", mycursor.lastrowid) 
    str1 = "Successfully Inserted "+sn+" with ID=" + str(mycursor.lastrowid)
    m1.set(str1)
    mycon.close()
    #print("Class XIA XIB etc Submitted" , cn)   
    
    m3.set(str1)

       
def masters():
    
    print("Coming to Masters from the main_screen")
    
    screen1 = tk.Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("460x350")    
    screen1.title("Master Details") 
   
    
    tabControl = ttk.Notebook(screen1) 
    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    tab3 = ttk.Frame(tabControl)

    tabControl.pack(expand=1, fill="both")  
    
    global fname 
    global lname 
    global classname 
    global subjectname 
    global m1
    global m2
    global m3
    
    
    
    fname = tk.StringVar()
    lname = tk.StringVar()
    classname = tk.StringVar()
    subjectname = tk.StringVar()
    
    m1 = tk.StringVar()
    m2 = tk.StringVar()
    m3 = tk.StringVar()
    
    #FOR TAB 1 Teacher Details
    tk.Label(tab1,text="Enter Teacher Details",bg=vc.getGColor1(),font=("Calibri",16), fg="white",width=41 ).grid(row=0,column=0,columnspan=6,sticky="W")
    #Empty Row that spans 6 Columsn
    tk.Label(tab1,text="").grid(row=1,column=0,columnspan=6) 
    #Empty Label omitting First Col
    tk.Label(tab1,text="").grid(row=2,column=0)
    tk.Label(tab1,text="First Name").grid(row=2,column=1,sticky="W",columnspan=2)
    tk.Entry(tab1,textvariable=fname).grid(row=2,column=3,sticky="W",columnspan=2)
    tk.Label(tab1,text="").grid(row=2,column=5)
    tk.Label(tab1,text="").grid(row=3,column=0,columnspan=6)
    # Last Name
    tk.Label(tab1,text="").grid(row=4,column=0)
    tk.Label(tab1,text="Last Name").grid(row=4,column=1,sticky="W",columnspan=2)
    tk.Entry(tab1,textvariable=lname).grid(row=4,column=3,sticky="W",columnspan=2)
    tk.Label(tab1,text="").grid(row=4,column=5)
    
    #Button
    tk.Label(tab1,text="").grid(row=5,column=0,columnspan=6) 
    tk.Label(tab1,text="").grid(row=6,column=0)
    tk.Button(tab1,text="Submit",command=teacherSubmit).grid(row=6,column=1,sticky=
"W")
    
    
    # Message Box

    tk.Label(tab1,text="").grid(row=7,column=0,columnspan=6)
    tk.Label(tab1,font=("Calibri",14),textvariable=m1).grid(row=8,column=0,columnspan
=6)

    #FOR TAB 2 Class Details
    tk.Label(tab2,text="Enter Class Details",bg=vc.getGColor1(),font=("Calibri",16), fg="white",width=41 ).grid(row=0,column=0,columnspan=6,sticky="W")
    #Empty Row that spans 6 Columsn
    tk.Label(tab2,text="").grid(row=1,column=0,columnspan=6) 
    #Empty Label omitting First Col
    tk.Label(tab2,text="").grid(row=2,column=0)
    tk.Label(tab2,text="Class Name").grid(row=2,column=1,sticky="W",columnspan=2)
    tk.Entry(tab2,textvariable=classname).grid(row=2,column=3,sticky="W",columnspan=2)
    tk.Label(tab2,text="").grid(row=2,column=5)
    tk.Label(tab2,text="").grid(row=3,column=0,columnspan=6)
    # Last Name
    tk.Label(tab2,text="").grid(row=4,column=0)
    tk.Label(tab2,text="").grid(row=4,column=1,sticky="W",columnspan=2)
    tk.Label(tab2).grid(row=4,column=3,sticky="W",columnspan=2)

    
    #Button
    tk.Label(tab2,text="").grid(row=5,column=0,columnspan=6) 
    tk.Label(tab2,text="").grid(row=6,column=0)
    tk.Button(tab2,text="Submit",command=classSubmit).grid(row=6,column=1,sticky="W")  
    
    # Message Box
    tk.Label(tab2,text="").grid(row=7,column=0,columnspan=6)
    tk.Label(tab2,font=("Calibri",14),textvariable=m2).grid(row=8,column=0,columnspan
=6)
    
    #FOR TAB 3 Subject Details
    tk.Label(tab3,text="Subject Details",bg=vc.getGColor1(),font=("Calibri",16), fg="white",width=41 ).grid(row=0,column=0,columnspan=6,sticky="W")
    #Empty Row that spans 6 Columsn
    tk.Label(tab3,text="").grid(row=1,column=0,columnspan=6) 
    #Empty Label omitting First Col
    tk.Label(tab3,text="").grid(row=2,column=0)
    tk.Label(tab3,text="Subject Name").grid(row=2,column=1,sticky="W",columnspan=2)
    tk.Entry(tab3,textvariable=subjectname).grid(row=2,column=3,sticky="W",columnspan
=2)
    tk.Label(tab3,text="").grid(row=2,column=5)
    tk.Label(tab3,text="").grid(row=3,column=0,columnspan=6)
    # 
    tk.Label(tab3,text="").grid(row=4,column=0)
    tk.Label(tab3,text="").grid(row=4,column=1,sticky="W",columnspan=2)
    tk.Label(tab3).grid(row=4,column=3,sticky="W",columnspan=2)

    
    #Button
    tk.Label(tab3,text="").grid(row=5,column=0,columnspan=6) 
    tk.Label(tab3,text="").grid(row=6,column=0)
    tk.Button(tab3,text="Submit",command=subjectSubmit).grid(row=6,column=1,sticky=
"W")  
    
    #Message Box
    
    tk.Label(tab3,text="").grid(row=7,column=0,columnspan=6)
    tk.Label(tab3,font=("Calibri",14),textvariable=m3).grid(row=8,column=0,columnspan
=6)
    
    tabControl.pack(fill="both")
    
def dbConnectAndPopulate(lllst,sqltxt):
    
    mycon = mysqlcn.connect(host="localhost",user=vc.getGDBUSER(),passwd=vc.getGDPASSWORD(),
database="tmsdon")
    query=(sqltxt)
    cursor = mycon.cursor()
   
    cursor.execute( query  )

    resultset = cursor.fetchall()
    
    for r in resultset:
        str1 =str( r[0])+" | " + str(r[1])
        lllst.append(str1)    
    cursor.close()
    mycon.close()
    
    
def populatTTList(dayId,periodId,classId,teacherId,subjectId):
    dbConnectAndPopulate(dayId,"Select did,dayname from days")
    
    dbConnectAndPopulate(periodId,"Select pid,pname from periods")
    
    dbConnectAndPopulate(classId,"Select cid,classname from classes")
      
    dbConnectAndPopulate(subjectId,"Select sid,subjectname from subjects")
    
    dbConnectAndPopulate(teacherId,"select tid,concat(lastname,',',firstname) as tname from teachers")

def getKey(str1):
    keylst = str1.split("|")
    intRetvalue = int(keylst[0])
    return intRetvalue
    
def ttSubmit():
    print("---------CLICK EVENT-----------------")
    print(ldid.get(),lcid.get(),lpid.get(),ltid.get(),lsid.get())

    kdid = getKey(ldid.get())
    kpid = getKey(lpid.get())
    ktid = getKey(ltid.get())
    kcid = getKey(lcid.get())
    ksid = getKey(lsid.get())
    
    mycon = mysqlcn.connect(host="localhost",user=vc.getGDBUSER(),passwd=vc.getGDPASSWORD(),
database="tmsdon")
    if mycon.is_connected:
        print("Sucessfully Connected")
    
    mycursor1 = mycon.cursor()
    mycursor2 = mycon.cursor()
    mycursor3 = mycon.cursor()
    
    sqlCheck = "select A.did as did,A.cid as CID,A.pid AS PID,A.tid AS TID,A.sid SID, d.dayname AS DAYNAME,c.classname AS CLASSNAME,p.pname AS PeriodName,        concat(t.lastname,',',t.firstname) AS TNAME ,s.subjectname AS SUBJECTNAME from timetable A inner join days d on d.did = a.did inner join classes 
c on c.cid = a.cid inner join  periods p on p.pid = a.pid inner join teachers t on t.tid = a.tid inner join subjects s 
on s.sid = a.sid where a.cid = {0} and a.pid ={1} and a.did = {2};".format(kcid,kpid,kdid)
    
    mycursor3.execute(sqlCheck)
    
    resultCheck = mycursor3.fetchall()
    
    TeacherName = ""

    SubjectName =""
    for r in resultCheck:
        TeacherName=r[8]

        SubjectName=r[9]

    if TeacherName!="":
        strMessForDialog="That class is allocated to "+TeacherName + " for Subject "+SubjectName+"!"
        MsgBox =tk.messagebox.askquestion("Do want to Reallocate?",strMessForDialog,icon="warning")
        if MsgBox=="yes":
            sqlDelete = "Delete from timetable where did={0} and cid={1} and pid={2}".format(kdid,kcid,kpid)
        
            mycursor1.execute(sqlDelete)
        else:
            return
    sqlINSERT = "INSERT INTO timetable (did,pid,cid,tid,sid ) VALUES ({0},{1},{2},{3},{4} )".format(kdid,kpid,kcid,ktid,ksid )
   
    try:
        mycursor2.execute(sqlINSERT)
        messageTxt.set("Successfully Inserted into timetable")
        print("------Inserted-------")
    except mysqlcn.Error as err:
        messageTxt.set("Error in Insert Probably the teacher is taking class at same time")
        print("{0} and error from db is {1}".format(sqlINSERT,err))
        
    finally:
        mycon.commit()
        mycon.close()     


    
    
    
    
def timetable():
    
    global periodId 
    global dayId
    global classId
    global teacherId
    global subjectId
    global messageTxt
    
    periodId=list()
    dayId = list()
    classId = list()
    teacherId = list()
    subjectId = list()
    
    global ldid
    global lpid
    global lcid
    global ltid
    global lsid
    
    
    messageTxt = tk.StringVar()
    ldid = tk.StringVar()
    lpid = tk.StringVar()
    lcid = tk.StringVar()
    ltid = tk.StringVar()
    lsid = tk.StringVar()
    
    populatTTList(dayId,periodId,classId,teacherId,subjectId)
    print(teacherId)
    print(subjectId)
    print(classId)  
    print(periodId)
    print(dayId)
    screen1 = tk.Toplevel(screen)
    screen1.title("Time Table")
    screen1.geometry("500x350")    
    screen1.title("Fill Time Table ") 
    tk.Label(screen1,text="Time Table Entry",bg=vc.getGColor1(),font=("Calibri",16), fg="white",width=45 ).grid(row=0,column=0,columnspan=6)
    #First Drop  Down
    tk.Label(screen1,text="").grid(row=1,column=0,columnspan=6)
    tk.Label(screen1,text="Enter Day ID").grid(row=4,column=2,sticky="w")
    #tk.Label(screen1,text="Drop Down Here").grid(row=2,column=3)
    daychosen = ttk.Combobox(screen1,width=20,textvariable=ldid)
    daychosen['values'] = (dayId)
    daychosen.grid(row=4,column=3)
    
    
    #Second Drop Down
    tk.Label(screen1,text="").grid(row=5,column=0,columnspan=6)
    tk.Label(screen1,text="Enter Period ID").grid(row=6,column=2,sticky="w")
    #tk.Label(screen1,text="Drop Down Here").grid(row=4,column=3)
    periodchosen = ttk.Combobox(screen1,width=20,textvariable=lpid)
    periodchosen['values'] = (periodId)
    periodchosen.grid(row=6,column=3)
    #Third Drop Down Teacher ID
    tk.Label(screen1,text="").grid(row=7,column=0,columnspan=6)
    tk.Label(screen1,text="Enter Teacher ID").grid(row=8,column=2,sticky="w")
    #tk.Label(screen1,text="Drop Down Here").grid(row=6,column=3)
    teacherchosen = ttk.Combobox(screen1,width=20,textvariable=ltid)
    teacherchosen['values'] = (teacherId)
    teacherchosen.grid(row=8,column=3)
    
    #Fourth Drop Down Class ID
    tk.Label(screen1,text="").grid(row=9,column=0,columnspan=6)
    tk.Label(screen1,text="Enter Class ID").grid(row=10,column=2,sticky="w")
    #tk.Label(screen1,text="Drop Down Here").grid(row=8,column=3) 
    classchosen = ttk.Combobox(screen1,width=20,textvariable=lcid)
    classchosen['values'] = (classId)
    classchosen.grid(row=10,column=3)    

    #Fifth Drop Down Subject ID
    tk.Label(screen1,text="").grid(row=11,column=0,columnspan=6)
    tk.Label(screen1,text="Enter Subject ID").grid(row=12,column=2,sticky="w")
    #tk.Label(screen1,text="Drop Down Here").grid(row=8,column=3)
    subjectchosen = ttk.Combobox(screen1,width=20,textvariable=lsid)
    subjectchosen['values'] = (subjectId)
    subjectchosen.grid(row=12,column=3)
    # command button here
    tk.Label(screen1,text="").grid(row=13,column=0,columnspan=6)
    tk.Button(screen1,text="Submit",command=ttSubmit).grid(row=14,column=1,sticky="W")
    
    
    #Empty Label before the messagebox
    tk.Label(screen1,text="").grid(row=15,column=0,columnspan=6)
    tk.Label(screen1,text="Test",font=("Calibri",10),textvariable=messageTxt, width=65,bg=vc.getGColor3()).grid(row=16,column=0,columnspan=6)                                            
    
def donothing():
    print("Doing Nothing")    
   
def doAbout():
    print("Wait.........")

    scrAbout = tk.Toplevel(screen  )
    scrAbout.title("About")
    scrAbout.geometry("500x350")    
    scrAbout.title("About ") 
    tk.Label(scrAbout,text="About ",bg="#303960",font=("Calibri",16), fg="white",width=45 ).grid(row=0,column=0,columnspan=6)

def main_screen():
    global screen
    
    global lblMainScreen 
    global btnMaster
    global btnTT
    global btnReport1
    global btnReport2
    global anlyticsmenu

    global vc
    
    vc = variableCaldron(-1)
    screen = tk.Tk()
    lblMainScreen = tk.StringVar()
   
    menubar = tk.Menu(screen)
    usermenu = tk.Menu(menubar, tearoff=0)
    usermenu.add_command(label="Login", command=login_screen  )
    usermenu.add_separator()
    #usermenu.add_command(label="New User", command=loginNewUser )
    #usermenu.add_separator()
    usermenu.add_command(label="Exit", command=screen.destroy)
    menubar.add_cascade(label="File", menu=usermenu)

    anlyticsmenu = tk.Menu(menubar,tearoff=0)
    anlyticsmenu.add_command(label="Analysis",command=doAnalysis)
    menubar.add_cascade(label="Reports",menu=anlyticsmenu)
    anlyticsmenu.entryconfig(1,state=tk.DISABLED)
    
    helpmenu = tk.Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Help", command=donothing)
    helpmenu.add_command(label="About...", command=doAbout)
    
    menubar.add_cascade(label="Help", menu=helpmenu)

    screen.config(menu=menubar)
    
    

    """
    if vc.getGSession()=="":
        print("----------Login Failure--------")
        screen.destroy()
        return 
    """
    screen.geometry("300x400")    
    screen.title("Main Screen")
    tk.Label(text="Time Table Management System",bg="#303960",fg="white",width="300",height="2",font=("Calibri",16)).pack()
    tk.Label(text="").pack()
    #
    btnMaster =tk.Button(text="Masters",height="2",width="30",command=masters )
    btnMaster.configure(state=tk.DISABLED)
    btnMaster.pack()
    
    
    tk.Label(text="").pack()
    #
    btnTT =tk.Button(text="Timetable",height="2",width="30",command=timetable)
    btnTT.configure(state=tk.DISABLED  )
    btnTT.pack()
    
    tk.Label(text="").pack()
    #
    btnReport1 =tk.Button(text="Report Selection",height="2",width="30",command=reports)
    btnReport1.configure(state=tk.DISABLED)
    btnReport1.pack()
    tk.Label(text="").pack()
    #
    btnReport2= tk.Button(text="View Time Table",height="2",width="30",command=reports2 )
    btnReport2.configure(state=tk.DISABLED)
    btnReport2.pack()
    
    tk.Label(text="").pack()
    tk.Label(text="",textvariable=lblMainScreen ).pack()
    screen.mainloop()



def analysisSubmit():
    print("Do Analysis for Teacher ID ",analysisTID.get())
    analysisTeacherID = getKey(analysisTID.get())
    print("The Key Value for the Teacher is ",analysisTeacherID)
    mycon = mysqlcn.connect(host="localhost",user=vc.getGDBUSER(),passwd=vc.getGDPASSWORD(),
database="tmsdon")
    
    if mycon.is_connected:
        print("Successfully Connected to MySQL")
    query = "select TT.did,TT.tid,count(TT.tid),  d.dayname, \
        concat(t.lastname,',',t.firstname) from timetable TT\
        inner join days D on D.DID = TT.did \
        inner join teachers t on t.TID = tt.tid \
        where tt.tid = {0} \
        group by tid,did;".format(  analysisTeacherID)
    
    cursor = mycon.cursor()
    
    cursor.execute(query)
    
    rs = cursor.fetchall()
    #dl = tuple() 
 
    tn =""
    d = dict()
    
    d = {"Mon":0,"Tue":0,"Wed":0,"Thu":0,"Fri":0,"Sat":0}
    
    for record in rs:
        #dl = dl + (record[3],)
#        cl.append(record[2])
        d[record[3]]=record[2]
        tn=record[4]
        

    print(d)

    y_pos = np.arange(len(d.keys()))

    pl.title("Classes by " + tn)
    pl.bar(y_pos,d.values(),color=vc.getGColor2())
    pl.xticks(y_pos,tuple(d.keys())  )
    ax =pl.gca()
    ax.set_facecolor( vc.getGColor1()  )
    pl.ylim(0,6)
    pl.show()
    
     

def doAnalysis():
    global lAnalysisTeacher
    global analysisTID 
    
    analysisTID = tk.StringVar()
    
    lAnalysisTeacher = list()
    #teacheCombo = ""
    dbConnectAndPopulate(lAnalysisTeacher,"select tid,concat(lastname,',',firstname) as tname from teachers")
    print("Analysis Screen") 
    scrAnalysis = tk.Toplevel(screen)
    scrAnalysis.geometry("500x350")
    scrAnalysis.title("Teacher Allocation")
    tk.Label(scrAnalysis,text="Teacher Allocation",bg="#303960",font=("Calibri",16), fg="white",width=45 ).grid(row=0,column=0,columnspan=6)
    tk.Label(scrAnalysis,text="").grid(row=1,column=0,columnspan=6)
    tk.Label(scrAnalysis,text="Enter Teacher ID").grid(row=2,column=2,sticky="w")
    #tk.Label(scrAnalysis1,text="Drop Down Here").grid(row=6,column=3)
    teacherCombo = ttk.Combobox(scrAnalysis,width=20,textvariable=analysisTID)
    teacherCombo['values'] = ( lAnalysisTeacher)
    teacherCombo.grid(row=2,column=3)
    tk.Label(scrAnalysis,text="").grid(row=3,column=0,columnspan=6)
    tk.Button(scrAnalysis,text="Submit",command=analysisSubmit).grid(row=4,column=2,sticky="W") 
    



    
def checkUser(un,pw):
    
    foundflag=False 
   

    if un=="admin" and pw=="admin":
        foundflag=True 

    
    if foundflag==True:
        print("--------------Success-----------------")
        btnMaster["state"]=tk.NORMAL
        btnTT["state"]=tk.NORMAL
        btnReport1["state"] = tk.NORMAL
        btnReport2["state"]=tk.NORMAL
        return True
    else:
        return False    
    
def loginSubmit():
    #print("Login Submitted with", lsUname.get() ," and ",lsPassword.get()   ) 
    
    
    if checkUser( lsUname.get(),  lsPassword.get()) == True:
        vc.setGSession(lsUname.get()) 
        lsMessage.set("Welcome to TMS")
    else:
        lsMessage.set("Invalid User Name or Password")

def login_screen():
    
    global scrLogin 
 
    scrLogin = tk.Toplevel(screen  )
    #scrLogin = tk.Tk()

    global lsUname
    global lsPassword 
    global lsMessage
    
    global txtUname
    global txtPass
    global lblLoginScreen 
    

    lsUname = tk.StringVar()
    lsPassword = tk.StringVar()
    lsMessage = tk.StringVar()    

    
    
    scrLogin.title("Time Table")
    scrLogin.geometry("500x350")    
    scrLogin.title("Login ") 
    tk.Label(scrLogin,text="Login",bg="#303960",font=("Calibri",16), fg="white",width=45 ).grid(row=0,column=0,columnspan=6)

    tk.Label(scrLogin,text="").grid(row=2,column=0)
    tk.Label(scrLogin,text="User Name").grid(row=3,column=1,sticky="W",columnspan=2)
    txtUname = tk.Entry(scrLogin,textvariable=lsUname  ).grid(row=3,column=2,sticky="W",columnspan=2)
    tk.Label(scrLogin,text="").grid(row=4,column=0)
    tk.Label(scrLogin,text="Password").grid(row=5,column=1,sticky="W",columnspan=2)
    txtPass = tk.Entry(scrLogin,textvariable=lsPassword  ,show="*").grid(row=5,column=2,sticky="W",columnspan=2)
    tk.Label(scrLogin,text="").grid(row=6,column=5,columnspan=6)
    
    #Button
    

    tk.Button(scrLogin,text="Submit",command=loginSubmit).grid(row=7,column=1,sticky="W")
    #tk.Button(scrLogin,text="New User?",command=loginNewUser).grid(row=7,column=4,sticky="W")
     
    # Message Box

    tk.Label(scrLogin,text="").grid(row=7,column=0,columnspan=6)
    lblLoginScreen = tk.Label(scrLogin,font=("Calibri",14),textvariable=lsMessage   ,text="Welcome to login").grid(row=8,column=0,columnspan=6)


    



main_screen()  

