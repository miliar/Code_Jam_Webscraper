import sys
import os

def getnum():
    return [int(x) for x in sys.stdin.readline().split()]

C, = getnum()

for i in range(1, C+1):
    sol = 0
    N, = getnum()
    wires = []
    for j in range(N):
        wires.append(getnum())
#    print wires
    def wirecmp(x,y):
        if x[0] < y[0]:
            return -1
        elif x[0] == y[0]:
            return 0
        else:
            return 1
    wires.sort(wirecmp)
    for x in range(N):
        for y in range(x+1, N):
#            print x,y
            w1 = wires[x]
            w2 = wires[y]
            assert w1[0] < w2[0]
            if w1[1] > w2[1]:
                sol+=1
    print "Case #%d: %d" % (i, sol)
#    break
