#! /usr/bin/python

import sys

def getline():
    return sys.stdin.readline().strip()

def solve(num):
    rides, seats, groupCount = (int(x) for x in getline().split())
    groupSizes = [int(x) for x in getline().split()]

    cache = [False] * groupCount
    for startPos in range(groupCount):
        groups, euros = 0, 0
        cache[startPos] = (euros, groups)
        for offset in range(groupCount):
            groups += 1
            euros += groupSizes[(startPos + offset) % groupCount]
            if euros > seats:
                break
            cache[startPos] = (euros, groups)

    pos, euros = 0, 0
    for ride in range(rides):
        entry = cache[pos]
        euros += entry[0]
        pos = (pos + entry[1]) % groupCount

    print 'Case #%d: %d' % (num, euros)

t = int(getline())
for x in xrange(t):
    solve(x + 1)
