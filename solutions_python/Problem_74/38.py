#!/usr/bin/python

import sys, re, string, math

def do_one_case(cnum):
    v = sys.stdin.readline().split()
    N = int(v[0])
    assert len(v)==2*N+1
    t = { "B":0, "O":0 }
    p = { "B":1, "O":1 }
    for i in range(N):
        r = v[2*i+1]
        rx = "B" if r=="O" else "O"
        b = int(v[2*i+2])
        tt = max(t[rx], t[r] + abs(b-p[r])) + 1
        p[r] = b
        t[r] = tt
    print "Case #%d: %d" % (cnum, tt)


def main():
    N = int(sys.stdin.readline().strip())
    for i in range(N):
        do_one_case(i+1)


if __name__ == "__main__":
    main()
