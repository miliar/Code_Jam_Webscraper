#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      qmarchal
#
# Created:     11/04/2013
# Copyright:   (c) qmarchal 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os,math,sys
f = open("A-small-attempt0.in")
T = int(f.readline())
squares = []
values = []
def WriteOutput(output):
    w = open("ouput.txt","w")
    w.write(output)
    w.close()
def Print(string):
    sys.stdout.write(str(string)+"\n")
def NextInt():
    return int(f.readline())
def NextList():
    return f.readline().split()
def NextIntList():
    strings = f.readline().split()
    ints = []
    for string in strings:
        ints.append(int(string))
    return ints
def NextStr():
    return f.readline()
def Area(j,r):
    return values[j]+2*(j+1)*r
def DoList():
    s=0
    for i in range(0,2001,1):
        squares.append(i*i)
        if i is not 0 and i%2 is 1:
            s+=squares[i]-squares[i-1]
            values.append(s)
def Main():
    output = ""
    ######### TO DO ##########
    DoList()
    for t in range(1,T+1,1):
        output +="Case #%d: "%t + Case() + "\n"
    WriteOutput(output)
def Case():
    output = ""
    r,t = NextIntList()
    ######### TO DO ##########
    s=0
    i=0
    while t>=Area(i,r):
        i+=1
    output += str(i)
    return output
if __name__ == '__main__':
    Main()
