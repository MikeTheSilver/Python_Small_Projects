from tkinter import *
import subprocess, sys, os

# powershell functions / powershell part
file_path = os.path.dirname(sys.argv[0])
def Create_VM():
    p = subprocess.Popen(["powershell.exe", file_path+"\Scripts\Create_VM.ps1"],stdout=sys.stdout)
    p.communicate()
def Check_PC():
    p = subprocess.Popen(["powershell.exe", file_path+"\Scripts\Check_PC.ps1"],stdout=sys.stdout)
    p.communicate()
def Add_Printer():
    p = subprocess.Popen(["powershell.exe", file_path+"\Scripts\Add_Printer.ps1"],stdout=sys.stdout)
    p.communicate()

print(file_path)
# Object
Manager = Tk()
Manager.title('Script Manager')
Manager.geometry('800x400')
Manager.maxsize(800,400)
Manager.config(bg="white")

# Example how to add text
# Script1 = Label(Manager, text='Create VM')
# Script1.grid(column=1,row=0)

#Buttons

Button1 = Button(Manager,text='Create VM',bg='aqua',fg='black',command=Create_VM,activebackground="Blue")
#Button1.grid(column=1,row=1)
Button1.place(relx=0.2,rely=0.2,anchor=CENTER)

Button2 = Button(Manager,text='Check PC',bg='aqua',fg='black',command=Check_PC,activebackground="Blue")
#Button2.grid(column=2,row=1)
Button2.place(relx=0.5,rely=0.2,anchor=CENTER)

Button3 = Button(Manager,text='Add Printer',bg='aqua',fg='black',command=Add_Printer,activebackground="Blue")
#Button3.grid(column=3,row=1)
Button3.place(relx=0.8,rely=0.2,anchor=CENTER)



# Line below starts program
Manager.mainloop()


