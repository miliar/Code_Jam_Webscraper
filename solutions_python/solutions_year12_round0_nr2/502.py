#! /usr/bin/python2.6
import itertools

tn = lambda n: n/3 + [0, 1, 1][n % 3]
sn = lambda n: n not in (0,1) and n/3 + [1, 1, 2][n % 3] or n

for tcase in range(1, input() + 1):
    nums = map(int, raw_input().split())
    n,s,p,t = nums[0],nums[1],nums[2],nums[3:]
    
    nmax,sst = len([a for a in t if tn(a) >= p]), [a for a in t if tn(a) < p]
    
    for a in sst:
        if sn(a) >= p and s > 0:
            s -= 1
            nmax += 1
    print 'Case #%d:' % tcase, nmax
