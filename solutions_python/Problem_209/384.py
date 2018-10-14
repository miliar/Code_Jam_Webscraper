import math


def solve(N, K, R, H):
    RH = sorted(zip(R, H), key=lambda x: x[0] * x[1], reverse=True)
    ans = 0
    for i in range(N):
        r, h = RH[i]
        t = r * (r + 2 * h)
        xs = (RH[:i] + RH[i + 1:])[:K - 1]
        for xr, xh in xs:
            t += 2 * xr * xh
        ans = max(ans, t)
    return ans * math.pi


T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    R, H = [], []
    for _ in range(N):
        r, h = map(int, input().split())
        R.append(r)
        H.append(h)
    print('Case #{}: {:.6f}'.format(tc + 1, solve(N, K, R, H)))
