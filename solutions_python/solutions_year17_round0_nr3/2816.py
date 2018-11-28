import heapq
def lower_median(t):
    # lower exclusive
    # higher inclusive
    return (t[0]+t[1]+1)/2

def partition(t):
    lm = lower_median(t)
    return (t[0],lm-1),(lm,t[1])

def size(t):
    return t[1]-t[0]

T = int(raw_input())
for t in xrange(T):
    n, k = map(int,raw_input().split(' '))
    heap = [(-n,0,n)]
    heapq.heapify(heap)
    for i in xrange(k-1):
        p = heapq.heappop(heap)
        p = (p[1],p[2])
        a,b = partition(p)
        heapq.heappush(heap,(-size(a),a[0],a[1]))
        heapq.heappush(heap,(-size(b),b[0],b[1]))
    p = heapq.heappop(heap)
    p = (p[1],p[2])
    s = lower_median(p)
    ls = s - p[0] - 1
    rs = p[1] - s
    print "Case #{0}: {1} {2}".format(t + 1, max(ls,rs), min(ls,rs))