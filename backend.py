from datetime import datetime

def is_valid_date(date_string):
    try:
        datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def is_valid_time(time_string):
    try:
        # Try to parse the time string using the specified format
        datetime.strptime(time_string, "%H:%M:%S")
        return True
    except ValueError:
        return False


def issueb(mydb):
    try:    
        roll  = input("Enter rollno:")
        name = input("Enter name:")
        author = input("Enter author name :")
        #checking for valid issue date
        flag=0
        while(flag==0):
            Date = input("Enter issue date: yyyy-mm-dd")
            if is_valid_date(Date):
                Dateissue =Date
                flag=1
            else:
                print("Invalid date format.")
                flag=0
        #checking for valid return date
        flag=0
        while(flag==0):
            Date = input("Enter return date yyyy-mm-dd")
            if is_valid_date(Date):
                Datereturn =Date
                flag=1
            else:
                print("Invalid date format.")
                flag=0            
        sql  = "insert into bookissue(roll,name,author,Dateissue,Datereturn) values(%s,%s,%s,%s,%s)"
        data =(roll,name,author,Dateissue,Datereturn)
        c = mydb.cursor()
        c.execute(sql,data)
        mydb.commit()
        print("...............")
        print("Book issued to :",name)
    except IntegrityError as e:
        print("Duplicate Entry:", str(e))
    except Error as e:
        print("An error occurred:", str(e))   
    
    
   


def displayb(mydb):
    try:
        sql = "select * from bookissue"
        c = mydb.cursor()
        c.execute(sql)
        myresult = c.fetchall()
        for i in myresult:
            print("Roll No:",i[0])
            print("Name:",i[1])
            print("Author:",i[2])
            print("Dateissue:",i[3])
            print("Datereturn:",i[4])
            print("................")    

    except Exception:
        print("An error occurred Please Try Again!!")   
    
def librarysubscriptionadd(mydb):
    try:

        Roll  = input("Enter rollno:")
        Name = input("Enter name:")
         #checking for valid issue date
        flag=0
        while(flag==0):
            Date = input("Enter Start date: YYYY-MM-DD")
            if is_valid_date(Date):
                Subscription_startdate =Date
                flag=1
            else:
                print("Invalid date format.")
                flag=0
        #checking for valid return date
        flag=0
        while(flag==0):
            Date = input("Enter End date: YYYY/MM/DD")
            if is_valid_date(Date):
                Subscription_enddate =Date
                flag=1
            else:
                print("Invalid date format.")
                flag=0
        
        sql  = "insert into librarysubsciption(Roll,Name,Subscription_startdate,Subscription_enddate) values(%s,%s,%s,%s)"
        data =(Roll,Name,Subscription_startdate,Subscription_enddate)
        c = mydb.cursor()
        c.execute(sql,data)
        mydb.commit()
        print("...............")
        print("Subscription Added  to :",Name)


    except IntegrityError as e:
        print("Duplicate Entry:", str(e))
    except Error as e:
        print("An error occurred:", str(e))

def librarysubscriptiondisplay(mydb):
    try:
        sql = "select * from librarysubsciption"
        c = mydb.cursor()
        c.execute(sql)
        myresult = c.fetchall()
        for i in myresult:
            print("Roll No:",i[0])
            print("Name:",i[1])
            print("Subscription Start Date:",i[2])
            print("Subscription End date:",i[3])
            print("................") 
    except Exception:
        print("An error occurred Please Try Again!!")          


def libraryworkshiftadd(mydb):
    try:
        empid  = input("Enter Empid:")
        Name = input("Enter name:")
        shift = input("Enter Shift:")
         #checking for valid time
        flag=0
        while(flag==0):
            time =  input("Enter shift start time 24 hrs format hh:mm:ss : ")
            if is_valid_time(time):
                shift_start_time=time
                flag=1
            else:
                print("Invalid time format.")
                flag=0

        #checking for valid return date
        flag=0
        while(flag==0):
            time =  input("Enter shift End time 24 hrs format hh:mm:ss : ")
            if is_valid_time(time):
                shift_end_time=time
                flag=1
            else:
                print("Invalid time format.")
                flag=0
        

        sql  = "insert into libraryworkshift(empid,Name,shift,shift_start_time, shift_end_time) values(%s,%s,%s,%s,%s)"
        data =(empid,Name,shift,shift_start_time, shift_end_time)
        c = mydb.cursor()
        c.execute(sql,data)
        mydb.commit()
        print("...............")
        print("Librarian Workshift added Succesfully!! ")

    except IntegrityError as e:
        print("Duplicate Entry:", str(e))
    except Error as e:
        print("An error occurred:", str(e))     


def libraryworkshiftdisplay(mydb):
    try:
        sql = "select * from libraryworkshift"
        c = mydb.cursor()
        c.execute(sql)
        myresult = c.fetchall()
        for i in myresult:
            print("EMP id:",i[0])
            print("Name:",i[1])
            print("Shift:",i[2])
            print("Shift start Time",i[3])
            print("Shift end Time",i[4])
            print("................")   
    except Exception:
        print("An error occurred Please Try Again!!") 