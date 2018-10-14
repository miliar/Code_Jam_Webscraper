import sys
#sorry for the horrible code repitition.
from collections import deque
cases = int(sys.stdin.readline())
for i in range(1,cases+1):
    args = sys.stdin.readline().split()
    R = int(args[0])
    K = int(args[1])
    N = int(args[2])        
    q = deque([int(t) for t in sys.stdin.readline().split()])
    while len(q) < N:
        q.extend([int(t) for t in sys.stdin.readline().split()])
    startingpoint = q.__copy__()
    m=0
    j=1
    flag = False
    while j <= R:
        pcount = 0
        gcount = 0
        while (gcount < N) and (pcount + q[0] <= K):        
            g0 = q.popleft()
            pcount += g0
            m += g0
            q.append(g0)
            gcount +=1
        if(q == startingpoint) and j< R:
            flag = True            
            break;
        j +=1
    if flag:
        m *= R/j
        c = 1
        while c <= R%j:
            pcount = 0
            gcount = 0
            while (gcount < N) and (pcount + q[0] <= K):        
                g0 = q.popleft()
                pcount += g0
                m += g0
                q.append(g0)
                gcount +=1
            c +=1
    print "Case #{0}: {1}".format(i,m)