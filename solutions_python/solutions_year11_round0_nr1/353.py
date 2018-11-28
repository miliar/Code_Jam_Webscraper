#!/usr/bin/python
import sys


n=int(sys.stdin.readline())
old=n
while n>0:
    prevb=1
    prevbs=0
    prevo=1
    prevos=0
    sec=0
    n=n-1
    x=sys.stdin.readline()
    xs=x.split()
    nb=int(xs[0])
    i=1
    while nb>0:
        if xs[i]=='O':
            if (sec - prevos) >= abs(int(xs[i+1]) - prevo) :
                sec = sec + 1
            else:
                sec = sec + 1 + (abs(int(xs[i+1]) - prevo) - (sec - prevos))
            prevos = sec
            prevo=int(xs[i+1])
        elif xs[i]=='B':
            if (sec - prevbs) >= abs(int(xs[i+1]) - prevb) :
                sec = sec + 1
            else:
                sec = sec + 1 + (abs(int(xs[i+1]) - prevb) - (sec - prevbs))
            prevbs = sec
            prevb=int(xs[i+1])
        i=i+2
        nb=nb-1
    print "Case #" + str(old-n) + ": " + str(sec)

