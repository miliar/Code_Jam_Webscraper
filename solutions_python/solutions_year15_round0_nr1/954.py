#!/usr/bin/python

import sys

def emit(text, *args):
    msg = text % args
    sys.stderr.write(msg)
    sys.stdout.write(msg)

def getline():
    return sys.stdin.readline().rstrip('\n')

def solve(ss):
    needed = 0
    standing = 0
    for i in range(len(ss)):
        if standing < i:
            needed = needed + (i - standing)
            standing = i
        standing = standing + ss[i]
    return needed

ncases = int(getline())

for casenr in range(1, ncases+1):
    smax, s = getline().split()
    s = [ int(c) for c in s ]
    emit("Case #%d: %s\n", casenr, solve(s))
