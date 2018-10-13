EPS = 1e-9
T = int(input())
for t in range(1,T+1):
    n, k = map(int, input().split())
    u = float(input())
    L = list(map(float, input().split()))
    L = sorted(L)
    cnt = 1
    a = L.pop(0)
    while (u-EPS) > 0 and L:
        b = L.pop(0)
        m = min(u/cnt, b-a)
        a += m
        u -= m*cnt
        if (u-EPS) > 0:
            cnt += 1
        else:
            L.append(b)
    pr = a**cnt
    if (u-EPS) > 0:
        pr = (a+u/n)**n
    else: 
        for l in L:
            pr *= l
    print("Case #%d: %.10f" %(t, pr))
