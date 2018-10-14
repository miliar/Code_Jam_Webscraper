#/usr/bin/env python

import sys, os
from math import ceil

# the first line is the total number of cases
cases_total = int(sys.stdin.readline().strip())

case = 0                                # id of the case
while case < cases_total:
    case += 1                           # iterate case id
    D = int(sys.stdin.readline().strip())
    Pi = [ int(x) for x in sys.stdin.readline().strip().split() ]

    # the longest time will be the largest Pi
    t_max = max(Pi)

    # Let e be an optimal number of eating steps, and s be an optimal number of special steps
    # we know that 1<=e<t_max, and we can calculate s as a function of e
    s_list = {t_max:t_max}
    t_list = {t_max:t_max}
    for e in range(1,t_max):
        # to make sure diners have at most e pancakes
        # we need to make ceil(Pi/e-1) moves
        s = 0
        for i in Pi:
            s_i = i/e - 1
            if ( i % e != 0 ):
                s_i += 1
            s += s_i
        s_list[e] = s
        t_list[e] = s + e

    out = str(min(t_list.values()))

    print "Case #"+str(case)+": "+out   # the output format is 'Case #${case}: ${output}'
