import json
import os
import time
from tkinter import *
from tkinter import font as tkFont
from tkinter import messagebox as msgbox

FILENAME = "data.json"

def getFile():
    os.system("wget https://raw.githubusercontent.com/krispedia/PSChecker/master/"+FILENAME)

def delFile():
    os.system("rm "+FILENAME)

def getData()->dict:
    getFile()

    with open(FILENAME, "r") as file:
        s = file.read()

        data = json.loads(s.replace('\n','').replace("'",'"'))
        #print(data)
    delFile()

    return data

# === Style
COLOR_BG="#565656"
COLOR_FG="#d3d3d3"
#fontStyle = tkFont.Font(family="Courier", size=40)

# === 데이터 가져옴. 
DATA = getData()['problems']

# === 
root = Tk()

root.title("Test")
root.geometry("300x300+300+300")
root.resizable(False, False)
root.config(bg=COLOR_BG)

Label(root, text="------------------------",font=("Courier", 20, "normal"), bg=COLOR_BG, fg=COLOR_FG).place(x=150,y=20, anchor='n')
Label(root, text="PS Study", font=("Courier", 28, "normal"), bg=COLOR_BG, fg=COLOR_FG).place(x=150,y=40, anchor='n')
Label(root, text="------------------------",font=("Courier", 20, "normal"), bg=COLOR_BG, fg=COLOR_FG).place(x=150,y=70, anchor='n')
Label(root, text=" 문제 번호? ",font=("Courier", 15, "normal"), bg=COLOR_BG, fg=COLOR_FG).place(x=150, y=120, anchor='n')

e = Entry(root, width=30)
e.place(x=150, y=150, anchor='n')

lblCheck = Label(root, text="---", font=("Courier", 18, "normal"), bg=COLOR_BG, fg=COLOR_FG)

def warn_digit():
    msgbox.showwarning("Warning", "문제 번호 입력!! ex) 123")

def findE():
    found = False
    # 1. 입력 받음 
    num = e.get()
    print(e.get())
    e.delete(0, END)
    # 1.1 숫자 아니면 다시 입력
    if num.isdigit() == False: 
        warn_digit()
        return
    
    # 2. 번호 찾기
    for each in DATA:
        if each['No.'] == num:
            found = True
            lblCheck.config(text="이미 했음!")
            break
    if found == False:
        lblCheck.config(text="안했음~")

btnFind = Button(root, text="Search", command=findE,bg="black", fg="gray")
btnFind.place(x=150, y=190, anchor='n')
lblCheck.place(x=150, y=240, anchor='n')

root.mainloop()
