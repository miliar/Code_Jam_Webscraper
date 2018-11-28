#!/usr/bin/env python
class Coaster:
    k=0
    count=0
    def __init__(self,k):
        self.k=k
    def run(self,groups):
        count=0
        index=0
        for group in groups:
            group=count+group
            if group>self.k:
                break
            else:
                index=index+1
                count=group
        self.count=self.count+count
        for i in range(0,index):
            groups.append(groups.pop(0))

from sys import stdin
T=int(stdin.readline())
for case in range(1,T+1):
    R,k,N=map(int,stdin.readline().split())
    groups=map(int,stdin.readline().split())
    coaster=Coaster(k)
    for i in range(0,R):
        coaster.run(groups)
    print "Case #%d: %d" % (case,coaster.count)
