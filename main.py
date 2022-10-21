from operator import truediv
from tkinter import N


board=[[0]*8 for _ in range (8)]

def ocupat(i,j):
    for k in range (0,8):
        if board[i][k]==1 or board[k][j]==1:
            return True
    return False

def turnuri(n):
    for i in range (0,n):
        for j in range (0,n):
            if (not(ocupat(i,j))) and (board[i][j]!=1):
                board[i][j]=1

for m in range(0,8):
    for n in range (0,8):
       board=[[0]*8 for _ in range (8)]
       board[m][n]=1 
       print("________________Primul Turn pe Pozitia ",m,n,"________________")
       turnuri(8)
       for l in board: 
            print(l)

