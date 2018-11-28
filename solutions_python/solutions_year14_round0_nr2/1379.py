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
def NextFloatList():
    strings = f.readline().split()
    floats = []
    for string in strings:
        floats.append(float(string))
    return floats
def NextStr():
    string = str(f.readline())
    return string.replace('\n',"")
def Main():
    output = ""
    for t in range(1,T+1,1):
        output +="Case #%d: "%t + Case() + "\n"
    WriteOutput(output)
def Case():
    C,F,X = NextFloatList()
    cps = 2.0
    time = 0.0
    while (1):
        tw = X/cps
        if (C/cps + X/(cps+F))>(tw):
            return str(round(time + tw,7))
        time += C/cps
        cps += F
    return ""
if __name__ == '__main__':
    Main()
