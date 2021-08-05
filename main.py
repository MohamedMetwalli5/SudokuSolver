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

e00 = Entry(root,width='2', borderwidth='2', font=('Helvetica',24))
e00.grid(row=0, column=0, padx=2, pady=2)

e01 = Entry(root,width='2', borderwidth='2', font=('Helvetica',24))
e01.grid(row=0, column=1, padx=2, pady=2)

e02 = Entry(root,width='2', borderwidth='2', font=('Helvetica',24))
e02.grid(row=0, column=2, padx=2, pady=2)

e03 = Entry(root,width='2', borderwidth='2', font=('Helvetica',24))
e03.grid(row=0, column=3, padx=2, pady=2)

e04 = Entry(root,width='2', borderwidth='2', font=('Helvetica',24))
e04.grid(row=0, column=4, padx=2, pady=2)

e05 = Entry(root,width='2', borderwidth='2', font=('Helvetica',24))
e05.grid(row=0, column=5, padx=2, pady=2)

e06 = Entry(root,width='2', borderwidth='2', font=('Helvetica',24))
e06.grid(row=0, column=6, padx=2, pady=2)

e07 = Entry(root,width='2', borderwidth='2', font=('Helvetica',24))
e07.grid(row=0, column=7, padx=2, pady=2)

e08 = Entry(root,width='2', borderwidth='2', font=('Helvetica',24))
e08.grid(row=0, column=8, padx=2, pady=2)
######################################
e10 = Entry(root,width='2', borderwidth='2', font=('Helvetica',24))
e10.grid(row=1, column=0, padx=2, pady=2)

e11 = Entry(root,width='2', borderwidth='2', font=('Helvetica',24))
e11.grid(row=1, column=1, padx=2, pady=2)

e12 = Entry(root,width='2', borderwidth='2', font=('Helvetica',24))
e12.grid(row=1, column=2, padx=2, pady=2)

e13 = Entry(root,width='2', borderwidth='2', font=('Helvetica',24))
e13.grid(row=1, column=3, padx=2, pady=2)

e14 = Entry(root,width='2', borderwidth='2', font=('Helvetica',24))
e14.grid(row=1, column=4, padx=2, pady=2)

e15 = Entry(root,width='2', borderwidth='2', font=('Helvetica',24))
e15.grid(row=1, column=5, padx=2, pady=2)

e16 = Entry(root,width='2', borderwidth='2', font=('Helvetica',24))
e16.grid(row=1, column=6, padx=2, pady=2)

e17 = Entry(root,width='2', borderwidth='2', font=('Helvetica',24))
e17.grid(row=1, column=7, padx=2, pady=2)

e18 = Entry(root,width='2', borderwidth='2', font=('Helvetica',24))
e18.grid(row=1, column=8, padx=2, pady=2)
##############################################################
e20 = Entry(root,width='2', borderwidth='2', font=('Helvetica',24))
e20.grid(row=2, column=0, padx=2, pady=2)

e21 = Entry(root,width='2', borderwidth='2', font=('Helvetica',24))
e21.grid(row=2, column=1, padx=2, pady=2)

e22 = Entry(root,width='2', borderwidth='2', font=('Helvetica',24))
e22.grid(row=2, column=2, padx=2, pady=2)

e23 = Entry(root,width='2', borderwidth='2', font=('Helvetica',24))
e23.grid(row=2, column=3, padx=2, pady=2)

e24 = Entry(root,width='2', borderwidth='2', font=('Helvetica',24))
e24.grid(row=2, column=4, padx=2, pady=2)

e25 = Entry(root,width='2', borderwidth='2', font=('Helvetica',24))
e25.grid(row=2, column=5, padx=2, pady=2)

e26 = Entry(root,width='2', borderwidth='2', font=('Helvetica',24))
e26.grid(row=2, column=6, padx=2, pady=2)

e27 = Entry(root,width='2', borderwidth='2', font=('Helvetica',24))
e27.grid(row=2, column=7, padx=2, pady=2)

e28 = Entry(root,width='2', borderwidth='2', font=('Helvetica',24))
e28.grid(row=2, column=8, padx=2, pady=2)

##############################################################
e30 = Entry(root,width='2', borderwidth='2', font=('Helvetica',24))
e30.grid(row=3, column=0, padx=2, pady=2)

e31 = Entry(root,width='2', borderwidth='2', font=('Helvetica',24))
e31.grid(row=3, column=1, padx=2, pady=2)

