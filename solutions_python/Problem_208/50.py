import sys
from collections import defaultdict

def split(gap):
    """Return size of big gap, small gap remaining"""
    # 1->0,0
    # 2->1,0
    # 3->1,1
    return gap//2, (gap-1)//2

def go(M):
    N,K = M.split()
    N = int(N)
    K = int(K)
    D = defaultdict(int) # Map from size of gap to count
    D[N] = 1
    while K>0:
        gap = max(D)
        count = D.pop(gap)
        count = min(K,count)
        assert count
        big,small = split(gap)
        D[big] += count
        D[small] += count
        K -= count
    return '{} {}'.format(big,small)
    
    
#sys.stdin=open('datac.txt')

T=input()
for t in range(1,T+1):
    N,Q = map(int,raw_input().split())
    horse_dist = []
    horse_speed = []
    for i in range(N):
        E,S = map(int,raw_input().split()) # dist,speed
        horse_dist.append(E)
        horse_speed.append(S)
    big = max(horse_dist)+1000 # furthest distance
    slow = N * big # moving at slowest speed between all nodes
    
    edges = []
    for i in range(N):
        E = map(int,raw_input().split())
        edges.append( [big if e<0 else e for e in E] )
    # First compute min distance between all cities
    #dist = [ [big] * N for i in range(N) ]
    dist = edges
    for i in range(N):
        dist[i][i] = 0
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j] = min( dist[i][j], dist[i][k] + dist[k][j])

    #print dist
    # Then minimum time
    # In these loops we are considering quickest route from i to j
    # only using horses up to i
    time_between = [ [slow] * N for i in range(N) ]
    for i in range(N):
        time_between[i][i] = 0
    for k in range(N):
        # Find quickest time from k to each destination
        timek = [slow] * N
        s = float(horse_speed[k])
        # Try a direct route
        for d in range(N):
            if dist[k][d] <= horse_dist[k]:
                timek[d] =  dist[k][d] / s
        # Accelerate by considering going to k2 first then destination
        for k2 in range(N):
            for d in range(N):
                time_between[k][d] = min(time_between[k][d],timek[k2]+time_between[k2][d])
        # Now update best route from any start to any dest using k
        for i in range(N):
            for j in range(N):
                # Consider a route that takes horse K from k to j2
                time_between[i][j] = min( time_between[i][j], time_between[i][k] + time_between[k][j])
    
    R = []
    for q in range(Q):
        U,V = map(int,raw_input().split())
        R.append(str(time_between[U-1][V-1])) # Useing 0-based indexing
    print "Case #{}: {}".format(t,' '.join(R))

