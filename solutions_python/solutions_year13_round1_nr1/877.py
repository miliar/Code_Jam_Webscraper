#!/usr/bin/env python

import sys
from math import sqrt, floor

def solve(r, t):
    a = 2.0
    b = (2.0*r-1)
    c = -t
    N = int(floor((-b + sqrt(b**2 - 4*a*c))/(2*a)))
    N = max(1, N-2)
    return solve2(r,t,N)

def solve2(r, t, start):
    N = start 
    while 1:
        if volume(r, N+1) > t:
            return N
        N += 1

def volume(r, N):
    return (2*r-1)*N + 2*N**2

def main():
    f = open(sys.argv[1])
    def rl():
        return [int(x) for x in f.readline().strip().split(' ')]
    N, = rl()
    for ii in range(N):
        r, t = rl()
        print 'Case #{}: {}'.format(ii+1, solve(r,t))

if __name__ == '__main__':
    main()
