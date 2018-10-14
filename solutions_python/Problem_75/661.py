#!/usr/bin/env python2.6

import sys

def read_int():
    return int(sys.stdin.readline())

def read_ints():
    return map(int, sys.stdin.readline().split())

def read_line():
    return sys.stdin.readline().strip()

def solve():
    values = read_line().split(' ')
    C = int(values[0])
    combine = [None] * C
    for i in range(0, C):
        combine[i] = values[i+1]
    D = int(values[C + 1])
    opposed = [None] * D
    for i in range(0, D):
        opposed[i] = values[C + 2 + i]
    N = int(values[C + D + 2])
    seq = values[-1]
    r = []
    for e in seq:
        if not r:
            r.append(e)
            continue
        l = r[-1]
        combined = False
        for c in combine:
            if c[0] == e and c[1] == l or c[1] == e and c[0] == l:
                r[-1] = c[2]
                combined = True
                break                
        if not combined:
            for a in r:
                for o in opposed:
                    if o[0] == e and o[1] == a or o[1] == e and o[0] == a:
                        r = []
                        break
                if not r:
                    break
            if r:
                r.append(e)
    print str(r).replace("'", "")

def main():
    T = read_int()
    
    for case in xrange(1, T + 1):
        print 'Case #%d:' % case,
        solve()

if __name__ == '__main__':
    main()
