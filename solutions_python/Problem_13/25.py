#!/usr/bin/python

import sys

nodes = []
c = []
M = 0
class fail: pass

def getMin(startNode, wantedValue):
#    print "Checking Node: " + `startNode`
    if startNode > (M-1)/2:
#        print "  is it: " + `wantedValue`

        if wantedValue == nodes[startNode]:
            return 0
        else:
            return 10000 + 1 

    if wantedValue :
        if nodes[startNode]:
            # Want a 1, and this is AND
            r = getMin(2 * startNode, 1) + getMin(2 * startNode + 1, 1)
        else:
            # This is OR
            r = min(getMin(2 * startNode, 1) ,getMin(2 * startNode + 1,1))
    else:
        if nodes[startNode]:
            r = min(getMin(2 * startNode, 0) , getMin(2 * startNode + 1,0))
        else:
            # THis is OR
            r = getMin(2 * startNode, 0) + getMin(2 * startNode + 1,0)
    if r == 0:
        return r

    if c[startNode]:
        if wantedValue:
            if not nodes[startNode]:
                # Want a 1, and this is AND
                r2 = getMin(2 * startNode, 1) + getMin(2 * startNode + 1,1)
            else:
                # This is OR
                r2 = min(getMin(2 * startNode, 1) ,getMin(2 * startNode + 1,1))
        else:
            if not nodes[startNode]:
                r2 = min(getMin(2 * startNode, 0) , getMin(2 * startNode + 1,0))
            else:
                # THis is OR
                r2 = getMin(2 * startNode, 0) + getMin(2 * startNode + 1,0)
#        print "r2  = " + `r2`
        if r2 + 1 < r:
            return r2 + 1
#    print "   Node" + `startNode` + ": " + `r`

    return r

if __name__ == "__main__":
    cases = int(sys.stdin.readline())
    for x in range(0,cases):
        nodes = [0]
        c = [0]
        M, V = map(int, sys.stdin.readline().split())
        for t in range(0, (M - 1)/2):
            l = map(int, sys.stdin.readline().split())
            nodes.append(l[0])
            c.append(l[1])
        for t in range((M+1)/2):
            l = int (sys.stdin.readline())
            nodes.append(l)
        #print nodes
        r = getMin(1, V)
        if r >= 10001:
            print "Case #%d: IMPOSSIBLE" % (x + 1)
        else:
            print "Case #%d: %d" % (x + 1, r)




