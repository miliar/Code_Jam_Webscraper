#!/usr/bin/python

"""
Airport Walkways problem solution
(GCJ 2011, Round 1B)
Author: madrezaan
"""

import sys, math, time

# open input file
if len(sys.argv) == 2 and sys.argv[1] != '--help':
    in_file = open(sys.argv[1])
else:
    print "Usage: airport_walkways.py <input file>"
    sys.exit(0)

# get number of cases
T = int(in_file.readline())

# begin prosessing cases
for cur_case in range(T):
    # get constants
    X, S, R, t, N = map(int, in_file.readline().split(" "))
    walkways = []
    for i in range(N):
        B, E, w = map(int, in_file.readline().split(" "))
        walkways.append((w, B, E))
    walkways.sort()
    walkways.reverse()
    # begin calculation
    intervals = []
    def calc_time(b, e):
        new_b = b
        new_e = e
        new_w = S
        for w, B, E in walkways:
            if B <= e and B >= b or E <= e and E >= b:
                if B > b:
                    new_b = B
                if E < e:
                    new_e = E
                if new_b == new_e:
                    new_b = b
                    new_e = e
                else:
                    new_w = S + w
                    break
        intervals.append((new_w, float(new_e - new_b) / new_w, float(new_e - new_b)))
        if new_b > b:
            calc_time(b, new_b)
        if new_e < e:
            calc_time(new_e, e)
        return
    calc_time(0, X)
    intervals.sort()
    #intervals.reverse()
    total_time = 0
    for new_w, _, l in intervals:
        new_t = l / (new_w - S + R)
        if new_t <= t:
            t -= new_t
        else:
            new_t = t + (l - t * (new_w - S + R)) / new_w
            t = 0
        total_time += new_t

    # output results
    print "Case #%d: %s" % (cur_case + 1, total_time)
        
# close input file
in_file.close()

    
        
