#!/opt/local/bin/python3.2
import math 
import sys
def clear(i):
    return math.ceil(i/3.0)
def surprising(i):
    if i==0: return 0
    return math.ceil((i-1)/3.0)+1
def solve(t,s,p):
    r=0
    for i in t:
        if clear(i)>=p:
            r+=1
        elif surprising(i)>=p and s>0:
            r+=1
            s-=1
    return r
for (i,s) in enumerate(sys.stdin.readlines()):
    if i==0: continue
    (N,S,p,*t)=(int(x) for x in s.strip().split(' '))
    assert len(t)==int(N)
    print('Case #{0}: {1}'.format(i,solve(t,S,p)))
