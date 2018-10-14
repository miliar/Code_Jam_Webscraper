import os
import math
from collections import defaultdict
__author__ = 'steven'

question='qb'
fs={'t1','small.in','large'}
def getmincost(n,c,f,x):
    t=0.0

    for i in range(0,n):
        t+=1/(2+f*i)
    t=t*c
    t+=x/(2+f*n)
    ct=getmincostnshift(n,c,f,x)
    return min(t,ct);

def getmincostnshift(n,c,f,x):
    t=0.0
    n-=1;

    for i in range(0,n):
        t+=1/(2+f*i)
    t=t*c
    t+=x/(2+f*n)
    return t
def getminn(c,f,x):
    return int(math.ceil((x*f-2*c)/(c*f)))
def solver(c,f,x):
    if (x*f-2*c)<0:
        return x/2
    minn=getminn(c,f,x)
    return getmincost(minn,c,f,x)


for s in fs:
    print question+s
    f='./'+question+s
    if os.path.isfile('./'+question+s):
        ls=open(f)
        noq=(int)(ls.readline())
        fout=open(question+s+'-a','w')
        print noq
        for i in range(0,noq):
            fa=ls.readline()
            fa=fa.split();
            c, f, x=[float(s) for s in fa]
            fout.write('Case #%d: %f\n'%(i+1,solver(c,f,x)))

#Case #1: 7
#Case #2: Bad magician!
#Case #3: Volunteer cheated!


