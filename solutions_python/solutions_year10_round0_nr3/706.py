#!/usr/bin/python2.6
#-*- coding: utf-8 -*-

import sys

COST = 1

if __name__ == '__main__':
    if not sys.argv[1:]:
        print "Usage: %s [input file]" % sys.argv[0]
        sys.exit(1)

    with open(sys.argv[1]) as f:
        cases = int(f.readline())

        # test each case
        for i in range(1, cases+1):
            # parse input
            values = f.readline()
            runs = int(values.split()[0])
            places = int(values.split()[1])
            groups = int(values.split()[2])
            queue = [int(x) for x in f.readline().split()]

            # count for the current case
            money = 0
            for j in range(1, runs+1):
                seats = 0
                cycle = 0 # allows to detect a cycle (all groups were involved in this run)
                while (seats + queue[0]) <= places and cycle < groups:
                    seats += queue[0]
                    money += queue[0] * COST
                    # move group to the end of the queue
                    queue = queue[1:] + [queue[0]]
                    cycle += 1

            # result
            print "Case #%s: %s" % (i, money)
