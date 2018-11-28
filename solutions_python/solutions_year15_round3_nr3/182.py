def all_possible(d, v):
    if len(d) == 1:
        return set([d[0]])
    p = []
    for i in range(len(d)):
        dp = d[:i] + d[i+1:]
        for x in all_possible(dp, v):
            p.append(x)
            if x + d[i] <= v:
                p.append(x+d[i])
        p.append(d[i])
    return set(p)

cache = {}
def to_add(d, v):
    ap = all_possible(d, v)
    D = set(d)
    missing = set(range(1, v+1)) - ap
    if len(missing) == 0:
        return 0
        
    f = list(sorted(missing))[0]
    possibilities = [f]
    for a in ap:
        if a >= f:
            continue
        if (f - a) not in D:
            possibilities.append(f-a)

    k = tuple(sorted(d)), f, v
    if k in cache:
        return cache[k]

    m = None
    for p in set(possibilities):
        x = to_add(d + [p], v)
        if m is None or x < m:
            m = x
            if m == 0:
                break
    cache[k] = m+1
    return m + 1


if __name__ == "__main__":
    T = int(raw_input())
    for i in range(1, T+1):
        C,D,V = map(int, raw_input().split())
        d = map(int, raw_input().split())
        print "Case #%d: %d" % (i, to_add(d,V))
