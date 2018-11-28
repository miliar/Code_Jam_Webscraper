from itertools import zip_longest
def solve_small(n, cs):
    if max(cs) * 2 > n:
        return "IMPOSSIBLE"
    cs, hs = zip(*sorted(zip(cs, "RYB")))
    ans = list()
    while cs[2] * 2 < n and cs[0] > 0:
        cs = [c - 1 for c in cs]
        ans += hs
        n -= 3
    for x, y in zip_longest(hs[0] * cs[0] + hs[1] * cs[1], hs[2] * cs[2]):
        if x: ans.append(x)
        if y: ans.append(y)
    return ''.join(ans)

t = int(input())
for i in range(1, 1 + t):
    n, r, _, y, _, b, _ = map(int, input().split())
    print('Case #%d: %s' % (i, solve_small(n, [r, y, b])))
