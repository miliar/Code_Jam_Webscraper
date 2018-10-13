#!/usr/bin/env python3

from sys import stdin


limit = 10**7 - 1
table = [i for i in range(limit + 1)]

prev_table = []
while prev_table != table:
    prev_table = list(table)
    for i in range(1, limit):
        table[i + 1] = min(table[i] + 1, table[i + 1])
        rev_i = int(str(i)[::-1])
        table[rev_i] = min(table[i] + 1, table[rev_i])


T = int(stdin.readline())
tests = [int(stdin.readline()) for i in range(T)]

for i, n in enumerate(tests):
    print("Case #%d: %d" % (i + 1, table[n]))
