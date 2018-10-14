from heapq_max import *

def solve():
    n,k = map(int, input().split())
    pq = []
    heappush_max(pq, (n+1, n+1, (0, n+1)))
    last = None

    for _ in range(k):
        p = heappop_max(pq)
        ls, rs = p[2]
        s = (ls + rs) // 2
        heappush_max(pq, (s-ls, n-ls, (ls, s)))
        heappush_max(pq, (rs-s, n-s, (s, rs)))
        # for i in range(len(pq)):
        #     print(pq[i])
        last = ((s-ls-1), (rs-s-1))
    return "{0} {1}".format(max(last[0], last[1]), min(last[0], last[1]))
    
t = int(input())
for i in range(t):
    print("Case #{0}: {1}".format(i+1, solve()))