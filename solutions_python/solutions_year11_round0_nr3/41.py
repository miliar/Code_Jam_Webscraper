#!/usr/bin/python

import sys, re, string, math

def do_one_case(cnum):
    N = int(sys.stdin.readline().strip())
    C = map(int, sys.stdin.readline().split())
    assert len(C)==N
    assert min(C)>0
    x = reduce(lambda x,y: x^y, C)
    if x:
        print "Case #%d: NO" % (cnum,)
    else:
        ans = sum(C) - min(C)
        print "Case #%d: %d" % (cnum, ans)


def main():
    N = int(sys.stdin.readline().strip())
    for i in range(N):
        do_one_case(i+1)


if __name__ == "__main__":
    main()
