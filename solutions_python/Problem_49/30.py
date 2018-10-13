import sys,re
import math
import string

def ri(f):  
    return int(f.readline().strip())
def rlf(f,fn):
    return map(fn, f.readline().strip().split())

def rl(f):
    return f.readline().strip().split()

f=open( sys.argv[1])
N=ri(f)
for i in xrange(N):
    n=ri(f)
    P=[]
    for j in range(n):
        P.append(rlf(f,int))
    
    pairs=[(0,1,2),(1,2,0),(0,2,1)]
    best=1000000
    if n==1:
        best=P[0][2]
    elif n==2:
        tt=pairs[0]
        (x1,y1,r1)=P[tt[0]]
        (x2,y2,r2)=P[tt[1]]
        r = max(r1,r2)
        best = min(best,r)
    else:
            
        for tt in pairs:
            (x1,y1,r1)=P[tt[0]]
            (x2,y2,r2)=P[tt[1]]
            (x3,y3,r3)=P[tt[2]]
            r = max(r3, (r1+r2+math.sqrt(pow(x2-x1,2) + pow (y2-y1,2)))/2) 
            best = min(best,r)
        
    print "Case #"+str(i+1)+": "+ str(best)


