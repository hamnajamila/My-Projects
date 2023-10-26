import csv
import datetime

datenow = datetime.datetime.today()
datelab = datetime.timedelta(days=14)
lastdate = datenow+datelab

places=['1','2','3','4','5','6','7','8','9']
library_books = ['Harry Potter','Lord of the rings','Lupin','To Kill a Mockingbird',
                'One Hundred Years of Solitude','Invisible Man','The Lion, the Witch, and the Wardrobe',
                'The Book Thief','Animal Farm','Little Women']
def book_names():
  print("Index",":","Books Names")
  for i in range(len(library_books)):
    print(" "*1,i," ",":",library_books[i])

global data
def activities(data):
  with open("library.csv","a") as library:
    add_data=csv.writer(library)
    add_data.writerow(data)
     

def record():
  with open("library.csv","r") as library:
    records=csv.reader(library)
    for rows in records:
      print(rows)

def admin():
    print('\n----------------------------------------------')
    print('-                                            -')
    print('-          Welcome to our Library            -')
    print('-                                            -')
    print('----------------------------------------------')
    print()
    while True:
        status="Admin"
        print("Enter 1 to add a book")
        print("Enter 2 to issue a book")
        print("Enter 3 to view available books")
        print("Enter 4 to delete a book")
        print("Enter 5 to check complains of students")
        print("Enter 6 to view history")
        print("Enter 7 view the dictionary of the books")
        print("Enter 8 to exit")
        print('\n----------------------------------------------')
        choice = int(input("-What would you like to do : "))
        print('----------------------------------------------')
                                
        if choice == 1:
            function="Add Books"
            n=int(input("How many books you want to add : "))
            for i in range(n):
              book = input('Enter a name of a book you want to add : ')
              print('----------------------------------------------')
              if book in library_books:
                print("We already have this book")
                print('----------------------------------------------')
                print(library_books)
                data=[status,function,n,book]
                activities(data)
              else:
                library_books.append(book)
                print('----------------------------------------------')
                print("Your book Name is",book,"and your book index is",len(library_books)-1)
                print('----------------------------------------------')
                data=[status,function,n,book] 
                activities(data)
                print(library_books)
        elif choice == 2:
            function="Issue a book"
            print('----------------------------------------------')
            print("Available books are:")
            book_names()
            print('----------------------------------------------')
            print("If you want to issued book by index Enter 1\nIf you want to issued book by it Name Enter 2")
            while True:
              n=int(input(">"))
              if n==2:
                book=input("The book issued name is : ")
                if book in library_books:
                  name=str(input("Enter name of a student to which book is issued : "))
                  reg_no=input("Enter regestration number of student : ")
                  batch=input("Enter batch with department : ")
                  print('----------------------------------------------')
                  print("Student name is",name)
                  print('----------------------------------------------')
                  print("Student regestration ID is",reg_no)
                  print('----------------------------------------------')
                  print("Student department is",batch)
                  print('----------------------------------------------')
                  print(name,"must return the book on",lastdate)
                  print('----------------------------------------------')
                  print("The Book name is",book)
                  library_books.remove(book)
                  print(library_books)
                  print('----------------------------------------------')
                  data=[status,function,book,name,reg_no,batch]
                  activities(data)
                  break
                else:
                  print("Book is not Available")
                  print('----------------------------------------------')
                  break
              elif n==1:
                for i in range(len(library_books)):
                  while True:
                    index=int(input("The book issued index is : "))
                    length=len(library_books)-1
                    if index <= length:
                      book=library_books[index]
                      if book in library_books:
                        name=str(input("Enter name of a student to which book is issued : "))
                        reg_no=input("Enter regestration number of student : ")
                        batch=input("Enter batch with department : ")
                        library_books.remove(book)
                        print('----------------------------------------------')
                        print("Student name is",name)
                        print('----------------------------------------------')
                        print("Regestration ID is",reg_no)
                        print('----------------------------------------------')
                        print("Department is",batch)
                        print('----------------------------------------------')
                        print(name,"should return book on",lastdate)
                        print('----------------------------------------------')
                        print("Book name is",book)
                        print('----------------------------------------------')
                        data=[status,function,index,name,reg_no,batch]
                        activities(data)
                        admin()
                    else:
                      print("This Book is not currently present in our library")
                      print('----------------------------------------------')
                      break      
              else:
                print("You Enter Wrong Information!\nEnter again")
                print('----------------------------------------------')
                break
                                              
        elif choice == 3:
            function="Check books"
            print("Available books are:")
            book_names()
            print('----------------------------------------------') 
            data=[status,function]
            activities(data)
        elif choice == 4:
            function="Delete a book"
            print("Available books are :")
            book_names()
            print("If you want to delete book by index Enter 1\nIf you want to delete book by it's Name Enter 2")
            while True:
              n=int(input())
              if n==2:
                print('----------------------------------------------') 
                book=input("Enter a name of a book you want to delete : ")
                print('----------------------------------------------') 
                if book in library_books:
                  library_books.remove(book)
                  print(library_books)
                  data=[status,function,book]
                  activities(data)
                  print('----------------------------------------------')
                  break
                else:
                  print("Book is not Found.")
                  print('----------------------------------------------') 
                  break
              elif n==1:
                index=int(input("Enter an index of a book you want to delete :"))
                length = len(library_books)-1
                if index <= length:
                  book=library_books[index]
                  if book in library_books:
                    dele=library_books.remove(library_books[index])
                    print(library_books)
                    data=[status,function,book]
                    activities(data)
                    print('----------------------------------------------')
                    break
                else:
                  print("Book is not currently present in our library")
                  print('----------------------------------------------')
                  break
              else:
                print("You have entered a Wrong Information!\nEnter again")
                print('----------------------------------------------') 
                break
        elif choice == 5:
            with open("complains.csv","r") as file:
              readi=csv.reader(file)
              for rows in readi:
                print(rows)
            print('----------------------------------------------')
        elif choice == 6:
          function="View history"
          record()
          data=[status,function]
          activities(data)
          print('----------------------------------------------')
        
        elif choice==7:
          exit()
          break
        else:
            print("Invalid")
            print('----------------------------------------------')
            print("\n----------------------------------------------")
            print('-                                            -')
            print('-         Programme has ended                -')
            print('-                                            -')
            print('----------------------------------------------')
            
