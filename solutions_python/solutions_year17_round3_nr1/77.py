from math import acos
t = int(input())
r = [0]*1005
h = [0]*1005
for ii in range(t):
    n, k = [int(x) for x in input().split()]
    for i in range(n):
        r[i], h[i] = [int(x) for x in input().split()]
    ans = 0
    for i in range(n):
        pq = []
        for j in range(n):
            if i != j and r[j] <= r[i]:
                pq.append(r[j] * h[j])
        tmp = r[i] * h[i]
        if len(pq) < k - 1:
            continue
        pq.sort()
        for j in range(k - 1):
            tmp += pq[-j-1]
        tmp *= 2
        tmp += r[i] ** 2
        ans = max(ans, tmp)
    print("Case #{}: {}".format(ii + 1, ans * acos(-1)))
