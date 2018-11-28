import sys
import os
import subprocess
import Tkinter

def main():
    from tkFileDialog import askopenfilename
    root=Tkinter.Tk()
    root.withdraw()
    nameIn = askopenfilename(title="Tic-Tac-Toe-Tomek",filetypes=[("text","*.txt"),("all files","*")])
    file = open(nameIn,"r")
    T=file.readline()

    ofile = open("output.txt","w")
    
    board=[]
    for i in range(0,int(T)):
        board=[]
        for j in range(0,4):
            row=file.readline()
            row=list(row[0:4])
            board.append(row)
        file.readline()
        state = TicTacToeTomek(board)
        ofile.write("Case #"+str(i+1)+': '+state+'\n')


def TicTacToeTomek(board):

    for s in board:
        if set(s)==set('X') or set(s)==set(['X','T']): return "X won"
        if set(s)==set('O') or set(s)==set(['O','T']): return "O won"

    for j in range(0,4):
        col=set()
        for i in range(0,4):
            col.add(board[i][j])
        if set(col)==set('X') or set(col)==set(['X','T']): return "X won"
        if set(col)==set('O') or set(col)==set(['O','T']): return "O won"
    col=set()
    for i in range(0,4):
        col.add(board[i][i])
    if set(col)==set('X') or set(col)==set(['X','T']): return "X won"
    if set(col)==set('O') or set(col)==set(['O','T']): return "O won"
    col=set()
    for i in range(0,4):
        col.add(board[i][3-i])
    if set(col)==set('X') or set(col)==set(['X','T']): return "X won"
    if set(col)==set('O') or set(col)==set(['O','T']): return "O won"
    for s in board:
        if "." in set(s):
            return "Game has not completed"
    return "Draw"
        
