#!/usr/bin/env python3
# vim:set sw=4 et smarttab:
# Round 1C 2014

import sys
import fractions

def main():
    filein = sys.stdin
    #filein = open('filename.in', 'r')
    line = filein.readline()
    fields = line.split()
    assert len(fields) == 1
    ntc = int(fields[0])

    for tc in range(1, ntc + 1):
        line = filein.readline()
        fields = line.split('/')
        assert len(fields) == 2
        p = int(fields[0])
        q = int(fields[1])
        answer = solve(p, q)
        if answer == None:
            answer = 'impossible'
        print('Case #{0}: {1}'.format(tc, answer))

def solve(p, q):
    d = fractions.gcd(p, q)
    p //= d
    q //= d
    if not power_of_two(q):
        return
    ret = recur(p, q)
    return ret

def power_of_two(a):
    assert a > 0
    t = 1
    while t < a:
        t *= 2
    return t == a

def recur(p, q):
    if p >= q // 2:
        return 1
    return recur(p, q // 2) + 1

if __name__ == '__main__':
    main()
