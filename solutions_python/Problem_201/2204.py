from collections import Counter
def split(n):
    l = n // 2
    r = max(0, n - l - 1)
    return (l, r)

t = int(input())
for c in range(t):
    n, k = map(int,input().split())
    d = Counter()
    d[n] = 1
    for i in range(k):
        e = max(d)
        l,r = split(e)
        d[e] -= 1
        if d[e] == 0:
            del d[e]
        d[l] += 1
        d[r] += 1
    print("Case #{}: {} {}".format(c+1, l,r))
