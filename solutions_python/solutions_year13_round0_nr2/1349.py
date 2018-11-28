#!/usr/bin/python

def prettyPrint(l):
    rows = len(l)
    i = 0 

    while i < rows :
        print l[i]
        i = i + 1
    print "****************************************************************"

def checkRow(lawn,i):
    M = len(lawn[i])
    val = lawn[i][0]
    for j in range(0,M):
        if lawn[i][j] != val:
            return False
    return True
    
def checkColumn(lawn,j) :
    N = len(lawn)
    val = lawn[0][j]
    for i in range(0,N):
        if lawn[i][j] != val:
            return False
    return True

def mowLawn(lawn):
    if lawn == [] :
        return True
    (N,M) = (len(lawn),len(lawn[0]))
    least = 100
    leastLocation = (0,0)
    for i in range(0,N):
        for j in range(0,M):
            if lawn[i][j] < least:
                least = lawn[i][j]
                leastLocation = (i,j)
    return reduceLawn(lawn,leastLocation[0],leastLocation[1])

def reduceLawn(lawn,i,j):
    (N,M) = (len(lawn),len(lawn[0]))
    lawn1 = []

    if checkRow(lawn,i):
        lawn1 = lawn[:i]+lawn[i+1:]
        return mowLawn(lawn1)

    if checkColumn(lawn,j):
        for i in range(0,N):
            newCol = lawn[i][:j] + lawn[i][j+1:]
            lawn1 = lawn1 + [newCol]
        return mowLawn(lawn1)

    return False
                   
nCases=int(raw_input())
testCase=1

while (testCase <= nCases):
    line = raw_input().split()
    N = int(line[0])
    M = int(line[1])
    
# Obtain input for lawn    
    lawn = []
    for i in range(0,N):
        row = raw_input().split()
        for j in range(0,M):
            row[j] = int(row[j])
        lawn = lawn + [row]

    if mowLawn(lawn):
        print "Case #"+str(testCase)+": YES"
    else :
        print "Case #"+str(testCase)+": NO"        

    testCase = testCase+1
