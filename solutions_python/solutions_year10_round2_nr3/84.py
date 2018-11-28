#!/usr/bin/env python

import re, sys

def check(a, sz):
    r = a[0]
    while r != 1:
        try:
            r = sz - a.index(r)
        except:
            return 0
    return 1
        
def go(a, n, depth):
    a[depth] = n
    t = check(a, depth+1)
    for x in xrange(2,n):
        t += go(a, x, depth+1)
    return t

done = {}
def solve(n):
    if done.has_key(n):
        return done[n]
    a = [None] * n
    ret = go(a, n, 0)
    done[n] = ret
    return ret

def main():
    lines = sys.stdin.readlines()
    T = int(lines[0])
    
    for i, line in enumerate(lines[1:]):
        output = solve(int(line)) % 100003
        print 'Case #%d: %s' % (i+1, output)

if __name__ == '__main__': main()
