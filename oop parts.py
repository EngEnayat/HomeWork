# create a class called Person with attributes name and age. Create an object of the 
# class and print 
#  its attributes.

# class Person():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# Ahmad = Person("Ahmad", 30)
# print(Ahmad.name, Ahmad.age)

#  2 . Add a method called greet to the Person class that prints a greeting message 
#  including the person's name.

# class Person():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
#     def greet(self, greet):
#         return f"{greet} {self.name}"
    
# Ahmad = Person("Ahmad", 30)
# print(Ahmad.greet("Hello"))

#  3. Create a class called Car with attributes make, model, and year. Include a 
#  method to print out the car's details.

# class Car():
#     def __init__(self, make,model, year):
#         self.make = make
#         self.model = model
#         self.year = year

#     def detail(self):
#         print(f"{self.make} {self.model} {self.year}")

# Pride = Car("Iranian", "new", 2020)
# Pride.detail()

# 4 Create a class Circle with a method to compute the area. Initialize the class with the radius.
# class Circle():
#     radius = 16
#     def compute(self):
#         print("the area is; ", Circle.radius * 0.5)
# circle_area = Circle()
# circle_area.compute()


# 5. Create a class Rectangle with methods to compute the area and perimeter. Initialize the class 
# with the length and width.

# 6  Create a base class Animal with a method speak. Create two derived classes Dog and Cat that 
# override the speak method.

# class Animal():
#     def __init__(self, an_type):
#         self.an_type = an_type
        
#     def speak(self):
#         print(f'the {self.an_type} is speaking')

# class Dog(Animal):
#     pass
# class Cat(Animal):
#     pass
# dog = Dog("dog")
# dog.speak()
# cat = Cat("cat")
# cat.speak()

#  7. Create a base class Shape with a method area. Create derived classes Square 
# #  and Triangle that implement the area method.

# class Shape():
#     def area():
#         print("calculating the area of the shape")
        
# class Square():
#     pass
# class Triangle():
#     pass
# square = Square()
# triangle = Triangle()



#  8. Create a class Employee with attributes name and salary. Create a derived 
#  class Manager with an additional attribute department.

# class Employee():
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
    
# class Manager(Employee):
#     def __init__(self, name, salary, department):
#         super().__init__(name, salary)
#         self.department = department

# manager = Manager("Ali", 8000, "computer")




# 9. Create a base class Vehicle with a method drive. Create derived classes 
# Bike and Truck that override the drive method.

# class Vehicle():
#     def drive(self):
#         print("the vehicle is driving")
# class Bike(Vehicle):
#     pass
# class Truck(Vehicle):
#     pass   

# bike = Bike()
# bike.drive()
# truck = Truck()
# truck.drive()




# 10. Create a base class Bird with a method fly. Create derived classes Eagle 
# and Penguin. Override the fly method in Penguin to indicate that penguins cannot fly.

# class Bird():
#     def fly(self):
#         print("the bird is flying")

# class Eagle(Bird):
#     def fly(self):
#         print("the Eagle is flying")
# class Penguin(Bird):
#     def fly(self):
#         print("the Penguin cannot flying")
# penguin = Penguin()
# penguin.fly()

        
        
#  11. Create a class Account with private attributes balance. Provide public methods to 
# deposit  and withdraw money 
        
# class Account():
#     def __init__(self, balance):
#         self.__balance = balance
#     def deposit(self, amount):
#         return self.__balance+amount
#     def withdraw(self, amount):
#         return self.__balance - amount

# z= Account(80)
# print(z.deposit(9))
# print(z.withdraw(8))



# 12. Create a class Book with private attributes title, author, and pages. Provide public
# methods to get  and set these attributes.

# class Book():
#     def __init__(self, title, author, pages):
#         self.__title = title
#         self.__author = author
#         self.__pages = pages
        
#     def set_book(self, title , author, pages):
#         self.__title = title
#         self.__author = author
#         self.__pages = pages
    
#     def get_book(self):
#         return f"{self.__title} {self.__author} {self.__pages}"
    
# book = Book("novel", "habib", 809)
# book.set_book("life", "ali", 30)
# print(book.get_book())



# 13. Create a class Laptop with private attributes brand, model, and price. Provide a 
# method to apply a discount and a method to display laptop details.

# class Laptop():
#     def __init__(self, brand, model, price):
#         self.__brand = brand
#         self.__model = model
#         self.__price = price
    
