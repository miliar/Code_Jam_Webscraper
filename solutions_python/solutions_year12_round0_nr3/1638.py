#!/usr/bin/env python

from math import log10

def solve(i):
    ans = 0
    a, b = map(int, raw_input().split())
    mem = []
    skip = []
    for x in xrange(a, b+1):
        if x in skip:
            continue
        
        count = 0
        
        d = int(log10(x))
        for y in xrange(1, d+1):
            base = 10**y
            z = (x % base) * 10**(d-y+1) + (x / base)
            if z != x and z > a and z <= b and (x, z) not in mem and (z, x) not in mem and int(log10(z)) == d:
                count += 1
                mem.append((x, z))
        
        ans += count
        
    print 'Case #%d: %d' % (i + 1, ans)

def main():
    n = int(raw_input())
    for i in xrange(n):
        solve(i)

if __name__ == '__main__':
    main()