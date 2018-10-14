#!/usr/bin/env python
import sys
import os
import itertools
def add_list(x):
    res = x[0]
    for i in range(1, len(x)):
        res = res ^ x[i]
    return res
with open(sys.argv[1], "r") as input:
    data = input.readlines()
with open("%s.result" % sys.argv[1], "w") as output:
    n = int(data[0])
    for i in range(n):
        string = map(lambda x: int(x), data[i*2+2][:-1].split())
        maxr = -1
        for j in range(1, len(string)):
            maxn = -1
            lt = list(itertools.combinations(string, j))
            for v in lt:
                r = string[:]
                l = []
                for vl in v:
                    l.append(vl)
                    r.remove(vl)
                if add_list(l) == add_list(r):
                    maxn = max(maxn, sum(l), sum(r))
            maxr = max(maxn, maxr)
        print maxr
        if maxr == -1:
            print>> output,  "Case #%d: NO" % (i + 1)
            print "Case #%d: NO" % (i + 1)
        else:
            print>> output,  "Case #%d: %s" % (i + 1, maxr)
            print "Case #%d: %s" % (i + 1, maxr)
