#!/usr/bin/env python

import os
import sys


def solve(N):
    while True:
        l = 0
        m = ''
        modified = False
        for n in N:
            if modified:
                m += '9'
                continue
            if int(n) >= l:
                m += n
                l = int(n)
                continue
            m = m[:-1] + str(int(l) - 1) + '9'
            modified = True
        N = m
        if not modified:
            break
    return m.lstrip('0')

def main():
    T = int(sys.stdin.readline().strip())
    for t in range(T):
        N = sys.stdin.readline().strip()
        result = solve(N)
        if result is None:
            print 'Case #%d: IMPOSSIBLE' % (t + 1)
        else:
            print 'Case #%d: %s' % (t + 1, result)

if __name__ == '__main__':
    main()

