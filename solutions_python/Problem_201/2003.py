import heapq

def bathroomStall(n,k):
    res = []
    heapq.heappush(res,-n)
    for i in xrange(k-1):
        maxvalue = -heapq.heappop(res)
        heapq.heappush(res,-((maxvalue-1)/2))
        heapq.heappush(res,-(maxvalue-(maxvalue-1)/2-1))
    maxvalue = -heapq.heappop(res)
    return (maxvalue-1)/2,maxvalue-(maxvalue-1)/2-1

#print bathroomStall(6,2)

T = input()
for i in xrange(1,T+1):
    n,k = map(int, raw_input().split())
    res = bathroomStall(n,k)
    print "Case #%i: %i %i"%(i,max(res),min(res))
