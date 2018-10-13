from heapq import heappush, heappop

T = int(input())


for t in range(T):
    n, k = map(int, input().split())

    x = []

    for i in range(k-1):
        #print(i)
        #print(n//2, n//2 - 1 + n%2)

        x += [n//2, n//2 -1 + n%2]
        heappush(x, -(n//2))
        heappush(x, -(n//2 -1 + n%2))
        n = -heappop(x)

    print("Case #%d: %d %d" % (t+1, n//2, n//2 -1 + n%2))





