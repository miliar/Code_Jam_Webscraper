#!/usr/bin/python

import sys

MINN = 1
MAXN = 10**7

def is_palin(n):
    return str(n) == str(n)[::-1]

fair_and_square_nums = []

for i in range(MINN, MAXN + 1):
    if i % ((MAXN - MINN + 1) / 100) == 0:
        sys.stderr.write("%d%% finished!\n" % (i / ((MAXN - MINN + 1) / 100), ))
    if is_palin(i) and is_palin(i * i):
        fair_and_square_nums.append(i * i)

sys.stderr.write("%s" % (fair_and_square_nums, ))

n = int(raw_input())
sys.stderr.write("%d\n" % (n, ))

for i in range(n):
    a, b = [int(x) for x in raw_input().split(" ")]

    sol = len([x for x in fair_and_square_nums if a <= x <= b])
    sys.stderr.write("%d %d: %d\n" % (a, b, sol))
    print("Case #%d: %d" % (i + 1, sol))
