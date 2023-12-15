import mysql.connector
from tabulate import tabulate

pa=input("Enter password of MYSQL DATABASE : ")

db=input("Enter name of your database: ")
database = mysql.connector.connect(host="localhost", user="root", passwd=pa)
query = database.cursor()
sql="create database if not exists %s" %(db,)
query.execute(sql)
query.execute('use '+db)
tablename=input("Name of your table: ")
query2 = "CREATE TABLE IF NOT EXISTS "+tablename+"\
         (ProductID VARCHAR(20), Name VARCHAR(20), Brand VARCHAR(20),Cost VARCHAR(20))"
query.execute(query2)


#SPLASH SCREEN (HEADER) TEXT
print('''
 Welcome to BillSys v1.0 
 A complete Product management system.
 :::::::::::::::::::::::::::::::::::::STARTING SYSTEM:::::::::::::::::::::::::::::::::::::
          ''')



#SEPERATE MODULES OR FUNCTIONS

def newProduct():
        L=[]
        ProductID = input("Enter product ID: ")
        L.append(ProductID)
        Name = input("Enter the name of the product: ")
        L.append(Name)
        Brand = input("Enter the brand or make: ")
        L.append(Brand)
        Cost = int(input("Enter the cost of the product: "))
        L.append(Cost)
        data = (L)
        query3 = "INSERT INTO "+tablename+" (ProductID, Name, Brand, Cost) VALUES (%s,%s,%s,%s)"
        query.execute(query3,data)
        database.commit()
        print ("Product added successfully.")

def fetchInfo():
        print("How do you want to fetch information for the product? : ")
        print("1. By Product ID")
        print("2. By Product Name")
        print("3. By Product Brand & Make")
        print("4. By Product Cost")
        ch = int(input("Enter your choice : "))
        if ch == 1:
                s = input("Enter product ID : ")
                rl = (s,)
                sql = "SELECT * FROM "+tablename+" WHERE ProductID=%s"
                query.execute(sql,rl)
                print(tabulate(query, headers="keys", tablefmt="fancy_grid"))              
        elif ch == 2:
                s = input("Enter product name : ")
                rl = (s,)
                sql = "SELECT * FROM "+tablename+" WHERE Name=%s"
                query.execute(sql,rl)
                print(tabulate(query, headers="keys", tablefmt="fancy_grid"))
        elif ch == 3:
                s = input("Enter product brand : ")
                rl = (s,)
                sql = "SELECT * FROM "+tablename+" WHERE Brand=%s"
                query.execute(sql,rl)
                print(tabulate(query, headers="keys", tablefmt="fancy_grid"))
        elif ch == 4:
                s = input("Enter product cost : ")
                rl = (s,)
                sql = "SELECT * FROM "+tablename+" WHERE Cost=%s"
                query.execute(sql,rl)
                print(tabulate(query, headers="keys", tablefmt="fancy_grid"))

def modProduct():
    print("How do you want to do ?")
    print("1. Delete any Product.")
    print("2. Change the values of Product.")
    c=int(input("Enter your choice: "))
    if c==1:
        ProductID=input("Enter ID of the product to be deleted : ")
        rl=(ProductID,)
        sql="DELETE FROM "+tablename+" WHERE ProductID=%s"
        query.execute(sql,rl)
        database.commit()
        print("Product deleted successfully !")
    elif c==2:
        print("What do you want to Change?")
        print("1. ProductID")
        print("2. Name")
        print("3. Brand")
        print("4. Cost")
        e=int(input("Enter your choice: "))
        if e==1:
            s=input("Enter current ProductID you want to change: ")
            f=input("Enter new ProductID: ")
            sql='update '+tablename+' set ProductID="'+f+'" where ProductID="'+s+'"'
            print(sql)
            query.execute(sql)
            database.commit()
            print("ProductID changed successfully !")
        elif e==2:
            s=input("Enter current Name you want to change: ")
            f=input("Enter new Name: ")
            sql='update '+tablename+' set Name="'+f+'" where Name="'+s+'"'
            query.execute(sql)
            database.commit()
            print("Name changed successfully !")
        elif e==3:
            s=input("Enter current Brand you want to change: ")
            f=input("Enter new Brand: ")
            sql='update '+tablename+' set Brand="'+f+'" where Brand="'+s+'"'
            query.execute(sql)
            database.commit()
            print("Brand changed successfully !")
        elif e==4:
            s=input("Enter current Cost you want to change: ")
            f=input("Enter new Cost: ")
            sql='update '+tablename+' set Cost="'+f+'" where Cost="'+s+'"'
            query.execute(sql)
            database.commit()
            print("Cost changed successfully !")

def disp():
    sql="select * from "+tablename
    query.execute(sql)
    print(tabulate(query, headers="keys", tablefmt="fancy_grid"))


#MAIN PROGRAM STARTS HERE
while True:
        print("\nSo what would you like to do?")
        print("1. Enter a new product.")
        print("2. Fetch a product infomation.")
        print("3. Modify product.")
        print("4. Display all product .")
        print("5. Exit BillSys.")
        Input = int(input("Please Select An Above Option(1,2,3,4): "))        
        print("\n")                                    
        if(Input == 1):
                newProduct()
        elif(Input==2):
                fetchInfo()
        elif(Input==3):
                modProduct()
        elif(Input==4):
                disp()
        elif (Input==5):
                print("Thanks for using!")
                break
