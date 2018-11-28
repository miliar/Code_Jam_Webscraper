# -*- coding: utf-8 -*-

import os,sys
import math

def jamout(linestring):
    if istest:
        print linestring
    else:
        fo.write(linestring + '\n')
        print linestring

def ispal(n):
    st = str(n)
    l  = len(st)
    if l % 2 == 0:
        for i in range(l/2):
            if st[i]!=st[l-i-1]:
                return False
        return True
    else:
        for i in range((l-1)/2):
            if st[i]!=st[l-i-1]:
                return False
        return True
def make_fair():
    lst = []
    for i in range(10000000):
        if ispal(i**2) and ispal(i):
            print str(i**2)+',',


ex = """3
1 4
10 120
100 1000
"""

lst = [0, 1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321, 4008004, 100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004, 404090404, 10000200001, 10221412201, 12102420121, 12345654321, 40000800004, 1000002000001, 1002003002001, 1004006004001, 1020304030201, 1022325232201, 1024348434201, 1210024200121, 1212225222121, 1214428244121, 1232346432321, 1234567654321, 4000008000004, 4004009004004]

if len(sys.argv)==3:
    infile  = sys.argv[1]
    outfile = sys.argv[2]
    fo = open(outfile,'w')
    s = open(infile, 'r').read()
    lines = s.split('\n')
    istest = False
else:
    lines = ex.split('\n')
    istest = True

T = int(lines[0])
cursor = 1
for i in range(T):
    p = lines[cursor]
    mn,mx = [int(n) for n in p.split(' ')]
    cursor += 1
    #print mn,mx
    cnt = 0
    for p in lst:
        if mn<=p and p<=mx:
            cnt +=1
    
    jamout("Case #%d: %d" % (i+1, cnt))

if istest==False:
    fo.close()