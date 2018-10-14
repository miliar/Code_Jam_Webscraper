#!/usr/bin/env python3
# vim:set ts=8 sw=4 et smarttab:
# Qualification Round 2012

import sys

line = sys.stdin.readline()
fields = line.split()
assert len(fields) == 1
ntc = int(fields[0])

for tc in range(1, ntc + 1):
    line = sys.stdin.readline()
    fields = line.split()
    n = int(fields[0])
    assert len(fields) == 3 + n
    s = int(fields[1])
    p = int(fields[2])
    without_surprising = 0
    with_surprising = 0
    for i in range(n):
        point = int(fields[3 + i])
        low = point // 3
        if point % 3 == 0:
            high = low
        else:
            high = low + 1
        if high >= p:
            without_surprising += 1
        elif point % 3 != 1 and high == p - 1 and high > 0 and high < 10:
            with_surprising += 1
    answer = without_surprising + min(with_surprising, s)
    print('Case #{0}: {1}'.format(tc, answer))
