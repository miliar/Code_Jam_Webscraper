#!/usr/bin/python
import sys
import string

def rl():
    return sys.stdin.readline().strip()

def normal(i):
    return min(i, i // 3 + bool(i % 3))

def special(i):
    return min(i, i // 3 + (i % 3 or 1))

def main():
    T = int(rl())
    for case in range(1, T+1):
        line = map(int, rl().split())
        N, S, p = line[:3]
        t = line[3:]
        c = 0
        for g in t:
            m = normal(g)
            if m+1 == p and S and special(g) == p:
                S -= 1
                m += 1
            if m >= p:
                c += 1
        print 'Case #%d: %d' % (case, c)

if __name__ == '__main__':
    main()
