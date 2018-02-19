"""Random pick three number generator
   Seth Ewald
   Feb. 16 2018"""

import tkinter as tk
from tkinter import ttk
from random import randint


#Define the main program function to run
def main():
  
#Define function to change label text on button click
    def onClick():
        a = randint(0, 9)
        b = randint(0, 9)
        c = randint(0, 9)
        d=(a,b,c)
        label.config(text=d)


#Create app window
    root = tk.Tk()
    root.minsize(width=300, height=75)
    root.maxsize(width=300, height=75)
    root.title("Pick Three Generator")

#Create button to generate a random pick three
    button = tk.Button(root, text='Generate Numbers',
                       width=25, command=onClick)
    button.pack()

#Create a label to display the random pick three
    label = tk.Label(root, text='')
    label.pack()
    root.mainloop()

if __name__ =='__main__':
    main()














