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
def Case():
    i1 = NextInt()
    t1 = [NextIntList(),NextIntList(),NextIntList(),NextIntList()]
    R1 = t1[i1-1]
    i2 = NextInt()
    t2 = [NextIntList(),NextIntList(),NextIntList(),NextIntList()]
    R2 = t2[i2-1]
    x = 0
    for i in range(0,4,1):
        for j in range(0,4,1):
            if R1[i] == R2[j]:
                if x == 0:
                    x = R1[i]
                else:
                    return str("Bad magician!")
    if x == 0:
        return str("Volunteer cheated!")
    return str(x)
if __name__ == '__main__':
    Main()
