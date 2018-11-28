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
    r,c=map(int,rl(f).split())
    tiles=[]
    for j in range(0,r):
        row=rl(f)
        tiles.append([])
        for k in range(0,c):
            tiles[j].append(row[k])
    debugop(tiles)
    print "Case #%d:" % (i+1)
    breaker=False
    for j in range(0,r-1):
        for k in range(0,c-1):
            if tiles[j][k] == "#":
                if tiles[j][k+1] == "#" and tiles[j+1][k] == "#" and tiles[j+1][k+1] == "#":
                    tiles[j][k] = "/"
                    tiles[j][k+1] = "\\"
                    tiles[j+1][k] = "\\"
                    tiles[j+1][k+1] = "/"
                else:
                    print "Impossible"
                    breaker=True
                    break
        if breaker:
            break
    if breaker:
        continue
    else:
        strt=""
        for j in range(0,r):
            strt= strt+"".join(tiles[j])+"\n"
        strt=strt[:-1]
        if strt.find("#") != -1:
            print "Impossible"
        else:
            print strt
                  

