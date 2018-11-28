#!python
import sys

def readint(): return int(raw_input())
def readints(): return [ int(x) for x in raw_input().split() ]
def readline(): return raw_input()
def skipline(): return raw_input()

def search(tbl, sx, sy, dx, dy, length):
    return [tbl[sy+dy*i][sx+dx*i] for i in range(length)]

def solve(w, d, tbl):
    xmax = [max(search(tbl, 0, z, 1, 0, w)) for z in range(d)]
    zmax = [max(search(tbl, x, 0, 0, 1, d)) for x in range(w)]
    for x in range(w):
        for z in range(d):
            h = tbl[z][x]
            if not(h >= xmax[z] or h >= zmax[x]):
                return "NO"
    return "YES"

if __name__ == "__main__":
    nt = readint()
    for i in range(nt):
        d, w = tuple(readints())
        tbl = [readints() for _ in range(d)]
        
        print "Case #%d: %s" % ( i+1, str(solve(w,d,tbl)))
