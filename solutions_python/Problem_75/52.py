#!/usr/bin/python

from collections import defaultdict

def solve(rawCombining, rawOpposing, elementList):
    #print rawCombining, rawOpposing, elementList

    combining = {}
    for a, b, c in rawCombining:
        combining[a, b] = c
        combining[b, a] = c
    #print combining

    opposing = defaultdict(list)
    for a, b in rawOpposing:
        opposing[a].append(b)
        opposing[b].append(a)
    #print opposing

    constructedElements = []
    for el in elementList:
        constructedElements.append(el)

        try:
            constructedElements[-2:] = combining[tuple(constructedElements[-2:])]
        except KeyError:
            pass
        for op in opposing[constructedElements[-1]]:
            if op in constructedElements[:-1]:
                constructedElements = []

    return '[' + ', '.join(constructedElements) + ']'

T = int(raw_input())
for i in range(T):
    line = raw_input().split(' ')
    cEnd = int(line[0]) + 1
    print "Case #%i: %s" % (i+1, solve(line[1:cEnd], line[cEnd + 1:-2], line[-1]))

