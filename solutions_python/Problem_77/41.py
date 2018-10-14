#!/usr/bin/python

import sys, re, string, math

def do_one_case(cnum):
    N = int(sys.stdin.readline().strip())
    v = map(lambda x: int(x)-1, sys.stdin.readline().split())
    assert len(v)==N
    assert sorted(v)==range(N)
    t = len([ 1 for i in range(N) if v[i] != i])
    print "Case #%d: %.6f" % (cnum, t)



def main():
    N = int(sys.stdin.readline().strip())
    for i in range(N):
        do_one_case(i+1)


if __name__ == "__main__":
    main()