e32 = Entry(root,width='2', borderwidth='2', font=('Helvetica',24))
e32.grid(row=3, column=2, padx=2, pady=2)

e33 = Entry(root,width='2', borderwidth='2', font=('Helvetica',24))
e33.grid(row=3, column=3, padx=2, pady=2)

e34 = Entry(root,width='2', borderwidth='2', font=('Helvetica',24))
e34.grid(row=3, column=4, padx=2, pady=2)

e35 = Entry(root,width='2', borderwidth='2', font=('Helvetica',24))
e35.grid(row=3, column=5, padx=2, pady=2)

e36 = Entry(root,width='2', borderwidth='2', font=('Helvetica',24))
e36.grid(row=3, column=6, padx=2, pady=2)

e37 = Entry(root,width='2', borderwidth='2', font=('Helvetica',24))
e37.grid(row=3, column=7, padx=2, pady=2)

e38 = Entry(root,width='2', borderwidth='2', font=('Helvetica',24))
e38.grid(row=3, column=8, padx=2, pady=2)
##############################################################
e40 = Entry(root,width='2', borderwidth='2', font=('Helvetica',24))
e40.grid(row=4, column=0, padx=2, pady=2)

e41 = Entry(root,width='2', borderwidth='2', font=('Helvetica',24))
e41.grid(row=4, column=1, padx=2, pady=2)

e42 = Entry(root,width='2', borderwidth='2', font=('Helvetica',24))
e42.grid(row=4, column=2, padx=2, pady=2)

e43 = Entry(root,width='2', borderwidth='2', font=('Helvetica',24))
e43.grid(row=4, column=3, padx=2, pady=2)

e44 = Entry(root,width='2', borderwidth='2', font=('Helvetica',24))
e44.grid(row=4, column=4, padx=2, pady=2)

e45 = Entry(root,width='2', borderwidth='2', font=('Helvetica',24))
e45.grid(row=4, column=5, padx=2, pady=2)

e46 = Entry(root,width='2', borderwidth='2', font=('Helvetica',24))
e46.grid(row=4, column=6, padx=2, pady=2)

e47 = Entry(root,width='2', borderwidth='2', font=('Helvetica',24))
e47.grid(row=4, column=7, padx=2, pady=2)

e48 = Entry(root,width='2', borderwidth='2', font=('Helvetica',24))
e48.grid(row=4, column=8, padx=2, pady=2)

##############################################################
e50 = Entry(root,width='2', borderwidth='2', font=('Helvetica',24))
e50.grid(row=5, column=0, padx=2, pady=2)

e51 = Entry(root,width='2', borderwidth='2', font=('Helvetica',24))
e51.grid(row=5, column=1, padx=2, pady=2)

e52 = Entry(root,width='2', borderwidth='2', font=('Helvetica',24))
e52.grid(row=5, column=2, padx=2, pady=2)

e53 = Entry(root,width='2', borderwidth='2', font=('Helvetica',24))
e53.grid(row=5, column=3, padx=2, pady=2)

e54 = Entry(root,width='2', borderwidth='2', font=('Helvetica',24))
e54.grid(row=5, column=4, padx=2, pady=2)

e55 = Entry(root,width='2', borderwidth='2', font=('Helvetica',24))
e55.grid(row=5, column=5, padx=2, pady=2)

e56 = Entry(root,width='2', borderwidth='2', font=('Helvetica',24))
e56.grid(row=5, column=6, padx=2, pady=2)

e57 = Entry(root,width='2', borderwidth='2', font=('Helvetica',24))
e57.grid(row=5, column=7, padx=2, pady=2)

e58 = Entry(root,width='2', borderwidth='2', font=('Helvetica',24))
e58.grid(row=5, column=8, padx=2, pady=2)

##############################################################
e60 = Entry(root,width='2', borderwidth='2', font=('Helvetica',24))
e60.grid(row=6, column=0, padx=2, pady=2)

e61 = Entry(root,width='2', borderwidth='2', font=('Helvetica',24))
e61.grid(row=6, column=1, padx=2, pady=2)

e62 = Entry(root,width='2', borderwidth='2', font=('Helvetica',24))
e62.grid(row=6, column=2, padx=2, pady=2)

e63 = Entry(root,width='2', borderwidth='2', font=('Helvetica',24))
e63.grid(row=6, column=3, padx=2, pady=2)

e64 = Entry(root,width='2', borderwidth='2', font=('Helvetica',24))
e64.grid(row=6, column=4, padx=2, pady=2)

e65 = Entry(root,width='2', borderwidth='2', font=('Helvetica',24))
e65.grid(row=6, column=5, padx=2, pady=2)

