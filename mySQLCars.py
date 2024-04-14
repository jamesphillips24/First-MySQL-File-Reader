import csv
import mysql.connector

#Program to read a csv file, turn any 'nan's to zeroes, put it in a mysql table,
#and print it to the console.

#Fancy database stuff
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="testdatabase"
)

#declare cursor
cursor = db.cursor()

#create the table
cursor.execute("CREATE TABLE Cars (id INT PRIMARY KEY AUTO_INCREMENT, mpg FLOAT, cylinders FLOAT, engine FLOAT, horsepower FLOAT, weight FLOAT, acceleration FLOAT, year FLOAT, origin VARCHAR(50), name VARCHAR(50))")

#Reading the file, skip the header, use csv.reader to read through it.
#For each element in each row, if the element is nan, turn it to zero.
#Try to convert the element to float, otherwise keep it as a string
with open("Car performance data.csv", "r") as file:
    next(file)
    f = csv.reader(file)
    for x in f:
        for y in range(len(x)):
            if x[y] == 'nan':
                x[y] = 0
            try:
                x[y] = float(x[y])
            except:
                continue
        cursor.execute("INSERT INTO Cars (mpg, cylinders, engine, horsepower, weight, acceleration, year, origin, name) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8]))

db.commit()

cursor.execute("SELECT * FROM Cars")

for x in cursor:
    print(x)