import heapq

for sadsf in range(int(input())):
    n, m = map(int, input().split())
    m -= 1
    h = []
    heapq.heappush(h, -n)
    d = {n:1}
    j = n
    while m > 0:
        #        print(d, h)
        if d[j] > m:
            break
        m -= d[j]
        if (j-1)//2 not in d:
            d[(j-1)//2] = 0
            heapq.heappush(h, -((j-1)//2))
        d[(j-1)//2] += d[j]
        if j//2 not in d:
            d[j//2] = 0
            heapq.heappush(h, -(j//2))
        d[j//2] += d[j]
        del d[j]
        heapq.heappop(h)
        j = -h[0]
    
    print('Case #{}: {} {}'.format(sadsf + 1, j//2, (j-1)//2))
