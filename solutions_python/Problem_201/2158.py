import heapq
T = int(raw_input())
for r in xrange(T):
    N, K = map(int, raw_input().split())
    pq = []
    heapq.heappush(pq, -N)
    for i in xrange(K-1):
        top = -heapq.heappop(pq)
        if top % 2 == 0:
            heapq.heappush(pq, -(top/2))
            heapq.heappush(pq, -(top/2 - 1))
        else:
            heapq.heappush(pq, -(top/2))
            heapq.heappush(pq, -(top/2))
    end = -1* pq[0]
    if end % 2 == 0:
        print "Case #%d: %d %d" %(r+1, end/2, end/2 - 1)
    else:
        print "Case #%d: %d %d" %(r+1,end/2, end/2)
    
