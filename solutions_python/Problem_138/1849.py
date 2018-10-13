#!/usr/bin/python2 -u
# -*- coding: utf-8 -*-
#
import sys, math

### ----- Variables
LINES = []

### ----- Functions
def pop_line():
    global LINES
    if len(LINES) == 0:
        return None
    line = LINES[0]
    LINES = LINES[1:]
    return line

### ----- Program Main
LINES = [line.rstrip() for line in sys.stdin]

T = int(pop_line())
for t in range(T):

    N = int(pop_line())

    BLOCKS1 = sorted(map(float, pop_line().split()))
    BLOCKS2 = sorted(map(float, pop_line().split()))

    # play game 'WAR'
    blocks1 = BLOCKS1[:]
    blocks2 = BLOCKS2[:]
    point = 0
    for i in range(N):

        matched = []
        for b1 in blocks1:

            pair = ()

            if b1 > max(blocks2):
                pair = (b1, min(blocks2))
            else:
                for b2 in blocks2:
                    if b2 >= b1:
                        pair = (b1, b2)
                        break

            matched.append(pair)

        matched = sorted(matched, key=lambda x: x[1], reverse=True)
        best = matched[0]
        if best[0] > best[1]:
            point += 1

        blocks1.remove(best[0])
        blocks2.remove(best[1])

    point1 = point

    # play game 'DECEITFUL-WAR'
    blocks1 = BLOCKS1[:]
    blocks2 = BLOCKS2[:]

    point = 0
    for i in range(N):

        matched = []
        for b1 in blocks1:

            pair = ()

            if b1 > max(blocks2):
                pair = (b1, min(blocks2))
            else:
                for b2 in blocks2:
                    if b2 >= b1:
                        pair = (b1, b2)
                        break

            # Can I deceive Ken?
            if pair[0] < pair[1] and pair[0] > min(blocks2):
                pair = (pair[0], min(blocks2))

            matched.append(pair)

        matched = sorted(matched, key=lambda x: x[0]-x[1], reverse=True)
        best = matched[0]

        if best[0] > best[1]:
            matched = filter(lambda x: x[0]>x[1], matched)
            matched = sorted(matched, key=lambda x: x[0])
            best = matched[0]
            point += 1

        else:
            matched = sorted(matched, key=lambda x: x[1], reverse=True)
            best = matched[0]

        blocks1.remove(best[0])
        blocks2.remove(best[1])

    point2 = point

    print 'Case #%d: %d %d' % (t+1, point2, point1)
