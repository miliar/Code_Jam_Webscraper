import heapq

tc = int(input())
for t in range(tc):
    n, k = map(int, input().split())
    H = []
    heapq.heappush(H, (-n, 1))
    k -= 1
    while k:
        n, c = heapq.heappop(H)
        if k < c:
            heapq.heappush(H, (n, c - k))
            c = k
        k -= c
        n = -n
        if n & 1:
            heapq.heappush(H, (-(n // 2), c * 2))
        else:
            heapq.heappush(H, (-(n // 2), c))
            heapq.heappush(H, (-(n // 2 - 1), c))
    n, c = heapq.heappop(H)
    n = -n
    if n & 1:
        y = z = n // 2
    else:
        y, z = n // 2, n // 2 - 1
    print("Case #{}: {} {}".format(t + 1, y, z))
