#!/usr/bin/python
import sys

T = int(sys.stdin.readline())
t = 1

def strTocharList(str1):
    i = 0
    lst = []
    while i < len(str1):
        lst += str1[i]
        i+=1
    return lst

def cLToStr(cL):
    str1 = ""
    for ch in cL:
        str1+=ch
    return str1
    

while t<=T:
    l = (sys.stdin.readline()).split()
    R = int(l[0])
    C = int(l[1])

    M = []
    i = 0
    while i<R:
        j = 0
        row = strTocharList(sys.stdin.readline()[:-1])
        M += [row]
        i+=1
        
#    print M

    answer=[]
    i=0
    while i<R:
        answer += [""]
        i+=1
    
    i=0
    while i<R:
        j = 0
        while j<C:
            if M[i][j]=='#':
                if i == (R-1) or j==(C-1) or M[i+1][j]!='#' or M[i][j+1] != '#' or M[i+1][j+1] != '#':
                    answer[0] = "Impossible"
                else :
                    M[i][j]='/'
                    M[i][j+1]='\\'
                    M[i+1][j]='\\'
                    M[i+1][j+1]='/'
            j+=1
        if answer[0] != "Impossible":
            answer[i] = cLToStr(M[i])
        i+=1

    if answer[0] == "Impossible":
        answer = ["Impossible"]

    print "Case #"+str(t)+":"
    for line in answer:
        print line

    t+=1
