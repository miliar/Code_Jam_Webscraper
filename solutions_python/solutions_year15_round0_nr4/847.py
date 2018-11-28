#!/usr/bin/python

N=int(raw_input())
for i in xrange(0,N):
    line = raw_input().split()
    X=int(line[0])
    R=min(int(line[1]),int(line[2]))
    C=max(int(line[1]),int(line[2]))

    winner="GABRIEL"
    if((R*C)%X):
        winner="RICHARD"
    elif(X>C):
        winner="RICHARD"
    elif(X==3 and R==1 and C==3):
        winner="RICHARD"
    elif(X==4 and R==1 and C==4):
        winner="RICHARD"
    elif(X==4 and R==2 and C==4):
        winner="RICHARD"
    elif(X==5 and R==1 and C==5):
        winner="RICHARD"
    elif(X==5 and R==2 and C==5):
        winner="RICHARD"
    elif(X==6 and R==1 and C==6):
        winner="RICHARD"
    elif(X==6 and R==2 and C==6):
        winner="RICHARD"
    elif(X>7):
        winner="RICHARD"
        

    print("Case #"+repr(i+1)+": "+winner)
