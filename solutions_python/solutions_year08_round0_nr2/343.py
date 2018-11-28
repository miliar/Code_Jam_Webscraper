#!/usr/bin/env python2.5
# encoding: utf-8
import sys
from collections import defaultdict
from operator import *

def time(s):
    """
    >>> time("01:01")
    61
    """
    return int(s[:2])*60 + int(s[3:])
    
def trainsNeeded(turnaround, AB, BA):
    """ 
    >>> trainsNeeded(5, ['09:00 12:00', '10:00 13:00', '11:00 12:30'], ['12:02 15:00', '09:00 10:30'])
    (2, 2)
    >>> trainsNeeded(2, ['09:00 09:01', '12:00 12:02'], [])
    (2, 0)
    """
    times = defaultdict(list)
    for a,b in (ts.split(" ") for ts in AB):
        times[time(a)].append((-1, 0))
        times[time(b)+turnaround].append((0, 1))
    for b,a in (ts.split(" ") for ts in BA):
        times[time(b)].append((0, -1))
        times[time(a)+turnaround].append((1, 0))
    mina, minb = 0, 0
    ta, tb = 0, 0
    for t, moves in sorted(times.items()):
        for (a,b) in moves:
            ta += a
            tb += b
        mina = min(mina, ta)
        minb = min(minb, tb)
    return -mina, -minb

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    inp = open(sys.argv[1])
    num_cases = int(inp.readline())
    out = open(sys.argv[1].replace(".in", ".out"), "w")
    for case in range(1,num_cases+1):
        turnaround = int(inp.readline())
        nAB, nBA = map(int, inp.readline().split())
        AB = [inp.readline().strip() for i in range(nAB)]
        BA = [inp.readline().strip() for i in range(nBA)]
        a, b= trainsNeeded(turnaround, AB, BA)
        result = "Case #%d: %d %d" % (case, a, b)
        out.write(result + "\n")

