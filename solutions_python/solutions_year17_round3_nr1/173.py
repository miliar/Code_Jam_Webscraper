import math
T = int(input())
for x in range(1, T + 1):
    N, K = map(int, input().split())
    Rs = []
    Hs = []
    arr = []
    s0 = {}
    s1 = {}
    for i in range(N):
        R, H = map(int, input().split())
        Rs.append(R)
        Hs.append(H)
        arr.append((R, math.pi * R**2, 2 * math.pi * R * H))
    arr = list(reversed(sorted(arr)))
    ans = 0.0
    for i in range(N - K + 1):
        r, s0, s1 = arr[i]
        ans = max(ans, sum(list(reversed(sorted([e[2] for e in arr[i + 1:]])))[:K - 1]) + s0 + s1)
    print("Case #%d: %f" % (x, ans))