#     def discount(self, discount):
#         if (discount == 399):
#             v = self.__price * 0.95
#             return f"{v} this is the amount agter discounting done"

#     def detail(self):
#         return f"{self.__brand} {self.__model} {self.__price}"

# dell = Laptop("Dell", 6490 , 8999)
# print(dell.discount(399))
# print(dell.detail())




#  14. Create a class BankAccount with private attributes account_number and balance.
#  Provide methods to deposit, withdraw, and check the balance.

# class BankAccount():
#     def __init__(self, account_number, balance):
#         self.__account_number = account_number
#         self.__balance = balance
        
#     def deposit(self, number_of_deposite):
#         v = self.__balance + number_of_deposite
#         return f"{v} amount has successfully done"
    
#     def withdraw(self, number_of_deposite):
#         v = self.__balance - number_of_deposite
#         return f"{v} amount has successfully withdrawed"


#     def checkBalance(self):
#         return f"this is your AccountNumber: {self.__account_number}, and this is amount of your balance: {self.__balance}"

# person1 = BankAccount(200, 9000)
# print(person1.deposit(100))
# print(person1.withdraw(100))
# print(person1.checkBalance())


#  15. Create a class Student with private attributes name, grade, and age. Provide 
# methods to get and set these attributes and a method to display the student's details.

# class Student():
#     def __init__(self, name, grade, age):
#         self.__name = name
#         self.__grade = grade
#         self.__age = age
#     def setter(self, name, grade, age):
#         self.__name = name
#         self.__grade = grade
#         self.__age = age
#     def getter(self):
#         return f"name: {self.__name}, grade: {self.__grade}, age: {self.__age}"
    
#     def display(self):
#         return f"name: {self.__name}, grade: {self.__grade}, age: {self.__age}"
    
# Ali = Student("Ali", "Ten", 20)
# Ali.setter("Ali", "Ten", 20)
# print(Ali.getter())
# print(Ali.display())

# 16. Create a class Library with attributes name and books (a list of Book objects). 
#Provide methods to add and remove books.
    
# class Library():
#     def __init__(self, name):
#         self.name = name
#         self.books = []
        
#     def adder(self, book):
#         v = self.books.append(book)
#         return f"{book} has added"
#     def remover(self, book):
#         if book in self.books:
#             self.books.remove(book)
#             print("successfully removed!")
            
# eqra = Library("math")
# print(eqra.adder("math"))
# print(eqra.remover("math"))


# 7. Create a class School with attributes name and students (a list of Student objects). 
# Provide methods to add and remove students.

# class School():
#     def __init__(self, name):
#         self.name = name
#         self.students = []
#     def add_st(self, name):
#         self.students.append(name)
#         return f"{name} has successfully added!"
#     def rem_st(self, name):
#         if name in self.students:
#             self.students.remove(name)
#             return f"{name} has successfully removed!"
        
# Homayon = School("Homayon")
# Homayon.add_st("Ali")
# print(Homayon.add_st("abbas"))
# print(Homayon.rem_st("Ali"))
    
    
#  18. Create a class Team with attributes name and members (a list of Person objects). 
# Provide methods to add and remove members.
    
# class Team():
#     def __init__(self, name):
#         self.name = name
#         self.members = []
#     def add_st(self, member):
#         self.members.append(member)
#         return f"{member} has successfully added!"
#     def rem_st(self, member):
#         if member in self.members:
#             self.members.remove(member)
#             return f"{member} has successfully removed!"
# Asia = Team("Asia")
# print(Asia.add_st("Afghanistan"))
# print(Asia.rem_st("Afghanistan"))



#  19. Create a class Company with attributes name and employees (a list of Employee objects). 
# Provide methods to add and remove employees.

# class Company():
#     def __init__(self, name):
#         self.name = name
#         self.employee = []
#     def add_st(self, name):
#         self.employee.append(name)
#         return f"{name} has successfully added!"
#     def rem_st(self, name):
#         if name in self.employee:
#             self.employee.remove(name)
#             return f"{name} has successfully removed!"
        
# emp1 = Company("Jamal")
# print(emp1.add_st("Jamal"))
# print(emp1.rem_st("Jamal"))


# 20. Create a class Zoo with attributes name and animals (a list of Animal objects). Provide 
# methods to add and remove animals.

