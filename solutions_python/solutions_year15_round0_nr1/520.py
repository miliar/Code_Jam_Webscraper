#!/usr/bin/env python

import sys, os

# the first line is the total number of cases
cases_total = int(sys.stdin.readline().strip())

case = 0                                # id of the case
for line in sys.stdin:                  # loop over each line of the cases
    case += 1                           # iterate case id
    if (case > cases_total):            # just in case something goes wrong (unlikely)
        raise Exception("Exceeded the total number of test cases.")

    [s_max, s] = line.strip().split()
    s_max = int(s_max)
    s = [ int(x) for x in list(s) ]

    n_invited = 0
    n_up = 0
    s_cur = 0
    while s_cur <= s_max:
        if n_up < s_cur:
            n_invited += (s_cur - n_up)
            n_up = s_cur
        n_up += s[s_cur]
        s_cur += 1

    out = str(n_invited)

    print "Case #"+str(case)+": "+out   # the output format is 'Case #${case}: ${output}'
