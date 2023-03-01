import sqlite3
db = sqlite3.connect('bookstore')
cursor = db.cursor()  # Get a cursor object

cursor.execute('''
    CREATE TABLE IF NOT EXISTS book_database(id INTEGER, title TEXT, author TEXT,
                   	quantity INTEGER)
''')
db.commit()

print("Welcome to the book database")
#set up table
id1 = 3001
title1 = 'a tale of two cities'
author1 = 'Charles Dickens'
quantity1 = 30

id2 = 3002
title2 = 'Harry Potter and the Philosophers stone'
author2 = 'J.K.Rowling'
quantity2 = 40

id3 = 3003
title3 = 'The lion the witch and the wardrobe'
author3 = 'C.S.Lewis'
quantity3 = 25

id4 = 3004
title4 = 'The Lord of the Rings'
author4 = 'J.R.R Tolkein'
quantity4 = 37

id5 = 3005
title5 = 'Alice in Wonderland'
author5 = 'Lewis Carroll'
quantity5 = 12

book_info = [(id1,title1,author1,quantity1),(id2,title2,author2,quantity2),(id3,title3,author3,quantity3),(id4,title4,author4,quantity4),(id5,title5,author5,quantity5)]
cursor.executemany('''INSERT INTO book_database(id, title, author, quantity)
                  VALUES(?,?,?,?
                  )''', book_info)
db.commit

while True:
  menu = int(input('''Select one of the following Options below:
1. Enter book
2. Update book
3. Delete book
4. Search books
0. Exit
: '''))

#request input for new book then insert
  if menu == 1:
    pass  
    id = int(input("Please enter the book id: "))
    title = input("Please enter the book title: ")
    author = input("Please enter the book author: ")
    quantity = int(input("Please enter the quantity of the book"))
    cursor.execute('''INSERT INTO book_database(id, title, author, quantity)
                  VALUES(?,?,?,?
                  )''', (id,title,author,quantity))
    print("New book has been added")
    db.commit()

#allow user to choose book, then field to update and then execute with print feedback
  elif menu == 2:
     book = int(input("Please enter the ID of the book you would like to edit: "))
     try:
        cursor.execute('''SELECT id, title, author, quantity FROM book_database WHERE id = ?''', (book))
        selected_book = cursor.fetchone()
        print(selected_book)
        edit_choice = int(input('''Select one of the following options below:
             1. Change title
             2. Change author
             3. Change quantity
             : '''))
        if edit_choice == 1: 
           new_title = input("Please enter the new title: ")
           cursor.execute('''UPDATE book_database SET title = ? WHERE id = ?''',(new_title,book,))
           print("Title updated")
           db.commit()
        elif edit_choice == 2: 
           new_author = input("Please enter the new author: ")
           cursor.execute('''UPDATE book_database SET author = ? WHERE id = ?''',(new_author,book,))
           print("Author updated")
           db.commit()
        elif edit_choice == 3:
           new_quantity = input("Please enter the new quantity: ")
           cursor.execute('''UPDATE book_database SET quantity = ? WHERE id = ?''',(new_quantity,book,))
           print("Quantity updated")
           db.commit()
        else:
           print("Please enter one of the options provided")
     except: 
        print("This book ID does not exist")
  elif menu == 3:
      delete_id = int(input("Please enter the ID of the book to be deleted: "))
      try: 
        cursor.execute('''DELETE FROM book_database WHERE id = ?''', (delete_id))
        print("This book has been deleted")
        db.commit()
      except:
        print("This book ID is not in the database")

#allow the user to select search criteria and then search
  elif menu == 4:
        search_choice = int(input('''Search by one of the following options below:
             1. Title
             2. Author
             3. ID
             : '''))
        if search_choice == 1:
          search_title = input("Please enter the book title: ").lower() 
          try:  
            cursor.execute('''SELECT id, title, author, quantity FROM book_database WHERE lower(title) = ?''', (search_title,))
            search_results = cursor.fetchall()
            a = search_results[0]
            print("ID: "+ str(a[slice(0,1)]))
            print("Title: "+ str(a[slice(1,2)]))
            print("Author: "+ str(a[slice(2,3)]))
            print("Quantity: "+ str(a[slice(3,4)]))
          except:
            print("This book does not exist in the database")
        elif search_choice == 2:
          search_author = input("Please enter the book author: ").lower()  
          try:
            cursor.execute('''SELECT id, title, author, quantity FROM book_database WHERE lower(author) = ?''', (search_author,))
            search_results = cursor.fetchall()
            a = search_results[0]
            print("ID: "+ str(a[slice(0,1)]))
            print("Title: "+ str(a[slice(1,2)]))
            print("Author: "+ str(a[slice(2,3)]))
            print("Quantity: "+ str(a[slice(3,4)]))
          except:
            print("This book does not exist in the database")
        elif search_choice == 3:
          search_id = int(input("Please enter the book ID: ")) 
          try: 
            cursor.execute('''SELECT id, title, author, quantity FROM book_database WHERE id = ?''', (search_id,))
            search_results = cursor.fetchall()
            a = search_results[0]
            print("ID: "+ str(a[slice(0,1)]))
            print("Title: "+ str(a[slice(1,2)]))
            print("Author: "+ str(a[slice(2,3)]))
            print("Quantity: "+ str(a[slice(3,4)]))
          except:
            print("This book does not exist in the database")
        else:
            print("Please select one of the choices available next time")
  elif menu == 0:
    print("You are leaving the database")
    db.close()
    exit()
  
  else: 
    print("Please choose one of the options provided")
