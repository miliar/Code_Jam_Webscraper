#!/usr/bin/python

import sys

data = open(sys.argv[1]).read().splitlines()

out = open(sys.argv[1] + ".out", 'w')
data.pop(0)
case = 1
for line in data:
    S, K = line.split()
    S = list(S)
    #print S
    count = 0
    for i in xrange(len(S) - int(K) + 1):
        b = S[i:int(K) + i]
        if b[0] == "-":
            count += 1
            for j in xrange(int(K)):
                if S[i + j] == "-":
                    S[i + j] = "+"
                else:
                    S[i + j] = "-"
    if "-" in S:
        count = "IMPOSSIBLE"
    outstr = "Case #%d: %s" % (case, str(count))
    print outstr
    out.write(outstr + "\n")
    case += 1
