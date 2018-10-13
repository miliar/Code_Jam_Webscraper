#!/usr/bin/python2.5
import re
r = re.compile('[ :]')

def read_times(string):
    t = [int(x) for x in r.split(string)]
    return (t[0] * 60 + t[1], t[2] * 60 + t[3])

def solve(lst):
    lst.sort()
    avail = 0
    needed = 0
    for (_, type) in lst:
        if type == 0:
            avail = avail + 1
        elif type == 1:
            if (avail > 0):
                avail = avail - 1
            else:
                needed = needed + 1
    return needed

for case in range(input()):
    t = int(input())
    na, nb = raw_input().split()
    ta = []
    tb = []
    for k in range(int(na)):
        ta.append(read_times(raw_input()))
    for k in range(int(nb)):
        tb.append(read_times(raw_input()))
    a = [(dep, 1) for (dep, arr) in ta] + [(arr + t, 0) for (dep, arr) in tb]
    b = [(dep, 1) for (dep, arr) in tb] + [(arr + t, 0) for (dep, arr) in ta]

    print "Case #%s: %s %s" % ( (case + 1), solve(a), solve(b) )

