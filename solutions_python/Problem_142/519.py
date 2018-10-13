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
import os,math,sys,copy
f = open("input.txt")
T = int(f.readline())

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
    string = str(f.readline())
    return string.replace('\n',"")
def Main():
    output = ""
    for t in range(1,T+1,1):
        output +="Case #%d: "%t + Case() + "\n"
    WriteOutput(output)
def Count(mot):
    temp = ""
    basic = ""
    occurs = []
    for lettre in mot:
        if lettre != temp:
            temp = lettre
            basic += lettre
            occurs.append(1)
        else:
            occurs[len(occurs)-1]+=1
    return occurs
def Cut(mot):
    temp = ""
    basic = ""
    for lettre in mot:
        if lettre != temp:
            temp = lettre
            basic += lettre
    return basic
def IsOK(mot, w):
    return (w==Cut(mot))
def Abs(a,b):
    return (int(math.fabs(a-b)))
def Case():
    N = NextInt()
    first = NextStr()
    w = Cut(first)
    second = NextStr()
    x = 0
    output = ""
    if IsOK(second, w):
        t = []
        t.append(Count(first))
        t.append(Count(second))
        for i in range(0,len(t[0])):
            x+=Abs(t[0][i],t[1][i])
        output = str(x)
    else:
        output = "Fegla Won"
    return output
if __name__ == '__main__':
    Main()
