import math

T = int(input())

for t in range(1, T+1):
    n, k = map(int, input().split())
    arr = []
    for i in range(n):
        r, h = map(int, input().split())
        arr.append((r, h))

    ans = 0
    for i in range(n):
        R, H = arr[i]
        varr = [p[0]*p[1] for j, p in enumerate(arr) if p[0] <= R and j != i]
        varr = sorted(varr, reverse=True)[:k-1]
        ans = max(ans, R**2 + 2*R*H + 2*sum(varr))

    print("Case #%d:" % t, ans*math.pi)

