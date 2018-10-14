from __future__ import division
import sys, string

def readlist():
	return [float(x) for x in sys.stdin.readline().strip().split(" ")]

def readint():
	return int(sys.stdin.readline())

def sim(C,F,X):
    #~ print C,F,X
    t = 0
    r = 2

    tbest = 1e10
    
    while 1:
        tfarm = t + C/r
        twin = t + X/r
        #~ print t, tfarm, twin
        tbest = min(tbest, twin)
        if tfarm > tbest:
            break
        t = tfarm
        r += F
    return tbest
    

T = readint()

for t in range(T):
    C,F,X = readlist()
    print "Case #%d: %s" % (t+1, sim(C,F,X))
