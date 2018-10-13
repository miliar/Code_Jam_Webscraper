# Brendan Wreford
import os
import math

# Create Output file
f = open('output.txt', "w")
f.close()

# Read Input file
f = open('A-small-attempt0 (1).in', "rb")
numOfTestCases = f.readline()
numOfTestCases = int(numOfTestCases)

for i in range(0,numOfTestCases):
    # Reading Logic
    case = f.readline()
    case = case.split()

    r = int(case[0])
    t = int(case[1])

    # Problem Logic
    y = (2*r-1)**2
    y = y+8*t
    y = y**0.5
    y=y+(1-2*r)
    y = y/4
    y = int(y)

    ty = y

    V1 = y*(-1 + 2*r + 2*y)
    A=0
    B=0
    if V1 < t:
        A = 1
    else:
        B = 1

    while(A):
        if V1 < t:
            ty = ty+1
            if ty*(-1 + 2*r + 2*ty)<t:
                y = ty
                V1 = y*(-1 + 2*r + 2*y)
            elif ty*(-1 + 2*r + 2*ty)>t:
                A = 0
        else:
            A = 0

    V1 = y*(-1 + 2*r + 2*y)
    while(B):
        if V1 > t:
            ty = ty-1
            if ty*(-1 + 2*r + 2*ty)<t:
                y = ty
                V1 = y*(-1 + 2*r + 2*y)
            elif ty*(-1 + 2*r + 2*ty)>t:
                B = 0
        else:
            B = 0

    # Write Output File
    g = open('output.txt', "a")
    g.write("Case #" + repr(i+1) + ": " + repr(y) + "\n")
    g.close
