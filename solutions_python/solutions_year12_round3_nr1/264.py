#!/bin/python
#import sys
#sys.stdin = file("sample.in")

def readint(): return int(raw_input())

def readints(): return [ int(x) for x in raw_input().split() ]

def lowest(cs):
    return set(cs.keys())-set(sum(cs.values(),[]))

def has_diamond(lc, ics, cs):
    if lc in ics:
        return True
    ics.add(lc)
    for cc in cs[lc]:
        if has_diamond(cc, ics, cs):
            return True
    return False

def solve(nc,cs):
    for lc in lowest(cs):
        ics = set()
        if has_diamond(lc, ics, cs):
            return "Yes"
    return "No"

if __name__ == "__main__":
    nt = readint()
    for i in range(nt):
        nc = readint()
        cs = dict([ (x,readints()[1:]) for x in range(1,nc+1) ])
        print "Case #%d: %s" % ( i+1, str(solve(nc,cs)))
