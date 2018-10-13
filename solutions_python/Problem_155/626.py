#!/usr/bin/python

import sys

nb = int(raw_input())

for case in xrange(1, nb+1):
    shy_max, temp = raw_input().split()
    shy_max = int(shy_max)
    shy_di = []
    for i in temp:
        shy_di.append(int(i))

#    print >> sys.stdout, shy_max
#    print >> sys.stdout, shy_di

    friends = 0
    total = 0
    for shyness, nb in enumerate(shy_di):
        if not nb:
            continue
        if total < shyness:
            delta = shyness - total
            total += delta
            friends += delta

        total += nb

    print "Case #%d: %d" % (case, friends)

