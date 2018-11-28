#!/usr/local/bin/python2.6
import sys

t = int(sys.stdin.readline())
for _ in range(1,t+1):
    n,k = map(int, sys.stdin.readline().split())
    if (k & (1<<n)-1) == ((1<<n)-1):
        print "Case #%d: ON" % _
    else:
        print "Case #%d: OFF" % _