def student():
    print('----------------------------------------------')
    print('-                                            -')
    print('-          Welcome to our Library            -')
    print('-                                            -')
    print('----------------------------------------------')
    print()
    status="Student"
    while True:
        print("Enter 1 to return a book")
        print("Enter 2 for issuing a book") 
        print("Enter 3 to view available books")
        print("Enter 4 for complains")
        print("Enter 5 to exit")
        print('\n----------------------------------------------')
        choice = int(input("-What would you like to do : "))
        print('----------------------------------------------')
                            
        if choice == 1:
            function="Return a book"
            book=input("Enter name of a book you want to return :")
            if book not in library_books:
                library_books.append(book) 
                print('----------------------------------------------')
                name = str(input("What is Your Name : ")) 
                reg_no=input("Enter regestration number of student : ")
                batch=input("Enter batch with department : ")
                print('----------------------------------------------')
                print(name,"return book on",datenow)
                print('----------------------------------------------')
                print("The Book name",book)
                print('----------------------------------------------')
                data=[book,name,reg_no,batch,book]
                activities(data)
                  
            else:
              print('----------------------------------------------')
              print("This book is already present!")
              print('----------------------------------------------')
        elif choice == 2:
          function="Issue a book"
          print('----------------------------------------------')
          print("Available books are:")
          book_names()
          print('----------------------------------------------')
          print("If you want to issued book by index Enter 1\nIf you want to issued book by it Name Enter 2")
          while True:
            n=int(input(">"))
            if n==2:
              book=input("The book issued name is : ")
              if book in library_books:
                name=str(input("Enter name of a student to which book is issued : "))
                reg_no=input("Enter regestration number of student : ")
                batch=input("Enter batch with department : ")
                print('----------------------------------------------')
                print("Student name is",name)
                print('----------------------------------------------')
                print("Student regestration ID is",reg_no)
                print('----------------------------------------------')
                print("Student department is",batch)
                print('----------------------------------------------')
                print(name,"must return the book on",lastdate)
                print('----------------------------------------------')
                print("The Book name",book)
                library_books.remove(book)
                print('----------------------------------------------')
                data=[status,function,book,name,reg_no,batch]
                activities(data)
                print("If you want to exit Enter 1\nIf you want to continue Enter 2")
              else:
                print("Book is not Available")
                print('----------------------------------------------')
                break
            elif n==1:
              for i in range(len(library_books)):
                while True:
                  index=int(input("The book issued index is : "))
                  if index <= len(library_books)-1:
                    book=library_books[index]
                    if book in library_books:
                      name=str(input("Enter name of a student to which book is issued : "))
                      reg_no=input("Enter regestration number of student : ")
                      batch=input("Enter batch with department : ")
                      library_books.remove(book)
                      print('----------------------------------------------')
                      print("Student name is",name)
                      print('----------------------------------------------')
                      print("Regestration ID is",reg_no)
                      print('----------------------------------------------')
                      print("Department is",batch)
                      print('----------------------------------------------')
                      print(name,"should return book on",lastdate)
                      print('----------------------------------------------')
                      print("Book name is",book)
                      print('----------------------------------------------')
                      data=[status,function,index,name,reg_no,batch]
                      activities(data)
                      student()
                      break
                  else:
                    print('----------------------------------------------')
                    print("This Book is not currently present in our library")
                    print('----------------------------------------------')
                    break      
            else:
              print("You Enter Wrong Information!\nEnter again")
              print('----------------------------------------------')
              break

        elif choice == 3:
            function="Check books"
            print("Available books are ")
            book_names()
            data=[status,function]
            activities(data)
            print('----------------------------------------------') 
        elif choice == 4:
             function="Complains Box"
             name = input("Enter your name : ")
             reg_num = input("Enter your registration number :")
             department = input("Enter your department : ")
             complain = input("Enter your complain : ")
             data = [name, reg_num, department, complain]
             with open('complains.csv', 'w', newline='') as file:
               writer = csv.writer(file)
               writer.writerow(data)
               print("Complain successfully Recieved in Admin Portal") 
               data=[status,function,complain]
               activities(data)
        elif choice == 5:
             exit()
             print('----------------------------------------------')
             break   
        else:
            print("Invalid")
            print('----------------------------------------------')
            print('\n----------------------------------------------')
            print('-                                            -')
            print('-         Programme has ended                -')
            print('-                                            -')
            print('----------------------------------------------')      
        
