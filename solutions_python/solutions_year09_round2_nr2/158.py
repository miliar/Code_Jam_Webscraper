from __future__ import with_statement
import sys

with open(sys.argv[1]) as f:
    num_cases = int(f.readline())

    for c in xrange(1, num_cases+1):
        D = dict(( (i, 0) for i in xrange(1,10) ))
        N = f.readline().strip()
        d = [int(i) for i in N]
        for i in xrange(1,10):
            D[i] = d.count(i)
        digits = sorted([0] + D.keys())
        d = [0] + d

        while True:
            j = len(d) - 1
            while d[j] == digits[-1]:
                d[j], j = 0, j-1
            d[j] = digits[digits.index(d[j])+1]

            for i in D.iterkeys():
                if d.count(i) != D[i]:
                    break # need the next tuple
            else:
                break # solution

        if d[0] == 0:
            del d[0]
        N = ''.join(map(str, d))
        print "Case #%d: %s" % (c, N)
