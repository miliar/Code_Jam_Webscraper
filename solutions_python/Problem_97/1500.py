#!/usr/bin/env python
#-*- coding: ISO-8859-1 -*-

import sys

file_in = 'C-small.in'
file_out = 'C-small.out'

def solve(A, B):
    result = 0
    
    for n in xrange(A, B):
        ns = str(n)
        for i in xrange(1, len(ns)):
            ms = ns[-i:] + ns[:len(ns) - i]
            m = int(ms)
            if A <= n < m <= B and len(ns) == len(ms):
                result += 1
    
    return result

if __name__ == '__main__':
    i = open(file_in, 'r')
    o = open(file_out, 'w')
    T = int(i.readline().strip())
    for case in xrange(T):
        A, B = map(int, i.readline().strip().split(' '))
        result = solve(A, B)
        o.write('Case #%d: %d\n' % (case + 1, result))
    o.close()
    i.close()
    sys.exit(0)
