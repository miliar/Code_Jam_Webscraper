#!/usr/bin/python
import math
import sys
import IPython

test = 0
debug = 0

def calc(L, n, s, e, curr):
    for x in xrange(0, s+1):
        for y in xrange(e, L):
            curr.add((x,y))
    return curr

def only_cons(sbs):
    vowels = 'aeiou'
    for c in sbs:
        if c in vowels:
            return False
    return True

def solve(name, n):
    if debug: print 'input:', name, n
    idx = 0

    L = len(name)

    curr = set()
    while idx <= (L-n):
        sbs = name[idx:idx+n]
        if debug: print 'Considering: %s' % sbs
        if only_cons(sbs):
            if debug:
                print 'only cons:', sbs
                print 'before', curr
            curr = calc(L, n, idx, idx+n-1, curr)
            if debug:
                print 'after', curr
        idx += 1

    return len(curr)


lines = open(sys.argv[1]).read().split('\n')

test_num=int(lines[0])
idx=1
for x in xrange(test_num):
    curr_line = lines[idx]
    idx += 1

    name, n = curr_line.split(' ')
    n = int(n)

    ans = solve(name, n)
    print 'Case #%s: %s' % (x+1, ans)

if test:
    pass
