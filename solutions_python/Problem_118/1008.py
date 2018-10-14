import sys
import os
import math
import Tkinter

def main():
    from tkFileDialog import askopenfilename
    root=Tkinter.Tk()
    root.withdraw()
    nameIn = askopenfilename(title="FairnSquare",filetypes=[("text","*.txt"),("all files","*")])
    file = open(nameIn,"r")
    T=file.readline()
    ofile = open("output.txt","w")
    
    for i in range(0,int(T)):
        row=file.readline().rsplit()
        A=int(row[0])
        B=int(row[1])
        number = FairSquare(A,B)
        ofile.write("Case #"+str(i+1)+': '+number+'\n')

def FairSquare(A,B):
    count=0
    for i in range(A,B+1):
        if fair(i) and fair(math.sqrt(i)):
            count+=1
    return str(count)

def fair(k):
    k=str(k)
    r=k[k.rfind(".")+1:]
    if "." in k and int(r)!=0:
        return False
    if "." in k:
        k=k[0:k.rfind(".")]
    e=len(k)-1;
    b=0
    while b<e:
        if k[b]!=k[e]:
            return False
        b+=1
        e-=1
    return True
