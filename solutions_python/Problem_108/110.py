#!/usr/bin/python
import sys
from collections import deque

class P(object):
    pass

def mySol(params):
    N = params.N
    D = params.D
    d = params.d
    l = params.l
    
    reach = [0] * (N) 
    reach[0] = d[0]*2
    q = deque()
    q.append(0)
    #continue as long as an improvement is possible   
    while (q):
        i = q.popleft()
        if reach[i]>=D: return "YES"
        for j in xrange(i+1,N):
            if d[j]>reach[i]: break
            newReach = max( [reach[j], d[j] + min([d[j]-d[i],l[j] ]) ])
            if newReach > reach[j] and (j not in q):
                q.append(j)
                reach[j] = newReach
    return "NO"
            
       

T = int(sys.stdin.readline().strip())
for case in xrange(T):
    params=P()
    params.N = [int(x) for x in sys.stdin.readline().split()][0]
    params.d = []
    params.l = []
    for i in xrange(params.N):
        d,l = [int(x) for x in sys.stdin.readline().split()]
        params.d.append(d)
        params.l.append(l)
    params.D = [int(x) for x in sys.stdin.readline().split()][0]
    print 'Case #%d: %s' % (case+1,mySol(params))