e66 = Entry(root,width='2', borderwidth='2', font=('Helvetica',24))
e66.grid(row=6, column=6, padx=2, pady=2)

e67 = Entry(root,width='2', borderwidth='2', font=('Helvetica',24))
e67.grid(row=6, column=7, padx=2, pady=2)

e68 = Entry(root,width='2', borderwidth='2', font=('Helvetica',24))
e68.grid(row=6, column=8, padx=2, pady=2)

##############################################################
e70 = Entry(root,width='2', borderwidth='2', font=('Helvetica',24))
e70.grid(row=7, column=0, padx=2, pady=2)

e71 = Entry(root,width='2', borderwidth='2', font=('Helvetica',24))
e71.grid(row=7, column=1, padx=2, pady=2)

e72 = Entry(root,width='2', borderwidth='2', font=('Helvetica',24))
e72.grid(row=7, column=2, padx=2, pady=2)

e73 = Entry(root,width='2', borderwidth='2', font=('Helvetica',24))
e73.grid(row=7, column=3, padx=2, pady=2)

e74 = Entry(root,width='2', borderwidth='2', font=('Helvetica',24))
e74.grid(row=7, column=4, padx=2, pady=2)

e75 = Entry(root,width='2', borderwidth='2', font=('Helvetica',24))
e75.grid(row=7, column=5, padx=2, pady=2)

e76 = Entry(root,width='2', borderwidth='2', font=('Helvetica',24))
e76.grid(row=7, column=6, padx=2, pady=2)

e77 = Entry(root,width='2', borderwidth='2', font=('Helvetica',24))
e77.grid(row=7, column=7, padx=2, pady=2)

e78 = Entry(root,width='2', borderwidth='2', font=('Helvetica',24))
e78.grid(row=7, column=8, padx=2, pady=2)

##############################################################
e80 = Entry(root,width='2', borderwidth='2', font=('Helvetica',24))
e80.grid(row=8, column=0, padx=2, pady=2)

e81 = Entry(root,width='2', borderwidth='2', font=('Helvetica',24))
e81.grid(row=8, column=1, padx=2, pady=2)

e82 = Entry(root,width='2', borderwidth='2', font=('Helvetica',24))
e82.grid(row=8, column=2, padx=2, pady=2)

e83 = Entry(root,width='2', borderwidth='2', font=('Helvetica',24))
e83.grid(row=8, column=3, padx=2, pady=2)

e84 = Entry(root,width='2', borderwidth='2', font=('Helvetica',24))
e84.grid(row=8, column=4, padx=2, pady=2)

e85 = Entry(root,width='2', borderwidth='2', font=('Helvetica',24))
e85.grid(row=8, column=5, padx=2, pady=2)

e86 = Entry(root,width='2', borderwidth='2', font=('Helvetica',24))
e86.grid(row=8, column=6, padx=2, pady=2)

e87 = Entry(root,width='2', borderwidth='2', font=('Helvetica',24))
e87.grid(row=8, column=7, padx=2, pady=2)

e88 = Entry(root,width='2', borderwidth='2', font=('Helvetica',24))
e88.grid(row=8, column=8, padx=2, pady=2)
########################################################################



