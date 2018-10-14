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
import os,math,sys,copy,random
f = open("A-small-attempt1.in")
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
    ######### TO DO ##########
    for t in range(1,T+1,1):
        output +="Case #%d: "%t + Case() + "\n"
    WriteOutput(output)
def Divide(t):
    return (t[0:int(len(t)/2)],t[int(len(t)/2):len(t)])
def Merge(t1,t2):
    if (len(t1) is 0):
        return t2
    if (len(t2) is 0):
        return t1
    if (t1[0]<t2[0]):
        return ([t1[0]] + Merge(t1[1:],t2))
    else:
        return ([t2[0]] + Merge(t1,t2[1:]))
def Sort(t):
    if (len(t)<2):
        return t
    else:
        t1,t2 = Divide(t)
        return Merge(Sort(t1),Sort(t2))
def Checks(s,t,score,A):
    if t==[]:
        return score
    if A is 0:
        return score
    a = t[0]
    if s>a:
        return Checks(s+a,t[1:],score,A)
    elif s-1+s>a:
        return Checks(s+s-1+a,t[1:],score+1,A)
    else:
        return min(Checks(s+s-1,t,score+1,A-1),Checks(s,t[1:],score+1,A))
def Case():
    output = ""
    S,A = NextIntList()
    motes = NextIntList()
    ######### TO DO ##########
    motes = Sort(motes)
    m2=Checks(S,motes,0,A)
    output += str(m2)
    return output
if __name__ == '__main__':
    Main()
