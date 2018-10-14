#!/usr/bin/env python
import sys

cases = None
case = 0
with open(sys.argv[1] if sys.argv[1:] else '/dev/stdin') as iostream:
    for line in iostream:
        line = line.strip()
        if not line:
            continue

        if not cases and line.isdigit():
            cases = int(line)
            continue

        case += 1
        a, b = line.split()
        a, b = int(a), int(b)
        k = 0
        for i in range(a, b + 1):
            if str(i)[::-1] == str(i) and str(int(i**.5)) == str(int(i**.5))[::-1] and int(i**.5) == i ** .5:
                k += 1
        print('Case #%i: %i' % (case, k))
