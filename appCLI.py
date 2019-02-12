import facebook
import json
import requests #to get the data, but here it is not used
import sqlite3 #Database library

db = sqlite3.connect("Fb.db")
db.execute("CREATE TABLE IF NOT EXISTS MYDATA (NAME CHAR[40],GENDER CHAR[10],LOCATION CHAR[30], EMAIL CHAR[50], RECENT_LIKED CHAR[30])")

#The user access token
token = 'EAAEaeLJJaZAwBAHwZA9SxHYfOQE058ywmTOWZAsFEYGRbxsCE1FJ4cPjgBzz9N0222ZBwLKZCXaoBzr23JnaVG7VSI8rYqvRAfFoOpiPZCiZA6lFFN8NFjQzx3iS834tsg6FEtp7w1ZC7ZBByuA0tH5BLnZCpoPBJb5Au6ZAvcFsjz99aZBqniK5xdt4PnYTdRYtb6ZCZBAIZCmKGpL3gZDZD'

graph = facebook.GraphAPI(token)

#My details stored in posts
posts = graph.get_object('me',fields = 'name,gender,email,location,likes')

#retrieving the data from json file
name = posts['name']
gender = posts['gender']
email = posts['email']
loc = posts['location']['name']
likes = posts['likes']['data']
pages= []
i =0
#Upto recent 10 pages of likings
while(i<10):
    try:
        pages.append(likes[i]['name'])
    except KeyError:
        pass
    i+=1
recent_liked = pages[0]
ans = input("Insert Data or not?(y/n) ")
if(ans=="y"):
    db.execute("INSERT INTO MYDATA(NAME, GENDER, LOCATION, EMAIL, RECENT_LIKED) VALUES(?,?,?,?,?)",(name,gender,loc,email,recent_liked));
db.commit()
db.close()


