def check (m):
    i = 0
    sum = u
    while (i < n) and (p[i] < m):
        sum -= (m - p[i])
        if sum < 0:
            return False
        i += 1
    return True    
T = int(input())
for t in range(1,T+1):
    n, k = map(int,input().split())
    u = float(input())
    p = list(map(float,input().split()))
    p.sort()
    L = p[0]
    R = 1.00000000000000001
    for jj in range(200):
        m = (L + R) / 2
        if check(m):
            L = m
        else:
            R = m
    ans = 1    
    for i in range(k):
        if p[i] > L:
            ans *= p[i]
        else:
            ans *= L
    print('Case #'+str(t)+':', ans)
        