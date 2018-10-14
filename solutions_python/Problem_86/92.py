#!/bin/python
import sys
import re
debug=False
def rl(f):
    return f.readline().strip()
def debugop(s):
    global debug
    if debug:
        print str(s)
if len(sys.argv) > 2:
    if sys.argv[2] == "yes":
        debug=True
f=open(sys.argv[1])
tcs=int(rl(f))
for i in range(0,tcs):
    n,l,h=map(int,rl(f).split())
    others=map(int,rl(f).split())
    if l == 1:
        print "Case #%d: 1" % (i+1)
        continue
    divides=False
    for j in range(l,h+1):
        for o in others:
            if j % o == 0 or o % j == 0:
                divides=True
            else:
                divides=False
                break
        if divides:
            print "Case #%d: %d" % (i+1,j)
            break
    if not divides:
        print "Case #%d: NO" % (i+1)
