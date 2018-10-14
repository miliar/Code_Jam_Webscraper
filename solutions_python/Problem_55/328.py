#!/usr/bin/python

from __future__ import division

import sys

def prefixWithSum(n, xs):
    sum = 0
    for (ix, x) in enumerate(xs):
        sum += x
        if sum > n:
            return ix, sum - x
    return ix, sum

if __name__ == '__main__':
    caseCount = int(sys.stdin.readline())

    for caseIx in range(caseCount):
        R, k, N = [int(x) for x in sys.stdin.readline().split(' ')]
        g = tuple(int(x) for x in sys.stdin.readline().split(' '))

        seen = {}
        rideHistory = []
        money = 0
        rides = 0

        while rides < R:
            #print >> sys.stderr, g, money, rides, seen, rideHistory
            if seen is not None and g in seen:
                cycleStart = seen[g]
                cycleLength = rides - cycleStart
                dups = (R - cycleStart) // cycleLength
                moneyAtStart = rideHistory[cycleStart-1] if cycleStart else 0
                money = moneyAtStart + (money - moneyAtStart) * dups
                rides += cycleLength * (dups - 1)
                seen = None

                #print >> sys.stderr, cycleStart, cycleLength, dups, moneyAtStart, money, rides
            else:
                groupCount, rideSize = prefixWithSum(k, g)
                ride = g[:groupCount]
                money += rideSize
                
                if seen is not None:
                    seen[g] = rides
                rideHistory.append(money)

                rides += 1
                g = g[groupCount:] + ride
        
        print "Case #%d: %d" % (caseIx + 1, money)
