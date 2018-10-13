def t(x, y):
    a1, v1 = x
    a2, v2 = y
    return - (a1 - a2) / (v1 - v2)
def solve(k, s):
    tmax = 0
    ans = 0
    for u in s:
        d = t(u, (k, 0))
        if tmax < d:
           tmax = d
           ans = u[0] / d + u[1]
    return ans
N = int(input())
for i in range(1, N + 1):
    k, n = map(int, input().split())
    s = list()
    for _ in range(n):
        x, y = map(int, input().split())
        s.append((x, y))
    a = solve(k, s)
    print('Case #%d: %f' % (i, a))
