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

def magic(f):
    a = readint(f)
    m1 = readmatrix(f, 4)
    b = readint(f)
    m2 = readmatrix(f, 4)

    r1 = m1[a-1]
    r2 = m2[b-1]

    same = []
    for i in xrange(4):
        for j in xrange(4):
            if r1[i] == r2[j]:
                same += [r1[i]]
    if len(same) == 1:
        return same[0]
    elif len(same) == 0:
        return "Volunteer cheated!"
    elif len(same) > 1:
        return "Bad magician!"  
    else:
        return "*************************************"

if __name__ == "__main__":
    f = open(sys.argv[1], "r")
    numCases = readint(f)
    for i in xrange(numCases):
        print "Case #%d: %s" % (i + 1, magic(f))
