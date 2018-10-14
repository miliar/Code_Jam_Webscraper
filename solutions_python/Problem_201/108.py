def update(d, k, v):
    if k in d:
        d[k] += v
    else:
        d[k] = v
    return d

for tc in range(1, int(raw_input())+1):
    n, k = map(int, raw_input().split())
    vals = {n: 1}
    depth = 0
    while k > 2**depth:
        k -= 2**depth
        newvals = {}
        for size in vals:
            if size%2 == 1:
                newvals = update(newvals, (size-1)/2, 2*vals[size])
            else:
                newvals = update(newvals, size/2, vals[size])
                newvals = update(newvals, size-size/2-1, vals[size])
        vals = newvals
        depth += 1
    if vals[max(vals)] >= k:
        v = max(vals)
    else:
        v = min(vals)
    mx = v/2
    mn = v-mx-1
    print "Case #%d: %d %d" % (tc, mx, mn)
