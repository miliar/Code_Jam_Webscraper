#!/usr/bin/env python
import sys
from time import time

def recycled(minimum, maximum, r):
    pairs = set()
    for n in range(minimum, maximum + 1):
        for m in r[str(n)]:
            m = int(m)
            if n < m and m >= minimum and m <= maximum:
                pairs.add((n, m))

    return len(pairs)

def main():
    r = {}
    m = 2000000
    for n in range(1, m + 1):
        if str(n) in r: continue
        digits = str(n)
        perms = set()
        for i in range(len(digits)):
            x = digits[i:] + digits[:i]
            if not x.startswith('0'):
                perms.add(x)
        for p in perms:
            r[p] = perms

    for i, line in enumerate(sys.stdin):
        start = time()
        (minimum, maximum) = [int(d) for d in line.strip().split()]
        result = recycled(minimum, maximum, r)
        elapsed = time() - start
        print "Case #{0}:".format(i + 1), result

if __name__ == "__main__": main()
