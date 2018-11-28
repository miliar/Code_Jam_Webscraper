#! /usr/bin/env python

import sys

def solve(n, s, p, totals):
    poss = 0
    for elem in totals:
#print "testing score %s, against requirement %s, %s surprises remain" % (elem, p, s)
        if 0 == elem % 3:
            if elem // 3 >= p:
                poss += 1
            else:
                if s > 0 and elem // 3 == p - 1 and elem > 0:
                    s -= 1 
                    poss += 1
        else:
            if elem // 3 >= p - 1:
                poss += 1
            else:
                if s > 0:
                    if ((elem // 3) * 3 == elem - 2) and ((elem // 3) + 2 >= p):
                        poss += 1
                        s -= 1
    return poss

with open(sys.argv[1],'r') as f:
    discard = True
    count = 1
    for line in f:
        if discard:
            discard = False
            continue


        #process
        linevals = line.rstrip().split()

        n = int(linevals[0])
        s = int(linevals[1])
        p = int(linevals[2])
        totals = [int(elem) for elem in linevals[3:]]
        result = solve(n, s, p, totals)
        print "Case #%s: %s" % (count, result)

        count += 1
