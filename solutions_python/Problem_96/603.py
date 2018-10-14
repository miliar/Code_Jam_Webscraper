def value(x, k):
    if x <= 1:
        return x
    return x / 3 + 1 if x % 3 == 1 else (x + 1) / 3 + k

def solve():
    a = map(int, raw_input().split())
    n, s, p = a[:3]
    t = a[3:]
    ret = 0
    for x in t:
        v = value(x, 0)
        if v >= p:
            ret += 1
        elif s > 0 and value(x, 1) >= p:
            s -= 1
            ret += 1
    return ret

for cas in range(1, int(raw_input()) + 1):
    print 'Case #%d: %d' % (cas, solve())