# class Zoo():
#     def __init__(self, name):
#         self.name = name
#         self.animals = []
#     def add_st(self, name):
#         self.animals.append(name)
#         return f"{name} has successfully added!"
#     def rem_st(self, name):
#         if name in self.animals:
#             self.animals.remove(name)
#             return f"{name} has successfully removed!"

# zebra = Zoo("zebra")
# print(zebra.add_st("zebra"))
# print(zebra.rem_st("zebra"))



#  21. Create a class FileManager with methods to read from and write to a file.

# class FileManager():
#     def reading(self, FileName):
#         with open(f"{FileName}", "r") as f:
#             print(f.read())
#     def writing(self,FileName):
#         with open(f"{FileName}", "w") as f:
#             v = str(input("enter something: "))
#             print(f.write(v))
#             print("the text wrote succedd")
# doc = FileManager()
# doc.reading("a.txt")
# doc.writing("a.txt")
            


# #  22. Create a class Log with methods to write error messages to a log file

# class Log():
#     def __init__(self, name):
#         self.name = name
#         self.members = []
#     def adder(self, name):
#         if name not in self.members:
#             self.members.append(name)
#     def error(self, yourName):
#         if yourName in self.members:
#                 print("you are a member here!")
#         else:    
#                 print("you are not a member!")  
    
# person1 = Log("ali")
# person1.adder("ali")
# person1.error("ali")
# person1.error("abbas")


# 23. Create a class Config that reads configuration settings from a file and provides 
# methods to access these settings.

# class config():
#     # def __init__(self, con_set):
#     #     self.con_set = con_set
#     def access(self, FileName):
#         with open(f"{FileName}", "r") as fr:
#             with open("line", "w")as fw:              
#                 for line in fr:
#                     line = fw.write(f"{fr.read()}")
#         print(line)
# first = config()
# first.access("a.txt")

# 24. Create a class Database that connects to a database and provides methods to execute queries. 
# Handle exceptions if the connection fails

# import sqlite3
# class database():
#     def connection(self):
#         try:
#             conn = sqlite3.connect("my_db.db")
#             c = conn.cursor()
#             c.execute('''CREATE TABLE students(
#                 name text,
#                 last text,
#                 age integer)''')
#             c.execute("INSERT INTO students VALUES('ali', 'abbasi', 20)")
#             c.execute("SELECT * FROM students")
#             print(c.fetchone())
#             conn.commit()
#             conn.close()
#         except:
#             print("The connection failed")
            
# mango = database()
# mango.connection()
    

# 25. Create a class Report that generates a report from data in a file. Provide methods 
# to handle exceptions if the file does not exist or cannot be read.



# 26. Create a class Ticket for a movie theater with attributes movie_name, seat_number,
# and price. Provide methods to display ticket details and apply discounts.

# class Ticket():
#     def __init__(self, movie_name, seat_number, price):
#         self.movie_name = movie_name
#         self.seat_number = seat_number
#         self.price = price
#     def discount(self, discount):
#         if discount == "ir90":
#             disc = self.price * 0.94
#             print("the new price after discount done", disc)
#         else:
#             print("you are not eligible for getting discount!")
#     def detail(self):
#         print(f"Name: {self.movie_name}, Seat_number: {self.seat_number}, price: {self.price}")
        
# titanic = Ticket("Titanic",25, 900)
# titanic.discount("ir90")
# titanic.detail()        
        
        
#  27. Create a class ShoppingCart with methods to add, remove, and display items. Each item
#  should be an object of a class Item with attributes name and price.       
# class ShopingCard():
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#         self.items = []
#     def adder(self, item):
#         if item not in self.items:
#             self.items.append(item)
#             print("item has successfully added!")
#     def remove(self, item):
#         if item in self.items:
#             self.items.remove(item)
#             print("the item has successfully removed!")
#     def display(self):
#         print(f"Name: {self.name}, Price: {self.price}")
# green = ShopingCard("green", 900)
# green.adder("green")
# green.remove("green")
# green.display()
        

# 28. Create a class Restaurant with attributes name and menu (a list of Item objects). 
# Provide methods to add and remove items from the menu.   
        
# class Restaurant():
#     def __init__(self, name):
#         self.name = name
#         self.menu = []
#     def adder(self, item):
#         if item not in self.menu:
#             self.menu.append(item)
#             print("adding successfully done!")
#     def remover(self, item):
#         try:
#             if item in self.menu:
#                 self.menu.remove(item)
#                 print("done removing")
#         except:
#             print("the item is not exist")
# steak = Restaurant("steak")
# steak.adder("steak")
# steak.remover("steak")      



