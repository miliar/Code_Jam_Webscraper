import numpy as np


__author__ = 'vasilisakoinoglou'

DEVEL = False

inputf = open('s_in.txt', 'r') if DEVEL else open('in.txt', 'r')

outputf = open('s_out.txt', 'w') if DEVEL else open('out.txt', 'w')

T = 0

cases = []

def readInput():
    global T, cases
    with inputf as f:
        T = int(f.readline())
        for case in range(0, T):
            cases.append(f.readline().split())


def isFair(n):
    ns = str(n)
    return ns == ns[::-1]


def getSquares(A, B):
    squares = []
    for i in range(0, B+1):
        s = i * i
        if (s >= A) and (s <= B):
            if isFair(i):
                squares.append(s)
    return squares

def fairnsquares(A,B):
    fas = 0
    for n in getSquares(A, B):
        if isFair(n):
            fas += 1
    return fas

readInput()
#print '='*80
#print cases

results = []
for i, case in enumerate(cases):
    casen = i+1
    x = fairnsquares(int(case[0]), int(case[1]))
    xs = "Case #%i: %i\n" % (casen, x)
    results.append(xs)
outputf.writelines(results)

