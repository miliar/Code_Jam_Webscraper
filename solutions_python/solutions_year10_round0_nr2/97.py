#from __future__ import division
import sys

def dbg(obj):
    print>>sys.stderr,obj

def gcd(a,b):
    a,b=(b,a) if b>a else (a,b)
    c=a%b
    while c<>0:
        a,b=b,c
        c=a%b
    return b

def gcdm(nums):
    if len(nums)==1:
        return nums[0]
    if len(nums)==2:
        return gcd(nums[0],nums[1])
    else:
        return gcdm([gcd(nums[0],nums[1])]+nums[2:])
    
f=open('c:\\B-large.in')
case_num=int(f.readline().strip())
for cur_case in range(case_num):
    print 'Case #%d:'%(cur_case+1),
    events = [int(s) for s in f.readline().split()][1:]
    dbg(events)
    events.sort() #???
    dbg(events)
    diff=[]
    for i in range(1,len(events)):
        c = events[i]-events[i-1]
        if c<>0:
            diff.append(events[i]-events[i-1])
    dbg(diff)
    if len(diff)<>0:
        g = gcdm(diff)
    else:
        g = events[0]
        dbg('impossible')
    dbg('gcd=%d'%g)
    rs=(g-events[0]%g)%g
    dbg('rs=%d'%rs)
    print rs
f.close()