from tkinter import *
from PIL import ImageTk,Image
import numpy as np
import time

root = Tk()
root.geometry("530x600")
root.resizable(width=0, height=0) #making the size of the window fixed
root.title("Sudoku Solver")

background = ImageTk.PhotoImage(Image.open("C:/Users/Mohamed/PycharmProjects/SudokuSolver/Background.jpg"))
background_label = Label(image=background)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

l = [["20" for i in range(9)] for j in range(9)]
l_integer = [[0 for i in range(9)] for j in range(9)]

e = [[0 for i in range(9)] for j in range(9)]
for i in range(9):
    for j in range(9):
        e[i][j] = Entry(root, width='2', borderwidth='2', font=('Helvetica', 24))
        e[i][j].grid(row=i, column=j, padx=2, pady=2)

########################################################################

def solve():
    global l
    global l_integer

    for i in range(9):
        for j in range(9):
            l[i][j] = e[i][j].get()

    for i in range(0,len(l_integer)):
        for j in range(0, len(l_integer[0])):
            if len(l[i][j]) > 0:
                l_integer[i][j] = int(l[i][j])
    actual_solver()

def possible(row,column,number):
    global l_integer
    print(np.matrix(l_integer))
    for i in range(0,9):
        if l_integer[row][i] == number:
            return False
    for i in range(0, 9):
        if l_integer[i][column] == number:
            return False
    x0 = (row // 3) * 3      # to check the 3*3 grid starting from the row that the number in
    y0 = (column // 3) * 3   # to check the 3*3 grid starting from the column that the number in
    for i in range(0, 3):
        for j in range(0, 3):
            if l_integer[x0+i][y0+j] == number:
                return False
    return True

def actual_solver():
    global l_integer
    for row in range(0, 9):
        for column in range(0, 9):
            if l_integer[row][column] == 0:
                for number in range(1, 10):
                    if possible(row, column, number):
                        l_integer[row][column] = number
                        actual_solver()
                        l_integer[row][column] = 0
                return
    print(np.matrix(l_integer))
    print()

    for i in range(9):
        for j in range(9):
            e[i][j].delete(0, END)
            e[i][j].insert(END, l_integer[i][j])
            if j == 8:
                root.update()

    for j in range(9):
        e[0][j].delete(0, END)
        e[0][j].insert(END, l_integer[0][j])

    root.update()
    time.sleep(60)  # after 60 seconds of showing the solution the program exits by itself
    exit(0)

SolveButton = Button(root, padx=30, bg="yellow", font=50 , text="Solve", command=solve)
SolveButton.grid(row=10, column=9)
root.mainloop()
