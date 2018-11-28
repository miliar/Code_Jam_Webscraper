#!/usr/bin/env python3
# vim:set ts=8 sw=4 et smarttab:
# Qualification Round 2011

import sys

line = sys.stdin.readline()
fields = line.split()
assert len(fields) == 1
ntc = int(fields[0])

for tc in range(1, ntc + 1):
    line = sys.stdin.readline()
    fields = line.split()
    assert len(fields) == 1
    n = int(fields[0])
    line = sys.stdin.readline()
    fields = line.split()
    assert len(fields) == n
    a = int(fields[0])
    min_candy = a
    sum_candy = a
    xor_candy = a
    for i in range(1, n):
        a = int(fields[i])
        min_candy = min(min_candy, a)
        sum_candy += a
        xor_candy ^= a
    print('Case #{0}: {1}'.format(tc, 'NO' if xor_candy != 0 else sum_candy - min_candy))
