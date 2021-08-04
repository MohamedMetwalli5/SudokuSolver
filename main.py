from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.geometry("530x600")
root.resizable(width=0, height=0)
root.title('Sudoku Solver')

background = ImageTk.PhotoImage(Image.open("C:/Users/Mohamed/PycharmProjects/SudokuSolver/Background.jpg"))
background_label = Label(image=background)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

l = [["0" for i in range(9)] for j in range(9)]

# for i in range(0,9):
#     for j in range(0, 9):
#         e = Entry(root,width='2', borderwidth='2', font=('Helvetica',24))
#         e.grid(row=i, column=j, padx=2, pady=2)

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
    print(l)

SolveButton = Button(root, padx=30, bg="yellow", font=50 , text="Solve", command=solve)
SolveButton.grid(row=10, column=9)


root.mainloop()
