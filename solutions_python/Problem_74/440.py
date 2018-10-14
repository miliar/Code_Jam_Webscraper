#!/usr/bin/python
import sys

def jumpTime(curr,next):
    if curr >= next:
        return (curr - next) 
    return (next - curr) 

def shortestTime(seq):
    pTime,cTime,tTime = 0,0,0
    robot = [['O',1],['B',1]]

    i=1
    n=len(seq)

    # Make all even positions as integers
    while i<n:
        seq[i]=int(seq[i])
        i+=2

    i=0
    while i<n:
        # Select the current Robot
        cR = 0
        if seq[i]=='B':
            cR=1

        # Synchronise the first jump
        cTime = 0
        nPos = seq[i+1]
        firstJump = jumpTime(robot[cR][1],nPos)
        if firstJump > pTime:
            cTime += (firstJump - pTime) 
        cTime += 1              
        robot[cR][1] = nPos     
        i += 2              

        # Compute the times for subsequent moves of the current robot
        while i<n and robot[cR][0] == seq[i]:
            nPos = seq[i+1]
            cTime += jumpTime(robot[cR][1],nPos) + 1
            robot[cR][1] = nPos 
            i+=2

        pTime = cTime  
        tTime += cTime

    return tTime

tests=int(sys.stdin.readline())
t=0

while t<tests:
    inString=(sys.stdin.readline()).split()
    seq=inString[1:]
    time=shortestTime(seq)
    print "Case #"+str(t+1)+": ",time
    t+=1
