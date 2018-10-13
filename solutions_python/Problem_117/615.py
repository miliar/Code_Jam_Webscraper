#!/usr/bin/python

import sys

def emit(text, *args):
    msg = text % args
    sys.stderr.write(msg)
    sys.stdout.write(msg)

def getline():
    return sys.stdin.readline().rstrip('\n')

def solve(arr, n, m):
    rowmax = [ max(arr[i]) for i in range(n) ]
    colmax = [ max([arr[i][j] for i in range(n)])
               for j in range(m) ]
    for i in range(n):
        for j in range(m):
            if arr[i][j] < rowmax[i] and arr[i][j] < colmax[j]:
                return "NO"
    return "YES"

ncases = int(getline())

for casenr in range(1, ncases+1):
    n, m = [ int(s) for s in getline().split() ]
    arr = []
    for i in range(n):
        arr.append([ int(s) for s in getline().split() ])
    emit("Case #%d: %s\n", casenr, solve(arr, n, m))
