#!/usr/bin/env python
import sys

def max_p_attainable(total):
    quot, mod = divmod(total, 3)
    if mod == 0:
        return quot
    else:
        return quot + 1

def max_surprising_attainable(total):
    if total == 0: return 0
    quot, mod = divmod(total, 3)
    if mod == 2:
        return quot + 2
    else:
        return quot + 1

lines = [line.strip() for line in sys.stdin.readlines()]
num_cases = int(lines[0])
for i, line in enumerate(lines[1:]):
    result = 0
    parts = [int(p.strip()) for p in line.split()]
    N, S, p = parts[0:3]
    totals = parts[3:]
    for tot in totals:
        max_p = max_p_attainable(tot)
        if max_p >= p:
            result += 1
        elif max_surprising_attainable(tot) >= p and S > 0:
            result += 1
            S -= 1
    sys.stdout.write("Case #%s: %s\n" %( i+1, int(result)))
