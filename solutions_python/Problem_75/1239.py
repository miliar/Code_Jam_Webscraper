#!/usr/bin/env python
# -*- coding: utf-8 -*-

def inNonBase(nonbase, ela, elb):

    if nonbase.get(ela + elb, None):
        return nonbase[ela + elb]

    if nonbase.get(elb + ela, None):
        return nonbase[elb + ela]

    return False

cases = int(raw_input())

for case in xrange(cases):
    raw = raw_input().split()

    nonbase = {}
    oppose = {}
    series = []

    nbnum = int(raw[0])
    raw = raw[1:]
    for x in xrange(nbnum):
        nonbase[raw[x][:-1]] = raw[x][-1]
        raw = raw[1:]

    oppnum = int(raw[0])
    raw = raw[1:]
    for x in xrange(oppnum):
        oppose[raw[x][0]] = raw[x][1]
        oppose[raw[x][1]] = raw[x][0]
        raw = raw[1:]

    sernum = raw[0]
    raw = raw[1:]
    series = list(raw[0])

    hand = [series[0]]
    series = series[1:]

    for el in series:
        if not len(hand):
            hand.append(el)
            continue

        nonb = inNonBase(nonbase, hand[-1], el)
        if nonb:
            hand.pop()
            hand.append(nonb)
            continue
        else:
            hand.append(el)

        op = oppose.get(el, None)
        if op:
            if op in hand:
                hand = []

    print "Case #{0}: [{1}]".format(case + 1, ", ".join(hand))


