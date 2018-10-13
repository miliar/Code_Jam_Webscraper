from queue import *

def calcSize(N, K):
    pq = PriorityQueue()
    pq.put(-N)
    for i in range(K):
        size = -pq.get()
        mindist = (size-1) // 2
        maxdist = size-1-mindist
        if size > 1:
            pq.put(-mindist)
            pq.put(-maxdist)
    return (maxdist, mindist)

T = int(input())
for case in range(T):
    N, K = map(int, input().split())
    maxd, mind = calcSize(N, K)
    print("Case #"+str(case+1)+": "+str(maxd)+" "+str(mind))
