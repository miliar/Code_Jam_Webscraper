#!/usr/bin/env python

import os, sys

def solve (line):
    A = int(line.split()[0])
    B = int(line.split()[1])
    P = line.split()[2:]
    P = [float(x) for x in P]

    plist = []
    elist = []
    solved = set()
    for x in range(pow(2, A))[1:]:
        rep = list( ((A - len(bin(x)[2:])) * "0") +  bin(x)[2:])
        rep = [float(x) for x in rep]

        if not str(rep) in solved:
            solved.add(str(rep))
            prob = 1
            for y in range(A):
                if rep[y] == 1:
                    prob *= 1 - P[y]
                else:
                    prob *= P[y]
            plist.append(prob)
            elist.append(rep)

        reprev = rep[:]
        reprev.reverse()
        if rep != reprev and not str(reprev) in solved:
            solved.add(str(reprev))
            prob = 1
            for y in range(A):
                if reprev[y] == 1:
                    prob *= 1 - P[y]
                else:
                    prob *= P[y]
            plist.append(prob)
            elist.append(reprev)

    # keep typing
    prob = reduce(lambda x,y:float(x)*float(y), P)
    p1 = (B-A+1) * prob

    rlist = []
    for prob in plist:
        keys = ((B-A)+B+2)
        rlist.append(keys * prob)

    p1 = (sum(rlist) + p1)

    # bkspc
    pxlist = []
    for x in range(1, A+1):
        prob = reduce(lambda x,y:float(x)*float(y), P)
        px = ((x*2)+B-A+1) * prob

        rlist = []
        for e in range(len(plist)):
            prob = plist[e]
            if not 1 in elist[e][:(A-x)]:
                keys = ((x*2)+B-A+1)
            else:
                keys = ((x*2)+B-A+1+B+1)
            rlist.append(keys * prob)
                

        px = (sum(rlist) + px)
        pxlist.append(px)

    px = min(pxlist)

    # enter right away
    prob = reduce(lambda x,y:float(x)*float(y), P)
    p2 = (B+2) * prob

    rlist = []
    for prob in plist:
        keys = (B+2)
        rlist.append(keys * prob)

    p2 = (sum(rlist) + p2)

    return str(min(p1, p2, px))


fd = sys.stdin

line = fd.readline()
sets = int(line)+1

for case in range(1, sets):
    line = fd.readline().strip()
    line += " " + fd.readline().strip()
    nline = solve(line)
    print "Case #%s: %s" % (case, nline)

fd.close()
