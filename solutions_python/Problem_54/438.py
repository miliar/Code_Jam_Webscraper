#!/usr/bin/env python

from fractions import gcd

def solve(case):
    ans = 0
    line = raw_input().split()
    N = int(line[0])
    line = map(lambda x: int(x), line[1:])
    diff = []

    for i in xrange(N):
        for j in xrange(i+1, N):
            diff.append(abs(line[i] - line[j]))

    dl = len(diff)
    if dl == 1:
        gd = diff[0]
    else:
        gd = gcd(diff[0], diff[1])
        for d in diff[2:]:
            gd = gcd(gd, d)

    ans = line[0] / gd
    if line[0] % gd != 0:
        ans = ans + 1
    #ans = ceil(line[0] / float(gd)) * gd - line[0]
    ans = ans * gd - line[0]
    
    print 'Case #%d: %ld' % (case + 1, ans)

def main():
    cases = int(raw_input())
    for case in xrange(cases):
        solve(case)
    
if __name__ == '__main__':
    main()