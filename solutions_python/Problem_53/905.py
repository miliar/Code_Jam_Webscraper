#!/usr/bin/env python
flag=None
def toogle(i):
    if i<=len(flag):
        if flag[i]:
            flag[i]=False
            toogle(i+1)
        else:
            flag[i]=True
from sys import stdin
N=int(stdin.readline())
for case in range(1,N+1):
    line=stdin.readline().split()
    n=int(line[0])
    k=int(line[1])
    flag={}
    for i in range(1,n+1):
        flag[i]=False
    for i in range(0,k):
        toogle(1)
    Flag="ON"
    for i in range(1,n+1):
        if not flag[i]:
            Flag="OFF"
            break
    print "Case #%d: %s" % (case, Flag)
