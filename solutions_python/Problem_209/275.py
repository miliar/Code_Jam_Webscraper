import math
for t in range(int(input())):
    n, k = map(int, input().split())
    p = [(tuple(map(int, input().split()))) for i in range(n)]
    
    q = [(2*math.pi*p[i][1]*p[i][0], p[i][1], p[i][0], i) for i in range(n)]
    q.sort()

    best = 0
    for i in range(n):
        br, bh = p[i]
        area = math.pi*br*br + 2*math.pi*br*bh
        c = 1
        if c<k:
            for j in range(n-1, -1, -1):
                if q[j][3]!=i and q[j][2]<=br:
                    area += q[j][0]
                    c += 1
                    if c==k:
                        break
        if c==k:
            best = max(best, area)
    print('Case #{}: {}'.format(t+1, best))


