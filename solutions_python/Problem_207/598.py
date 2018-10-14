#!/usr/bin/env python
from math import *
from sys import *

numcases = int(stdin.readline())


def isValid(color,number):
    global N
    global stable
    if number <= 0:
        return False
    if (stable[len(stable) -1] == color):
        return False
    if len(stable) == N-1 and stable[0] == color:
        return False
    return True


def attempt(color):
    global N
    global stable
    if (isValid(color,1)):
        stable = stable + color
        return True
    return False
    
    

for case in range(1,numcases+1):
    global N
    global stable
    data = map(int,stdin.readline().split())
    N = data[0]
    R = data[1]
    Y = data[3]
    B = data[5]
    maxc = max(R,Y,B)
    first = ""
    if maxc == R:
        stable = "R"
        R -= 1
        first = "R"
    elif maxc == Y:
        stable = "Y"
        Y -= 1
        first = "Y"
    else:
        stable = "B"
        B -= 1
        first = "B"


    
    impossible = False
    for i in range(N-1):
        done = False
        Rvalid = isValid("R",R)
        Yvalid = isValid("Y",Y)
        Bvalid = isValid("B",B)
        if Rvalid:
            if (not( Yvalid or Bvalid)) or ((not Yvalid )and (R > B or (R==B and first== "R"))) or ((not Bvalid )and (R > Y or (R==B and first=="R"))) or (R > B and R > Y) or (R == Y and R == B and first=="R") :
                attempt("R")
                R -= 1
                continue
        if Bvalid:
            if (B > Y) or not Yvalid or (B==Y and first=="B"):
                attempt("B")
                B -= 1
                continue
        if Yvalid:
            attempt("Y")
            Y -= 1
            continue
        impossible = True
        

                
            

    if impossible:
        print "Case #" + str(case) + ": " + "IMPOSSIBLE"
    else:
        print "Case #" + str(case) + ": " + stable