print('----------------------------------------------')
print('-                                            -')
print('-  Welcome to our Library  Management System -')
print('-                                            -')
print('----------------------------------------------')
print()
while True:
    print("Enter 1 for Student portal \nEnter 2 for Admin portal ")
    user = int(input("> "))
    if user==2:
        for i in range(3): #If you enter incorrect password more then 3 times programme will go to main page.
          while True:
            print('----------------------------------------------')
            print('-                                            -')
            print('-    Welcome to Admin Portal of Library      -')
            print('-                                            -')
            print('----------------------------------------------')
            print()  
            id = input("Enter your Library ID or Name : ")     #id is Admin or 220201000
            if id=="220201000" or id=="Admin":                
              password = input("Enter Your Password : ")       #password is Sir Nadeem 
              if password=="Sir Nadeem":
                print(admin())
              else:
                print("Incorrect Password!")
                break
            else:
              print("Incorrect ID!")
              break
    elif user==1:
        for i in range(3): #If you enter incorrect password more then 3 times programme will go to main page.
          while True:
            print('----------------------------------------------')
            print('-                                            -')
            print('-    Welcome to Student Portal of Library    -')
            print('-                                            -')
            print('----------------------------------------------')
            print()    
            id = input("Enter your Library ID or Name : ")       #id is Student or 220201000
            if id=="220201000" or id=="Student":
              password = input("Enter Your Password : ")         #Password is CS-03A
              if password=="CS-03A":
                print(student())
                break
              else:
                print("Incorrect Password!")
                break
            else:
              print("Incorrect ID!")
              break
    else:
        print('\n--------------------------------')
        print('Invalid choice, Choose again')
        print('--------------------------------\n')
