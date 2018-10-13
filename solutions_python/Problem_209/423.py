import math
t = int(input())
ip = lambda : map(int, input().split())
for i in range(1, t+1):
    n, k = ip()
    ans = 0
    L = []
    R = []
    H = []
    M = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for j in range(n):
        L.append(tuple(ip()))
    L.sort(reverse=True)
    for r, h in L:
        R.append(r)
        H.append(h)
    for j in range(n-1, -1, -1):
        for r in range(1, k):
            M[j][r] = max(M[j+1][r], M[j+1][r-1] + 2*R[j]*H[j])
        ans = max(ans, R[j]*R[j] + 2*R[j]*H[j] + M[j+1][k-1])
    print('Case #%d: %f'%(i, ans*math.pi))
    

