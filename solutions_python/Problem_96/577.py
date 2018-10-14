#!/usr/bin/env python

import sys

infile = open(sys.argv[1])
outfile = open(sys.argv[2], "w")

num_cases = int(infile.readline())
for i in xrange(num_cases):
    line = infile.readline().split()
    N = int(line[0])
    S = int(line[1])
    p = int(line[2])
    t = [int(l) for l in line[3:]]
    ok = 0 # number googlers whose best score is > p in any case
    ok_if_surprising = 0 # number of googlers whose best score is > p only if surprising
    for total in t:
        if total < 2:
            max_normal = total
            max_surprising = total
        elif total > 27:
            max_normal = 10
            max_surprising = 10
        elif (total % 3) == 2:
            max_normal = total/3 + 1
            max_surprising = max_normal + 1
        elif (total % 3) == 1:
            max_normal = total/3 + 1
            max_surprising = max_normal
        else:
            max_normal = total/3
            max_surprising = max_normal + 1

        if max_normal >= p:
            ok += 1
        elif max_surprising >= p:
            ok_if_surprising += 1

    result = ok
    if (ok_if_surprising > S):
        result += S
    else:
        result += ok_if_surprising

    outfile.write("Case #%d: %d\n"%(i+1, result))

outfile.close()

