#!/usr/bin/python
import sys

'''
str1 is a string of integers separated by space
to Int will return a list of integers 
'''
def strToIntList(str1):
    l=str1.split()
    i=0
    while i<len(l):
        l[i]=int(l[i])
        i+=1
    return l

def strToCharList(str1):
    strList = []
    i=0
    while i<len(str1):
        strList += str1[i]
        i += 1
    return strList

def prettyPrint(board):
    for row in board:
        print row 
    print    

'''
toTuple takes a list of integers, I
and returns a list of tuples, Ituples 
            where for every i, Ituples[i]=(i,I[i])
'''
def toTuple(I):
    i=0
    Ituples=[]
    while i<len(I):
        Ituples.append((i,I[i]))
        i+=1
    return Ituples

T = int(sys.stdin.readline())
t = 1

while t<=T :
    N = int(sys.stdin.readline())
    board = []

    i = 0
    while i<N:
        str1 = (strToCharList(sys.stdin.readline())[:-1])
        board += [str1]
        i+=1

#    print board

    rpi = []
    wp = []
    won = []
    played = []
    owpMat = []
    owp = []
    oowp = []
    
    for str1 in board:
        n,w = 0.0,0.0
        for ch in str1:
            if ch == '1' or ch == '0':
                n += 1
            if ch == '1':
                w += 1
        wp += [w/n]
        won += [w]
        played +=[n]

#    print wp
    i = 0
    while i<N:
        tot = 0.0
        opponents = 0.0
        curOwp = []
        j=0
        while j< N:
            if board[i][j] == '0':
                tot += (won[j]-1)/(played[j]-1)
                opponents += 1
            elif board[i][j] =='1' :
                tot += (won[j]/(played[j]-1))
                opponents += 1
            j+=1
        owp += [(tot / opponents)]
        i+=1

    i = 0
    while i<N:
        tot = 0.0
        opponents = 0.0
        curOwp = []
        j=0
        while j< N:
            if board[i][j] == '0' or board[i][j] =='1':
                tot += owp[j]
                opponents += 1
            j+=1
#        print str(i)+") tot,opponents "+str(tot)+","+str(opponents)
        oowp += [(tot / opponents)]
        i+=1

#    print wp[0]
    i=0
    while i< N:
        rpi += [0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i]]
        i += 1
    
    print "Case #"+str(t)+":"
#    print rpi
    for r in rpi:
        print r
    t+=1          
