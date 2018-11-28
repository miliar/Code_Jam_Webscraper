import sys
import re
from pprint import pprint

input = sys.stdin
T=int(input.readline())

    
for i in xrange(1,T+1):
    vals = []
    N=int(input.readline())
    for j in xrange(N):
        vals.append ( map(int, input.readline().split()))
    coords = set()
    for x1,y1,x2,y2 in vals:
        for k in xrange(x1, x2+1):
            for l in xrange(y1, y2+1):
                coords.add((k,l))
    c=0
    while len(coords) >0:
        next = set()
        for x, y in coords:
            if not(((x-1,y) not in coords) and ((x, y-1) not in coords)):
                next.add((x,y))
        for x, y in coords:
            if ((x, y+1) not in coords) and ((x-1,y+1) in coords):
                next.add((x,y+1))
        coords = next
        c+=1
    print "Case #%s: %s" % (i, c)

