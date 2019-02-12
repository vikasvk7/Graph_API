import sqlite3

db = sqlite3.connect("Fb.db")

cursor = db.execute("SELECT * FROM MYDATA")
c = 0
for row in cursor :
    if(c==0):
        print("Name            ", "Gender             ", "Location          ", "Email         ", "Recent-Liked        ")
        print("--------------------------------------------------------------------------------- ")
    print(row[0],"  ",row[1],"  ",row[2],"  ",row[3],"  ",row[4])
    c+=1
#db.execute("DELETE FROM MYDATA WHERE NAME = ?",("Vikas Vishwakarma",)) To delete the name from table
db.commit()
db.close()