#!/usr/bin/python

import sys

def IsValidSplit(score, i, isSupr):
    result = False
    
    r = score - i
    
    if not isSupr:
        r1 = r - i 
        r2 = r - (i - 1)

        result = (r1 >= 0 and r1 == i) or \
                 (r1 >= 0 and r1 == (i - 1)) or \
                 (r2 >= 0 and r2 == (i - 1))
    else:
        r1 = r - i
        r2 = r - (i - 1)
        r3 = r - (i - 2)

        #print r1, r2, r3, (i - 2),
        result = (r1 >= 0 and r1 == (i - 2)) or \
                 (r2 >= 0 and r2 == (i - 2)) or \
                 (r3 >= 0 and r3 == (i - 2))
        #print (r1 == (i - 2)), (r2 == (i - 2)), (r3 == (i - 2))

    return result

def GetBest(haveMax, i, reg, supr):
    #print i, reg, supr

    if i >= len(haveMax):
        return 0
    
    r1 = 0
    if reg > 0:
        r1 += haveMax[i][0] + GetBest(haveMax, i + 1, reg - 1, supr)

    r2 = 0
    if supr > 0:
        r2 += haveMax[i][1] + GetBest(haveMax, i + 1, reg, supr - 1)
    
    return r1 if r1 > r2 else r2

def Process(n, line):
    raw = line.strip().split()
    N = int(raw[0])
    S = int(raw[1])
    p = int(raw[2])
    scores = [int(s) for s in raw[3:]]
    
    #print N, S, p, scores
    
    haveMax = []
    for score in scores:
        onReg = False
        onSupr = False
        #print score
        for i in xrange(10, p-1, -1):
            if onReg and onSupr: break

            onReg |= IsValidSplit(score, i, False)
            onSupr |= IsValidSplit(score, i, True)
            #print "\t", i, onReg, onSupr


        haveMax.append((onReg, onSupr))

    #print haveMax
    numMax = GetBest(haveMax, 0, N - S, S)

    print >>sys.stdout, "Case #%d: %d" % (n, numMax)
    

if __name__ == "__main__":

    n = 0
    for line in sys.stdin:
        if n > 0:
            Process(n, line.strip())
        n += 1
