#!python
import sys

def readint(): return int(raw_input())
def readints(): return [ int(x) for x in raw_input().split() ]
def readline(): return raw_input()
def skipline(): return raw_input()

def search(tbl, sx, sy, dx, dy):
    return set([tbl[sy+dy*i][sx+dx*i] for i in range(4)])

def solve(tbl):
    lines = ([ search(tbl, 0,y,1,0) for y in range(4) ] +
             [ search(tbl, x,0,0,1) for x in range(4) ] +
             [ search(tbl, 0,0,1,1) ] +
             [ search(tbl, 0,3,1,-1) ])
    if set("X") in lines:
        return "X won"
    elif set("O") in lines:
        return "O won"
    elif set("XT") in lines:
        return "X won"
    elif set("OT") in lines:
        return "O won"
    elif "." not in "".join(tbl):
        return "Draw"
    return "Game has not completed"

if __name__ == "__main__":
    nt = readint()
    for i in range(nt):
        tbl = [readline() for _ in range(4)]
        skipline()
        
        print "Case #%d: %s" % ( i+1, str(solve(tbl)))
