#!/usr/bin/python

import sys
from pprint import pprint

def solve(cakes, unit):
    count = 0
    while "-" in cakes:
        '''
        pre = cakes[0:unit]
        if "-" in pre and "+" in pre:
            return "IMPOSSIBLE"
        after = cakes[-unit:]
        print after
        if "-" in after and "+" in after:
            return "IMPOSSIBLE"
        '''
        pos = cakes.find("-")
        if len(cakes) < pos + unit:
            return "IMPOSSIBLE"
        cakes = flip(cakes, pos, pos + unit)
        #print cakes
        count += 1
    return count


def flip(cakes, start, end):
    after = cakes[0: start]
    for i in xrange(start, end):
        after += "+" if cakes[i] == "-" else "-"
    after += cakes[end:]
    return after

if __name__ == '__main__':

    case_N = int(sys.stdin.readline().strip())
    #pprint(case_N)
    for n in xrange(case_N):
        cakes, unit = sys.stdin.readline().strip().split(" ")
        ans = solve(cakes, int(unit))
        print 'Case #' + str(n+1) + ': ' + str(ans)
