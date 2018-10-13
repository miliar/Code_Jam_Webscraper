#!/usr/bin/env python

import sys

def solve(n, k):
    wrap = 2 ** n
    snaps_that_matter = k % wrap
    return snaps_that_matter == wrap - 1

def main():
    lines = sys.stdin.readlines()
    T = int(lines[0])
    
    for i, line in enumerate(lines[1:]):
        N, K = line.split(' ')
        on = solve(int(N), int(K))
        str_on = 'OFF'
        if on:
            str_on = 'ON'
        print 'Case #%d: %s' % (i+1, str_on)

if __name__ == '__main__': main()
