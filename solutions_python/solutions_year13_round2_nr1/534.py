#!/usr/bin/python

import sys

def readints(f):
    return [int(s) for s in f.readline().split()]

def readint(f):
    return int(f.readline())

def readmatrix(f, rows):
    matrix = []
    for i in xrange(rows):
        matrix += [readints(f)]
    return matrix

def doSomething(a, motes):
    if a == 1:
        return a, [], len(motes)
    x = a
    z = 0
    while x <= motes[0]:
        z += 1
        x += x - 1
    if z >= len(motes):
        return a, [], len(motes)
    else:
        return x, motes, z

def solve(a, motes):
    motes.sort()
    x = 0
    while len(motes) > 0:
        if motes[0] < a:
            a += motes[0]
            motes.pop(0)
        else:
            a, motes, z = doSomething(a, motes)
            x += z
    return x

if __name__ == "__main__":
    f = open(sys.argv[1], "r")
    numCases = readint(f)
    for i in xrange(numCases):
        a, n = readints(f)
        motes = readints(f)
        s = solve(a, motes)
        print "Case #%d: %d" % (i + 1, s)
