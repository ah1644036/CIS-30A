# -*- coding: utf-8 -*-
"""
Write a Python program to place order and set appointment for delivery of goods 
    or services from a mobil pet spa
The program should prompt the user to select products or services and
    appointment or delivery date and time from the available options in the 
    1-year span. 
o The program should display the user selection on screen.
o The program should output the order summary and appointment in a text file.
o The program should contain the following components:
 Include comments throughout the program
 Use variables and list to store and access data. You can use tuple or 
dictionary in place of a list 
 Use string object to display and control text output. 
 Define 2 or more functions and use function calls to execute tasks in the 
program. 
 Implement loop (for or while or both) 
 Include conditional statement (if or if-else or if-elif-else) 
 Use a non-built-in module, custom module. 
 Contains at least 2 classes and 1 sub-class 
 Includes 1 or more objects and 1 or more methods in each class. 
 Implement error detection using Python built-in exceptions. 
 Implement file operations and file output. 
 Integrate UI (optional): Bonus 30 points

"""

#Greeting and check-in with pet-type
print("Welcome to Valued Pet Mobile Spa!")
print("Where we value and pamper your pet!")
print(" ")
pet_type = input("What kind of pet can we take care of: \n"
                 "Enter 1 for dog\n"
                 "Enter 2 for cat\n"
                 "Enter 3 for other")
#error catch
for i in pet_type:
    try:
        pet_type = range(1,3)
    except:
        print("Oops! That's not a valid entry. Please try again.")

#evaluate time needed
if pet_type == 1:
    import dogmod
    dogmod.weight
    dogmod.coat
    
elif pet_type == 2:
    import catmod
    catmod.weight
    catmod.coat
    
else:
    print("Unfortunately at this time we only offer online services for dogs " 
          "and cats. Please check back soon for additional offerings or " 
          "contact our office to make special arrangements")

#present service offerings for selection
if pet_type == 1:
    print("From teacup breeds to giant breeds, we offer several service tiers:\n"
          "1--Basic service: bathe, dry, brush, and style\n"
          "2--Pamper: all of Basic + nail clipping and gland expression\n"
          "3--Frou-frou: all of Pamper + teeth and ear cleaning")
    service = input(print("How can we take care of your pet?"))

#give subtotal and save to file


#set appointment time and closing
try:
    import tkinter as tk
    from tkinter import ttk
except ImportError:
    import Tkinter as tk
    import ttk

from tkcalendar import Calendar, DateEntry

def example1():
    def print_sel():
        print(cal.selection_get())

    top = tk.Toplevel(root)

    cal = Calendar(top,
                   font="Arial 14", selectmode='day',
                   cursor="hand1", year=2018, month=2, day=5)
    cal.pack(fill="both", expand=True)
    ttk.Button(top, text="ok", command=print_sel).pack()

def example2():
    top = tk.Toplevel(root)

    ttk.Label(top, text='Choose date').pack(padx=10, pady=10)

    cal = DateEntry(top, width=12, background='darkblue',
                    foreground='white', borderwidth=2)
    cal.pack(padx=10, pady=10)

root = tk.Tk()
s = ttk.Style(root)
s.theme_use('clam')

ttk.Button(root, text='Calendar', command=example1).pack(padx=10, pady=10)
ttk.Button(root, text='DateEntry', command=example2).pack(padx=10, pady=10)

root.mainloop()

print("Thank you for choosing Valued Pet Mobile Spa! We look forward to seeing "
      "you and your pet on {}", cal)
