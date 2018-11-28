#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import sys
import os
import time
import itertools
import collections

ss = """1 1
2 4
3 9
11 121
22 484
101 10201
111 12321
121 14641
202 40804
212 44944
1001 1002001
1111 1234321
2002 4008004
10001 100020001
10101 102030201
10201 104060401
11011 121242121
11111 123454321
11211 125686521
20002 400080004
20102 404090404
100001 10000200001
101101 10221412201
110011 12102420121
111111 12345654321
200002 40000800004
1000001 1000002000001
1001001 1002003002001
1002001 1004006004001
1010101 1020304030201
1011101 1022325232201
1012101 1024348434201
1100011 1210024200121
1101011 1212225222121
1102011 1214428244121
1110111 1232346432321
1111111 1234567654321
2000002 4000008000004
2001002 4004009004004"""


x = [int(y.split()[-1]) for y in ss.split("\n")]
#print x

f = lambda(s):s==''.join([s[len(s)-1-i] for i in range(len(s))])

def g(x):
    for i in range(1,x):
        if f(str(i)) and f(str(i*i)):
            print i, i*i


def main():
    tt = int(raw_input())
    #print "t=",tt
    for t in xrange(tt):
        m,n = map(int, raw_input().strip().split())
        ans = [y for y in x if m<=y<=n]
        print "Case #%d: %d" % (t+1, len(ans))


if __name__ == '__main__':
    main()