def solve():
    global l
    global l_integer
    l[0][0] = e00.get()
    l[0][1] = e01.get()
    l[0][2] = e02.get()
    l[0][3] = e03.get()
    l[0][4] = e04.get()
    l[0][5] = e05.get()
    l[0][6] = e06.get()
    l[0][7] = e07.get()
    l[0][8] = e08.get()

    l[1][0] = e10.get()
    l[1][1] = e11.get()
    l[1][2] = e12.get()
    l[1][3] = e13.get()
    l[1][4] = e14.get()
    l[1][5] = e15.get()
    l[1][6] = e16.get()
    l[1][7] = e17.get()
    l[1][8] = e18.get()

    l[2][0] = e20.get()
    l[2][1] = e21.get()
    l[2][2] = e22.get()
    l[2][3] = e23.get()
    l[2][4] = e24.get()
    l[2][5] = e25.get()
    l[2][6] = e26.get()
    l[2][7] = e27.get()
    l[2][8] = e28.get()

    l[3][0] = e30.get()
    l[3][1] = e31.get()
    l[3][2] = e32.get()
    l[3][3] = e33.get()
    l[3][4] = e34.get()
    l[3][5] = e35.get()
    l[3][6] = e36.get()
    l[3][7] = e37.get()
    l[3][8] = e38.get()

    l[4][0] = e40.get()
    l[4][1] = e41.get()
    l[4][2] = e42.get()
    l[4][3] = e43.get()
    l[4][4] = e44.get()
    l[4][5] = e45.get()
    l[4][6] = e46.get()
    l[4][7] = e47.get()
    l[4][8] = e48.get()

    l[5][0] = e50.get()
    l[5][1] = e51.get()
    l[5][2] = e52.get()
    l[5][3] = e53.get()
    l[5][4] = e54.get()
    l[5][5] = e55.get()
    l[5][6] = e56.get()
    l[5][7] = e57.get()
    l[5][8] = e58.get()

    l[6][0] = e60.get()
    l[6][1] = e61.get()
    l[6][2] = e62.get()
    l[6][3] = e63.get()
    l[6][4] = e64.get()
    l[6][5] = e65.get()
    l[6][6] = e66.get()
    l[6][7] = e67.get()
    l[6][8] = e68.get()

    l[7][0] = e70.get()
    l[7][1] = e71.get()
    l[7][2] = e72.get()
    l[7][3] = e73.get()
    l[7][4] = e74.get()
    l[7][5] = e75.get()
    l[7][6] = e76.get()
    l[7][7] = e77.get()
    l[7][8] = e78.get()

    l[8][0] = e80.get()
    l[8][1] = e81.get()
    l[8][2] = e82.get()
    l[8][3] = e83.get()
    l[8][4] = e84.get()
    l[8][5] = e85.get()
    l[8][6] = e86.get()
    l[8][7] = e87.get()
    l[8][8] = e88.get()
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
    e00.delete(0, END)
    e00.insert(END, l_integer[0][0])
    e01.delete(0, END)
    e01.insert(END, l_integer[0][1])
    e02.delete(0, END)
    e02.insert(END, l_integer[0][2])
    e03.delete(0, END)
    e03.insert(END, l_integer[0][3])
    e04.delete(0, END)
    e04.insert(END, l_integer[0][4])
    e05.delete(0, END)
    e05.insert(END, l_integer[0][5])
    e06.delete(0, END)
    e06.insert(END, l_integer[0][6])
    e07.delete(0, END)
    e07.insert(END, l_integer[0][7])
    e08.delete(0, END)
    e08.insert(END, l_integer[0][8])

    root.update()

    e10.delete(0, END)
    e10.insert(END, l_integer[1][0])
    e11.delete(0, END)
    e11.insert(END, l_integer[1][1])
    e12.delete(0, END)
    e12.insert(END, l_integer[1][2])
    e13.delete(0, END)
    e13.insert(END, l_integer[1][3])
    e14.delete(0, END)
    e14.insert(END, l_integer[1][4])
    e15.delete(0, END)
    e15.insert(END, l_integer[1][5])
    e16.delete(0, END)
    e16.insert(END, l_integer[1][6])
    e17.delete(0, END)
    e17.insert(END, l_integer[1][7])
    e18.delete(0, END)
    e18.insert(END, l_integer[1][8])

    root.update()

    e20.delete(0, END)
    e20.insert(END, l_integer[2][0])
    e21.delete(0, END)
    e21.insert(END, l_integer[2][1])
    e22.delete(0, END)
    e22.insert(END, l_integer[2][2])
    e23.delete(0, END)
    e23.insert(END, l_integer[2][3])
    e24.delete(0, END)
    e24.insert(END, l_integer[2][4])
    e25.delete(0, END)
    e25.insert(END, l_integer[2][5])
    e26.delete(0, END)
    e26.insert(END, l_integer[2][6])
    e27.delete(0, END)
    e27.insert(END, l_integer[2][7])
    e28.delete(0, END)
    e28.insert(END, l_integer[2][8])

    root.update()

    e30.delete(0, END)
    e30.insert(END, l_integer[3][0])
    e31.delete(0, END)
    e31.insert(END, l_integer[3][1])
    e32.delete(0, END)
    e32.insert(END, l_integer[3][2])
    e33.delete(0, END)
    e33.insert(END, l_integer[3][3])
    e34.delete(0, END)
    e34.insert(END, l_integer[3][4])
    e35.delete(0, END)
    e35.insert(END, l_integer[3][5])
    e36.delete(0, END)
    e36.insert(END, l_integer[3][6])
    e37.delete(0, END)
    e37.insert(END, l_integer[3][7])
    e38.delete(0, END)
    e38.insert(END, l_integer[3][8])

    root.update()

    e40.delete(0, END)
    e40.insert(END, l_integer[4][0])
    e41.delete(0, END)
    e41.insert(END, l_integer[4][1])
    e42.delete(0, END)
    e42.insert(END, l_integer[4][2])
    e43.delete(0, END)
    e43.insert(END, l_integer[4][3])
    e44.delete(0, END)
    e44.insert(END, l_integer[4][4])
    e45.delete(0, END)
    e45.insert(END, l_integer[4][5])
    e46.delete(0, END)
    e46.insert(END, l_integer[4][6])
    e47.delete(0, END)
    e47.insert(END, l_integer[4][7])
    e48.delete(0, END)
    e48.insert(END, l_integer[4][8])

    root.update()

    e50.delete(0, END)
    e50.insert(END, l_integer[5][0])
    e51.delete(0, END)
    e51.insert(END, l_integer[5][1])
    e52.delete(0, END)
    e52.insert(END, l_integer[5][2])
    e53.delete(0, END)
    e53.insert(END, l_integer[5][3])
    e54.delete(0, END)
    e54.insert(END, l_integer[5][4])
    e55.delete(0, END)
    e55.insert(END, l_integer[5][5])
    e56.delete(0, END)
    e56.insert(END, l_integer[5][6])
    e57.delete(0, END)
    e57.insert(END, l_integer[5][7])
    e58.delete(0, END)
    e58.insert(END, l_integer[5][8])

    root.update()

    e60.delete(0, END)
    e60.insert(END, l_integer[6][0])
    e61.delete(0, END)
    e61.insert(END, l_integer[6][1])
    e62.delete(0, END)
    e62.insert(END, l_integer[6][2])
    e63.delete(0, END)
    e63.insert(END, l_integer[6][3])
    e64.delete(0, END)
    e64.insert(END, l_integer[6][4])
    e65.delete(0, END)
    e65.insert(END, l_integer[6][5])
    e66.delete(0, END)
    e66.insert(END, l_integer[6][6])
    e67.delete(0, END)
    e67.insert(END, l_integer[6][7])
    e68.delete(0, END)
    e68.insert(END, l_integer[6][8])

    root.update()

    e70.delete(0, END)
    e70.insert(END, l_integer[7][0])
    e71.delete(0, END)
    e71.insert(END, l_integer[7][1])
    e72.delete(0, END)
    e72.insert(END, l_integer[7][2])
    e73.delete(0, END)
    e73.insert(END, l_integer[7][3])
    e74.delete(0, END)
    e74.insert(END, l_integer[7][4])
    e75.delete(0, END)
    e75.insert(END, l_integer[7][5])
    e76.delete(0, END)
    e76.insert(END, l_integer[7][6])
    e77.delete(0, END)
    e77.insert(END, l_integer[7][7])
    e78.delete(0, END)
    e78.insert(END, l_integer[7][8])

    root.update()

    e80.delete(0, END)
    e80.insert(END, l_integer[8][0])
    e81.delete(0, END)
    e81.insert(END, l_integer[8][1])
    e82.delete(0, END)
    e82.insert(END, l_integer[8][2])
    e83.delete(0, END)
    e83.insert(END, l_integer[8][3])
    e84.delete(0, END)
    e84.insert(END, l_integer[8][4])
    e85.delete(0, END)
    e85.insert(END, l_integer[8][5])
    e86.delete(0, END)
    e86.insert(END, l_integer[8][6])
    e87.delete(0, END)
    e87.insert(END, l_integer[8][7])
    e88.delete(0, END)
    e88.insert(END, l_integer[8][8])

    root.update()

    e00.delete(0, END)
    e00.insert(END, l_integer[0][0])
    e01.delete(0, END)
    e01.insert(END, l_integer[0][1])
    e02.delete(0, END)
    e02.insert(END, l_integer[0][2])
    e03.delete(0, END)
    e03.insert(END, l_integer[0][3])
    e04.delete(0, END)
    e04.insert(END, l_integer[0][4])
    e05.delete(0, END)
    e05.insert(END, l_integer[0][5])
    e06.delete(0, END)
    e06.insert(END, l_integer[0][6])
    e07.delete(0, END)
    e07.insert(END, l_integer[0][7])
    e08.delete(0, END)
    e08.insert(END, l_integer[0][8])
    root.update()
    time.sleep(60)  # after 60 seconds of showing the solution the program exits by itself
    exit(0)

SolveButton = Button(root, padx=30, bg="yellow", font=50 , text="Solve", command=solve)
SolveButton.grid(row=10, column=9)
root.mainloop()
