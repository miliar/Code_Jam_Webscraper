from math import pi
T = int(input())
for t in range(1, T+1):
    n, k = map(int, input().split())
    L = [tuple(map(int, input().split())) for i in range(n)]
    mx = 0
    for i in range(n):
        R = L[:i]+L[i+1:]
        R = [2*pi*r[0]*r[1] for r in R]
        R = sorted(R)[::-1] 
        sm = pi*L[i][0]**2+2*pi*L[i][0]*L[i][1]
        sm += sum(R[:k-1])
        mx = max(sm, mx)
    print("Case #%d: %.10f" %(t, mx))
