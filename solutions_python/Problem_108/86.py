def solve():
    N = int(raw_input())
    vines = []
    for i in xrange(N):
        vines.append(map(int, raw_input().split()))
    D = int(raw_input())
    i = 0
    pre = 0
    cur = 0
    while True:
        d, l = vines[i]
        cur = d + min(d - pre, l)
        if cur >= D:
            break
        pre = d
        i += 1
        if i == len(vines):
            return "NO"
        d, l = vines[i]
        if d > cur:
            return "NO"
        best = 0
        for d, l in vines:
            if d <= cur:
                dist = d + min(d - pre, l)
                best = max(best, dist)
        if best >= D:
            break
        best2 = 0
        for d, l in vines:
            if d <= best:
                best2 = max(best2, d)
        d, l = vines[i]
        while d <= cur:
            d, l = vines[i]
            if d + min(d - pre, l) >= best2:
                break
            i += 1
    return "YES"

T = int(raw_input())
for i in range(T):
    print "Case #%d:" % (i + 1), solve()
