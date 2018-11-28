#!/usr/bin/env python

import sys


def remove_longest(turn, table) :
    size = len(table)
    path = [0]
    last = table[0]
    i = 1
    while i < size:
        if last[2] != table[i][2] \
           and last[1] <= (table[i][0] - turn) :
            path.append(i)
            last = table[i]
        i += 1
#    print path
    start = table[path[0]][2]
    path.reverse()
    [table.pop(i) for i in path]
    return table, start

def get_train_cnt(turn, table) :
    resultA = 0;
    resultB = 0;
    while len(table) > 0:
        table, start = remove_longest(turn, table)
        if start == 'A' :
            resultA += 1
        elif start == 'B' :
            resultB += 1
    return resultA, resultB

def to_minutes(hhmms) :
    def tmtm(hhmmhhmm):
        def tm(hhmm):
            hh, mm = hhmm.split(':')
            return int(hh)*60 + int(mm)
        return tuple(map(tm, hhmmhhmm.split()))
    return map(tmtm, hhmms)

def combine(A2B, B2A) :
    result = []
    result.extend([(x[0], x[1], 'A') for x in A2B])
    result.extend([(x[0], x[1], 'B') for x in B2A])
    result.sort()
    return result

cnt = int(sys.stdin.readline())
for i in xrange(cnt):
    turn = int(sys.stdin.readline())
    A, B = tuple([int(x) for x in sys.stdin.readline().split()])
    A2B = [sys.stdin.readline() for j in xrange(A)]
    B2A = [sys.stdin.readline() for j in xrange(B)]
    A2B = to_minutes(A2B)
    B2A = to_minutes(B2A)
    A2B.sort()
    B2A.sort()
    timetable = combine(A2B, B2A)
#    print timetable
    res = get_train_cnt(turn, timetable)
    print 'Case #%d: %d %d' % (i + 1, res[0], res[1])

