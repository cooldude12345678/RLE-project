import tkinter as tk
from tkinter import ttk



master = tk.Tk()
master.geometry("450x350")

     

def RLE():
  print("you selected option 1")
  master1 =tk.Tk()
  master1.geometry("450x350")
  master1.configure(bg="blue")
  print("how many lines of compressed data would you like to enter")
  klks = int(input(""))
  while klks < 3:
    print("please renter")
    klks = int(input(""))
    
  
  theinput=[]
  for x in range(klks):
    ljk = input("please enter line {0}:".format(x+1)).rstrip()
    theinput.append(ljk)
  
  
  
  
  outp = ""
  for x in theinput:
    for i in range(0, len(x ), 3):
      group = x [i:i+3]
      outp += f"{int(group[:2]) * group[2]}"
    outp += "\n"
  print(outp)
  returnmenu =input("would you like to return to the menu: ")
  if returnmenu == "yes":
    master1.destroy()
  else:
    exit("\n\n goodbye")
  
  







def showascii():
  print("you selected option 2")
  master1 =tk.Tk()
  master1.geometry("450x350")
  master1.configure(bg="blue")
  showtheascii = input("what file would you like to display: ")
  with open (showtheascii)as f1:
    hia = f1.read()
    print(hia)

  
  button5 = ttk.Button(master1, text="this is option 2")
  button5.place(x = 175, y = 150)
  returnmenu =input("would you like to return to the menu: ")
  if returnmenu == "yes":
    master1.destroy()
  else:
    exit("\n\n goodbye")
  
def convertascii():
  print("you selected option 3")
  master1 =tk.Tk()
  master1.geometry("450x350")
  master1.configure(bg="blue")

  
  button4 = ttk.Button(master1, text="this is option 3")
  button4.place(x = 175, y = 150)
  asciinput = input("enter the name of the file you would like to convert to ascii: ")
  with open (asciinput, "r")as f3:
    j = f3.read()

  convertlist = j.strip().split("\n")

  
  outp = ""
  for x in convertlist:
    for i in range(0, len(x ), 3):
      group = x [i:i+3]
      outp += f"{int(group[:2]) * group[2]}"
    outp += "\n"
  print(outp)
  returnmenu =input("would you like to return to the menu: ")
  if returnmenu == "yes":
    master1.destroy()
  else:
    exit("\n\n goodbye")






  
  
  

def Rleconverter():
  finder = input("what file would you like to convert to rle: ")
  with open(finder,"r")as f5:
    text = f5.read()

  #start count at 1 
  count = 1
  #size of string
  length = len(text)
  
  stre = ""
  for x in range(length-1):
    current = text[x]
    nextletter = text[x+1]
    if current==nextletter:
      count+= 1
    
    
    else:
        ooo = ("{:02d}".format(count))
        stre +=str(ooo)+current
        count = 1
  
  if count > 0:
    ooo = ("{:02d}".format(count))
    stre +=str(ooo)+text[-1]
    stre[:-2]
    
  
  
  stre += str(count) + current
  with open("read.txt", "w")as f8:
   comp= f8.writelines(stre)
  with open("read.txt","r")as f9:
    hi = f9.read()
  
  print(hi)
  
  
  h = len(hi)
  b = len(text)
  hell = h - b
  if hell > 0:
    print("\n\nthe origional file is ", hell ," charecters shorter")
  else:
    print("\n\nthe compressed file is ", abs(hell)," charecters shorter")
    
  
    
  

    
    
  
  
  
  
  


def quitmenu():
  exit("\nYOU QUIT GOODBYE\n")



button1=ttk.Button(master, text="Enter RLE", command=RLE)
button1.place(x=20, y=175)
button2 = ttk.Button(master, text="Display ascii Art", command=showascii)
button2.place(x= 110,y= 175 )
button3 = ttk.Button(master, text="convert to ascii", command=convertascii)
button3.place(x= 220, y= 175)
button7 = ttk.Button(master, text="please select one of these options")
button7.place(y=0, x = 120)
convertRle = ttk.Button(master, text="Convert to RLE", command= Rleconverter)
convertRle.place(x= 330,y=175)
quits = ttk.Button(master, text="Quit", command=quitmenu)
quits.place(y=30,x=190)


master.mainloop()
