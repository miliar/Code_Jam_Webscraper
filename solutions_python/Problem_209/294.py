import sys
import math

t = int(sys.stdin.readline())
for t0 in range(t):
    n, k = sys.stdin.readline().split(' ')
    n, k = int(n), int(k)
    l = []

    for n0 in range(n):
        r, h = sys.stdin.readline().split(' ')
        r, h = int(r), int(h)
        l.append((r,h))

    l = sorted(l)
    l = sorted(l, key = lambda x : 2 * math.pi * x[0] * x[1], reverse = True)

    chosen = set({})
    max_r = 0
    k0 = 0
    res = 0
    for i,x in enumerate(l):
        if k0 == k: 
            break
        res += 2*math.pi*x[0] * x[1]
        chosen.add(x)
        max_r = max(max_r, x[0])
        last = x
        k0 += 1

    l = sorted(l, key = lambda x : math.pi * x[0] * x[0] + 2 * math.pi * x[0] * x[1], reverse = True)

    for x in l:
        if x in chosen:
            continue
        else:
            if x[0] > max_r and math.pi * x[0] * x[0] + 2 * math.pi * x[0] * x[1] > 2*math.pi * last[0] * last[1] + math.pi * max_r * max_r:
                res -= 2*math.pi * last[0] * last[1]
                res += math.pi * x[0] * x[0] + 2 * math.pi * x[0] * x[1]
                break
    else:
        res += math.pi * max_r * max_r


    print("Case #", t0 + 1, ": ", res, sep = '')