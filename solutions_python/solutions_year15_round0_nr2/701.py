t = int(input())

memo = {};

def best(f):
    tf = tuple(f)
    if tf in memo: return memo[tf]
    m = float("inf")
    I = max([j for j in range(len(f)) if f[j] != 0])
    p = f[:]
    if I > 1:
        for i in range(1, I):
            p[I] -= 1
            p[i] += 1
            p[I - i] += 1
            m = min(m, 1 + best(p))
            p[I] += 1
            p[i] -= 1
            p[I - i] -= 1
    m = min(m, I)
    memo[tf] = m
    return m

for test in range(t):
    memo = {}
    n = int(input())
    l = list(map(int, input().split()))
    f = [0 for i in range(1+max(l))]
    for i in l:
        f[i] += 1
    print("Case #{}: {}".format(test+1, best(f)))
