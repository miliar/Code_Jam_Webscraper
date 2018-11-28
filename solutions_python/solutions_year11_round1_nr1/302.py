#!/usr/bin/python
import sys
from math import floor

def solve(N, PD, PG):
    possibilitiesForD = []
    for D in range(1,N+1):
        if (D * PD) % 100 == 0:
            possibilitiesForD.append(D)
    if len(possibilitiesForD) == 0:
        return False
    if 0 < PG and PG < 100:
        return True
    if PG == PD:
        return True
    return False


if __name__ == "__main__":
    number = input()
    i = 0
    out = []
    while i < number:
        data = raw_input().split(' ')
        out.append(solve(int(data[0]), int(data[1]), int(data[2])))
        i += 1
    for i, item in enumerate(out):
        if item:
             print "Case #%i: Possible" % (i+1)
        else:
             print "Case #%i: Broken" % (i+1)
