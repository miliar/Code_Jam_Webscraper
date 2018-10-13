import sys
import os
import math
import Tkinter

def main():
    from tkFileDialog import askopenfilename
    root=Tkinter.Tk()
    root.withdraw()
    nameIn = askopenfilename(title="Bullseye",filetypes=[("text","*.txt"),("all files","*")])
    file = open(nameIn,"r")
    T=file.readline()
    ofile = open("output.txt","w")
    
    for i in range(0,int(T)):
        row=file.readline().rsplit()
        r=int(row[0])
        t=int(row[1])
        number = paint(r,t)
        ofile.write("Case #"+str(i+1)+': '+number+'\n')

def paint(r,t):
    rp=t
    count=0
    while (2*r+1)<=rp:
        count+=1
        rp-=2*r+1
        r+=2
    return str(count)
