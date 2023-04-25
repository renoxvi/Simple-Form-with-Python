import mysql.connector
import webbrowser

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="reninhospital"
)

if mydb.is_connected():
  print("Connected to database")

firstName = input("Enter first name: ").strip()
middleName = input("Enter middle name: ").strip()
surname = input("Enter surname: ").strip()
dob = input("Enter birth date: ").strip()
gender = input("Enter gender: ").strip()
county = input("Enter county: ").strip()

mycursor = mydb.cursor()
sql = "INSERT INTO patients (`First Name`, `Middle Name`, Surname, `Date of Birth`, Gender, County) VALUES (%s, %s, %s, %s, %s, %s)"
values = (firstName, middleName, surname, dob, gender, county)
mycursor.execute(sql, values)
mydb.commit()

print(mycursor.rowcount, "record inserted.")
