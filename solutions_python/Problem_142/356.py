#/!usr/bin/env python

import sys
import logging

input = open(sys.argv[1]).readlines()
T = int(input.pop(0).rstrip())

def simplify(string):
    last = ''
    new_string = ''
    count = []
    temp_count = None
    for ch in string:
        if ch != last:
            new_string += ch
            last = ch
            if temp_count:
                count.append(temp_count)
            temp_count = 1
        else:
            temp_count += 1
    count.append(temp_count)
    return new_string, count

def median(mylist):
    sorts = sorted(mylist)
    length = len(sorts)
    if not length % 2:
        return (sorts[length / 2] + sorts[length / 2 - 1]) / 2.0
    return sorts[length / 2]

for case in range(1, T+1):
    N = int(input.pop(0).rstrip())
    strings = [x.strip() for x in input[:N]]
    input = input[N:]

    ss = set()
    count = []
    for s in strings:
        ts, tcount = simplify(s)
        ss.add(ts)
        count.append(tcount)
    if len(ss) != 1:
        sys.stdout.write('Case #%s: Fegla Won\n' % case)
    else:
        move = 0
        for i in range(len(count[0])):
            tmpcounts = []
            for j in range(len(count)):
                tmpcounts.append(count[j][i])
            m = int(median(tmpcounts))
            for c in tmpcounts:
                move += abs(m-c)
        sys.stdout.write('Case #%s: %s\n' %(case, move))