# 29. Create a class Flight with attributes flight_number, destination, and passengers
# (a list of Person objects). Provide methods to add and remove passengers.

# class Flight():
#     def __init__(self, flight_number, destination):
#         self.flight_number = flight_number
#         self.destination = destination
#         self.passengers = []
#     def adder(self, passenger):
#         if passenger not in self.passengers:
#             self.passengers.append(passenger)
#             print("done adding!")
#         else:
#             print("this person is already exist!")
#     def remove(self, passenger):
#         if passenger in self.passengers:
#             self.passengers.remove(passenger)
#             print("removing done!")
# Jamal = Flight(38, "USA")
# Jamal.adder("Jamal")
# Jamal.remove("Jamal")


# 30. Create a class Hotel with attributes name and rooms (a list of Room objects). Each Room
# should have attributes room_number and is_occupied. Provide methods to book and checkout rooms

# class Room:
#     def __init__(self, room_number: int, is_occupied: bool):
#         self.room_no = room_number
#         self.is_occupied = is_occupied
            
# room1 = Room(1, True)
# room2 = Room(2, False)
# room3 = Room(3, False)
# room4 = Room(4, False)
# room5 = Room(5, True)
# room6 = Room(6, False)
# room7 = Room(7, True)
# room8 = Room(8, True)
# room9 = Room(9, False)
# room10 = Room(10, False)


# class Hotel:
#     def __init__(self, name):
#         self.name = name
#         self.room = [room1, room2, room3, room4, room5, room6, room7, room8, room9, room10]
        
#     def check(self):
#         for i in self.room:
#             if self.room[i].is_occupied == True:
#                 print('Room is occupied..')
#             else:
#                 print('Room is Free..')
                
#     def book(self):
#         for i in self.room:
#             if self.room[i].is_occupied == True:
#                 print('It is already booked')
#             else:
#                 self.room[i].is_occupied = True
#                 print('You are Welcome, My Lord!')
                

# h1 = Hotel('Abas&Mahgol Ltd')
# h1.check()


# 36
# import tkinter as tk

# class CounterApp:
#     def __init__(self, root):
#         self.counter_value = 0
        
#         # Create and pack the counter label
#         self.label = tk.Label(root, text=f"Counter: {self.counter_value}", font=("Helvetica", 18))
#         self.label.pack(pady=20)
        
#         # Create and pack the increment button
#         self.increment_button = tk.Button(root, text="Increment", command=self.increment_counter)
#         self.increment_button.pack()

#         # Create and pack the decrement button
#         self.decrement_button = tk.Button(root, text="Decrement", command=self.decrement_counter)
#         self.decrement_button.pack()

#     def increment_counter(self):
#         self.counter_value += 1
#         self.label.config(text=f"Counter: {self.counter_value}")

#     def decrement_counter(self):
#         self.counter_value -= 1
#         self.label.config(text=f"Counter: {self.counter_value}")

# # Create the main tkinter window
# root = tk.Tk()
# root.title("Counter App")
# root.geometry('600x400')

# # Create an instance of CounterApp
# app = CounterApp(root)

# # Run the tkinter main loop
# root.mainloop()


# 37

# import tkinter as tk
# from tkinter import messagebox

# class ToDoApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("To-Do App")

#         # List to store tasks
#         self.tasks = []

#         # Entry for task input
#         self.task_entry = tk.Entry(root, width=40)
#         self.task_entry.pack(pady=10)

#         # Button to add task
#         add_button = tk.Button(root, text="Add Task", command=self.add_task)
#         add_button.pack()

#         # Listbox to display tasks
#         self.task_listbox = tk.Listbox(root, height=15, width=50)
#         self.task_listbox.pack(pady=10)

#         # Button to remove task
#         remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)
#         remove_button.pack()

#     def add_task(self):
#         task = self.task_entry.get().strip()
#         if task:
#             self.tasks.append(task)
#             self.task_listbox.insert(tk.END, task)
#             self.task_entry.delete(0, tk.END)
#         else:
#             messagebox.showwarning("Warning", "Please enter a task.")

