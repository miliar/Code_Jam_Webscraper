#!/usr/bin/python

import fileinput 

def intersect(a, b):
     return list(set(a) & set(b))

fi=fileinput.input()
nTestCases=int(fi.readline())

for testNumber in range(1, nTestCases+1):
    i1=int(fi.readline())
    grid1=[]
    grid1.append(map(int,fi.readline().strip().split(" ")))
    grid1.append(map(int,fi.readline().strip().split(" ")))
    grid1.append(map(int,fi.readline().strip().split(" ")))
    grid1.append(map(int,fi.readline().strip().split(" ")))
    #print grid1
    s1=grid1[i1-1]
    #print grid
    i2=int(fi.readline())
    grid2=[]
    grid2.append(map(int,fi.readline().strip().split(" ")))
    grid2.append(map(int,fi.readline().strip().split(" ")))
    grid2.append(map(int,fi.readline().strip().split(" ")))
    grid2.append(map(int,fi.readline().strip().split(" ")))
    #print grid2
    s2=grid2[i2-1]
    resultSet=intersect(s1, s2)
    resultCount=len(resultSet)
    if resultCount==0:
        result="Volunteer cheated!"
    elif resultCount>1:
        result="Bad magician!"
    else:
        result="%d"%resultSet[0]
    print("Case #%d: %s"% (testNumber, result))



