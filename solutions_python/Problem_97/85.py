#!/usr/bin/python

import os
import sys

fin = sys.stdin

def normalize(x):
    s = str(x)
    smallest = x
    for i in xrange(1, len(s)):
        n = int(s[i:] + s[:i])
        if n < smallest:
            smallest = n
    return smallest

def main():
    T = int(fin.readline())
    for t in xrange(1, T + 1):
        A, B = map(int, fin.readline().split())
        m = {}
        for n in xrange(A, B+1):
            x = normalize(n)
            if x in m:
                m[x] += 1
            else:
                m[x] = 1
        count = 0
        for x in m.values():
            if x > 1:
                count += (x * x - x) / 2
        print 'Case #%d: %d' % (t, count)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        fin = open(sys.argv[1], 'r')
    main()
