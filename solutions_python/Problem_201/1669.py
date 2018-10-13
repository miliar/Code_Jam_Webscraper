import heapq

T = int(input().split()[0])

for i in range(T):
    N, K = [int(x) for x in input().split()]
    def f(n):
        return ((n-1)//2, (n)//2)
    S = []
    heapq.heappush(S, -N)
    for j in range(K-1):
        n = -heapq.heappop(S)
        n1, n2 = f(n)
        heapq.heappush(S, -n1)
        heapq.heappush(S, -n2)
    n = -heapq.heappop(S)
    n1, n2 = f(n)
    print('Case #{0}: {1} {2}'.format(i+1, n2, n1))
