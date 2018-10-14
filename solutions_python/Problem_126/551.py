#!/usr/bin/env python
#-*- coding:utf-8 -*-

C = {}

for c in "bcdfghijklmnpqrstvwxyz":
    C[c] = 1
C["a"] = 0
C["e"] = 0
C["i"] = 0
C["o"] = 0
C["u"] = 0

def convert(name):
    return map(lambda c: str(C[c]), name)

def solve(name, n):
    c = 0
    for i in range(0, len(name)+1):
        for j in range(i+n, len(name)+1):
            try:
                name[i:j].index("1"*n)
                c += 1
            except ValueError:
                pass
    return c


def main():
    t = int(raw_input())
    for tc in xrange(1, t+1):
        name, n =  tuple(raw_input().split())
        n = int(n)
        name = "".join(convert(name))
        print "Case #%d: %d" % (tc, solve(name, n)) 

if __name__ == '__main__':
    main()


