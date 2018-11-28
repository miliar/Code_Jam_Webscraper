#coding=utf-8
class memoize(dict):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        return self[args]

    def __missing__(self, key):
        result = self[key] = self.func(*key)
        return result

@memoize
def calc(p, n):
    if p <= n:
        return 0
    return min(calc(p - p/2, n) + calc(p/2, n) + 1,  (p + n - 1) / n - 1)

T = int(raw_input())
for case in range(1, T + 1):
    _ = int(raw_input())
    P = map(int, raw_input().split())
    ans = max(P)
    for i in range(1, 1001):
        ans = min(ans, sum([calc(p, i) for p in P]) + i)
    print "Case #%d: %d"%(case, ans)


