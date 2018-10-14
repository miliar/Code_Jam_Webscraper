import sys
import os
import subprocess
import Tkinter

def main():
    from tkFileDialog import askopenfilename
    root=Tkinter.Tk()
    root.withdraw()
    nameIn = askopenfilename(title="Lawnmower",filetypes=[("text","*.txt"),("all files","*")])
    file = open(nameIn,"r")
    T=file.readline()
    ofile = open("output.txt","w")
    
    for i in range(0,int(T)):
        lawn=[]
        row=file.readline().rsplit()
        N=int(row[0])
        M=int(row[1])
        for j in range(0,N):
            row = file.readline().rsplit()
            row = [int(k) for k in row]
            lawn.append(row)
        state = Lawnmower(lawn,N,M)
        ofile.write("Case #"+str(i+1)+': '+state+'\n')


def Lawnmower(lawn,N,M):

    MaxRow=[]
    for row in lawn:
        MaxRow.append(max(row))
    MaxCol=[-1 for k in range(0,M)]

    for j in range(0,M):
        for i in range(0,N):
            if lawn[i][j]>MaxCol[j]:
                MaxCol[j]=lawn[i][j]

    for i in range(0,N):
        for j in range(0,M):
            if lawn[i][j]!=MaxRow[i] and lawn[i][j]!=MaxCol[j]:
                return "NO"
    return "YES"
