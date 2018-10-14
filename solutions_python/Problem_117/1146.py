#!/usr/bin/env python

T = long(raw_input())            #number of real tests
for t in range(1,T+1):
    A = []
    rrr,ccc=raw_input().split()
    rrr = long(rrr)
    ccc = long(ccc)
    for i in range(rrr):
        x = raw_input().split()
        A.append([long(q) for q in x])

    itsOK = True
    for r in range(rrr):
        for c in range(ccc):
            tar = A[r][c]
            rowgood = True #assume all is good
            colgood = True
            for x in range(rrr):
                if A[x][c] > tar:
                    colgood = False
                    break
            for x in range(ccc):
                if A[r][x] > tar:
                    rowgood = False
                    break
            if not (rowgood or colgood):
                itsOK = False
                break
        if not itsOK:
            break
    if itsOK:
        print "Case #%i: %s"%(t,"YES")
    else:
        print "Case #%i: %s"%(t,"NO")