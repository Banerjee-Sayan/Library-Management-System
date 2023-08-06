import backend
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "library"
)
create_books_issue = """
CREATE TABLE bookissue(
    roll INT NOT NULL  PRIMARY KEY,
    name VARCHAR(20),
    author VARCHAR(100),
    Dateissue DATE,
    Datereturn DATE
    )
"""
create_library_subcription = """
CREATE TABLE librarysubsciption(
    Roll INT NOT NULL PRIMARY KEY,
    Name VARCHAR(20),
    Subscription_startdate DATE,
    Subscription_enddate DATE
)
"""
create_library_workshift = """
CREATE TABLE libraryworkshift(
  empid INT NOT NULL PRIMARY KEY,
  Name VARCHAR(20),
  shift VARCHAR(20),
  shift_start_time TIME,
  shift_end_time TIME
)
"""
# with mydb.cursor() as cursor: 
#     cursor.execute(create_books_issue)

# with mydb.cursor() as cursor:
#     cursor.execute(create_library_subcription)

# with mydb.cursor() as cursor:
#     cursor.execute(create_library_workshift)

# print("Database created")

print("............Library Management.............")
       
def main():
    c='y'
    while(c=='Y' or c=='y'):
        print("""
        1.Issue book
        2.Display Issued book
        3.Add Library Subscription
        4.Display Library Subscription
        5.Add Librarian Workshift
        6. Display Librarian Workshift
        """)
        choice = input("Enter task no:")
        print("............................")
        if(choice == '1'):
            backend.issueb(mydb)
        elif(choice == '2'):
            backend.displayb(mydb)
        elif(choice=='3'):
            backend.librarysubscriptionadd(mydb)
        elif(choice=='4'):
            backend.librarysubscriptiondisplay(mydb) 
        elif(choice=='5'):
            backend.libraryworkshiftadd(mydb) 
        elif(choice=='6'):
            backend.libraryworkshiftdisplay(mydb) 
        else:
             print("wrong choice")

        c = input("Do You want to continue? Y/N : ")    

main()