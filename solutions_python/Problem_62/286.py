import sys
from bisect import bisect


cases=int(sys.stdin.readline())

for i in range(1, cases+1):
    [wires]=sys.stdin.readline().split()
    wires=int(wires)
    res=0
    forward=[]
    backward=[]
    for j in range(wires):
        [a, b]=sys.stdin.readline().split()
        a=int(a)
        b=int(b)
        forward.append((a,b))
        backward.append((b,a))
    forward.sort()
    backward.sort()
#    print forward
#    print backward
    for (j,k) in forward:
        l=bisect(backward, (k,0))
        for r in range(l, len(backward)):
            (m,n)=backward[r]
#            print j, k, m, n
            if (j>n):
                res+=1
    print "Case #%d: %d"%(i, res)
        
