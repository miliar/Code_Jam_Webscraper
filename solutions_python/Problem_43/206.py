#!/usr/bin/env python

import sys

T = int(sys.stdin.readline().strip())

for case in range(1, T+1):
    data = list(sys.stdin.readline().strip())
    mapping = {}
    ans = []
    swapped = False
    if len(data) == 1:
        swapped = False

    elif len(data) > 1:
        for ind in xrange(1, len(data)):
            if data[ind] != data[0]:
                data[ind], data[0] = data[0], data[ind]
                swapped = True
                break

    if swapped == False:
        num = 1
        for x in data:
            if x not in mapping:
                mapping[x] = num
                num += 1
    elif swapped == True:
        num = 0
        for x in data:
            if x not in mapping:
                mapping[x] = num
                num += 1

        data[ind], data[0] = data[0], data[ind]

    for value in data:
        ans.append(mapping[value])

    base = max(ans)+1

    ans.reverse()

    sol = 0
    pos = 0
    for value in ans:
        sol += value * base ** pos
        pos += 1


    print 'Case #%s: %s' % (case, sol)
