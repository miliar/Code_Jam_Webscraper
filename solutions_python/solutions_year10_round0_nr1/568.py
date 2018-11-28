#!/usr/bin/env python
t=input()
for c in range(t):
    n,k=map(int,raw_input().split())
    s= (1<<n)-1
    r="OFF"
    if s&k==s:
        r="ON"
    print "Case #%s: %s"%(c+1,r)
