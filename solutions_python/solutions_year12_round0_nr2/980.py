#! /usr/bin/env python2.7
# -*- coding: utf-8 -*-
from itertools import combinations_with_replacement

def run(n):
    data = raw_input().split()

    num, s, best = int(data[0]), int(data[1]), int(data[2])
    scores = sorted([int(x) for x in data[3:]])

    count = 0
    for i in xrange(num):
        lower = scores[i] // 3

        #print "lower-1:", lower - 1
        for x, y, z in combinations_with_replacement(xrange(lower-1 if
            lower else 0, lower+3 if lower > 8 else 11), 3):
            if z - y > 2 or z - x > 2 or y - x > 2:
                continue

            if x + y + z == scores[i] and z >=  best:
                if z - y == 2 or z - x == 2 or y - x == 2:
                    #print "s:", s
                    if s:
                        #print 'deduce'
                        s = s - 1
                        #print s
                    else:
                        continue
                #print "numbers:", x, y, z
                #print
                count += 1
                break
                
    print "Case #%d: %d" % (n + 1, count)

n = int(raw_input())
[run(i) for i in xrange(n)]