#     def remove_task(self):
#         try:
#             index = self.task_listbox.curselection()[0]
#             self.task_listbox.delete(index)
#             del self.tasks[index]
#         except IndexError:
#             messagebox.showwarning("Warning", "Please select a task to remove.")

# # Create the main tkinter window
# root = tk.Tk()

# # Create an instance of ToDoApp
# app = ToDoApp(root)

# # Run the tkinter main loop
# root.mainloop()


# 38

# import tkinter as tk

# class CalculatorApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Calculator")

#         # Entry for displaying calculations
#         self.entry = tk.Entry(root, width=20, borderwidth=5, font=("Arial", 18))
#         self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

#         # Calculator buttons
#         buttons = [
#             ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
#             ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
#             ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
#             ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
#         ]

#         # Create and place buttons
#         for (text, row, col) in buttons:
#             button = tk.Button(root, text=text, padx=20, pady=10, font=("Arial", 18),
#                                command=lambda t=text: self.handle_click(t))
#             button.grid(row=row, column=col, padx=5, pady=5)

#     def handle_click(self, text):
#         current = self.entry.get()
#         if text == '=':
#             try:
#                 result = eval(current)
#                 self.entry.delete(0, tk.END)
#                 self.entry.insert(tk.END, str(result))
#             except Exception as e:
#                 self.entry.delete(0, tk.END)
#                 self.entry.insert(tk.END, "Error")
#         else:
#             self.entry.insert(tk.END, text)

# # Create the main tkinter window
# root = tk.Tk()

# # Create an instance of CalculatorApp
# app = CalculatorApp(root)

# # Run the tkinter main loop
# root.mainloop()

# 39

# import tkinter as tk
# from tkinter import messagebox

# class LoginApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Login")

#         # Username entry
#         self.username_label = tk.Label(root, text="Username:")
#         self.username_label.grid(row=0, column=0, padx=10, pady=10)
#         self.username_entry = tk.Entry(root)
#         self.username_entry.grid(row=0, column=1, padx=10, pady=10)

#         # Password entry
#         self.password_label = tk.Label(root, text="Password:")
#         self.password_label.grid(row=1, column=0, padx=10, pady=10)
#         self.password_entry = tk.Entry(root, show='*')
#         self.password_entry.grid(row=1, column=1, padx=10, pady=10)

#         # Login button
#         self.login_button = tk.Button(root, text="Login", command=self.check_credentials)
#         self.login_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

#     def check_credentials(self):
#         username = self.username_entry.get()
#         password = self.password_entry.get()

#         # Replace with actual credentials validation logic
#         if username == "admin" and password == "password":
#             messagebox.showinfo("Login Successful", "Welcome, Admin!")
#         else:
#             messagebox.showerror("Login Failed", "Invalid username or password.")

# # Create the main tkinter window
# root = tk.Tk()

# # Create an instance of LoginApp
# app = LoginApp(root)

# # Run the tkinter main loop
# root.mainloop()


# 40

# import tkinter as tk
# from tkinter import messagebox
# import requests

# class WeatherApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Weather App")

#         # Entry for city input
#         self.city_entry = tk.Entry(root, width=30)
#         self.city_entry.pack(pady=10)

#         # Button to fetch weather
#         self.get_weather_button = tk.Button(root, text="Get Weather", command=self.get_weather)
#         self.get_weather_button.pack()

#         # Label to display weather information
#         self.weather_label = tk.Label(root, text="", font=("Helvetica", 18))
#         self.weather_label.pack(pady=20)

#     def get_weather(self):
#         city = self.city_entry.get()
#         if not city:
#             messagebox.showwarning("Warning", "Please enter a city.")
#             return
        
#         api_key = 'YOUR_API_KEY'  # Replace with your API key
#         url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        
#         try:
#             response = requests.get(url)
#             data = response.json()
#             if data['cod'] == 200:
#                 weather_description = data['weather'][0]['description']
#                 temperature = data['main']['temp']
#                 self.weather_label.config(text=f"Weather: {weather_description}\nTemperature: {temperature} °C")
#             else:
#                 messagebox.showerror("Error", f"Error: {data['message']}")
#         except Exception as e:
#             messagebox.showerror("Error", f"Error fetching weather data: {e}")

# # Create the main tkinter window
# root = tk.Tk()

# # Create an instance of WeatherApp
# app = WeatherApp(root)

# # Run the tkinter main loop
# root.mainloop()
