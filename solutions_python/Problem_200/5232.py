import pygame
import copy
import math
from random import randint
import os.path
from pathlib import Path
def isnin(i):
    i=list(str(i))
    j=len(i)-1
    k=100
    print("sdf", i[j])
    if (int(i[j]) != 0):
        return False
    j=j-1
    while(j>=0):
        print("sdf",j)
        if(int(i[j])==1):
            j = j - 1
            continue
        else:
            return False

    return True
def convert(i):
    t=str(i)
    j=len(t)-1
    k=[]
    for l in range(j):
        k.append('9')
    return int("".join(k))
def isTidy(i):
    i=list(str(i))
    j=len(i)-1
    k=100
    while(j>=0):
        if(int(i[j])<=k):
            k=int(i[j])
        else:
            return False
        j=j-1
    return True
def solveTidy(i):
    fl=0
    while(0<i):
        print(i)
        if(isnin(i)):
            return convert(i)
        if(isTidy(i)):
            return i
        else:
            i=i-1


file = open("text.txt", "r")
file2=open("results.txt", "w")
l = file.readline()
n=int(l)
for i in range(n):
    l = file.readline().replace(' ','')
    print('hi')
    fl=solveTidy(int(l))
    file2.write("Case #" + str(i+1)+': ' + str(fl)+'\n' )
