""" 
Code Jam 2013
Problem: Bullseye
Usages: 
  $ python script < input > output
  PS > gc input | python script | sc output.
"""

import sys, math
from math import floor

def calc(r, t):
    a, b, c = 2, 2*r-1, -t
    d = (b**2-4*a*c)**0.5
    r1 = (-b + d) / (2*a)
    return int(floor(r1))

if __name__ == '__main__':
    numcases = int(sys.stdin.readline().strip())
    for i in range(1, numcases+1):
        r, t = map(int, sys.stdin.readline().strip().split())
        result = calc(r, t)
        print "Case #%d: %s" % (i, result)
