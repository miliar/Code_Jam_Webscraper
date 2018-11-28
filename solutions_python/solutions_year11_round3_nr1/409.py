#!/usr/bin/python

import sys

def readints(f):
    return [int(s) for s in f.readline().split()]

def readint(f):
    return int(f.readline())

def readRow(line):
    return map(lambda x : x == '#', line)

def invalid(m, i, j):
    if m[i][j] is None or not m[i][j]:
        return False
    if m[i][j] and (i == len(m)-1 or j == len(m[0])-1):
        return True
    if m[i][j] and (m[i+1] is None or m[i][j+1] is None or m[i+1][j+1] is None):
        return True
    a = m[i][j]
    b = m[i+1][j] and m[i][j+1] and m[i+1][j+1]
    return a and not b

def compute(m):
    grid = [['.' for c in r] for r in m]
    for i in xrange(len(m)):
        for j in xrange(len(m[i])):
            if not invalid(m, i, j) and m[i][j]:
                m[i][j] = None
                grid[i][j] = '/'
                m[i+1][j] = None
                grid[i+1][j] = '\\'
                m[i][j+1] = None
                grid[i][j+1] = '\\'
                m[i+1][j+1] = None
                grid[i+1][j+1] = '/'
            elif invalid(m,i,j):
                print "Impossible"
                return
    printGrid(grid)

def printGrid(grid):
    for i in xrange(len(grid)):
        print "".join(grid[i])
  
if __name__ == "__main__":
    f = open(sys.argv[1], "r")
    numCases = readint(f)
    for i in xrange(numCases):
        r, c = readints(f)
        m = []
        for j in xrange(r):
            s = f.readline().strip()
            m += [readRow(s)]
        print "Case #%d:" % (i + 1)
        compute(m)
