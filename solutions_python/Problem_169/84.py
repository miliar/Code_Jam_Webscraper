import numpy as np
import sys
f = open("b3.in")
sys.stdout=open('out','w')
def raw_input():
    return f.readline().strip()
for i in range(int(raw_input())):
    print "Case #%d:"%(i+1),
    n,v,t= map(float, raw_input().split())
    n=int(n)
    l=[None]*n
    for i in range(n):
        l[i]= list(map(float, raw_input().split()))
    if t<min(i[1] for i in l) or t>max(i[1] for i in l):
        print "IMPOSSIBLE"
    else:
        if n==1:
            print v/l[0][0]
        elif l[0][1]==l[1][1]:
            print "%f"%(v/(l[0][0]+l[1][0]))
        else:
            a = [[None] * n for _ in range(2)]
            for i in range(n):
                a[0][i]=l[i][0]
                a[1][i]=l[i][1]*l[i][0]
            a=np.array(a)
            b=np.array([v,v*t])
            s=np.linalg.solve(a,b)
            print "%f"%(max(s))