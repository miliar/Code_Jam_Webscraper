def simulate(cells, prisoners):
    res = 0

    for c in cells:
        prisoners[c] = False
        at = c - 1

        while at >= 0 and prisoners[at]:
            res += 1
            at -= 1

        for p in prisoners[c+1:]:
            if not p:
                break
            res += 1
        
    return res


def permutations(xs):
    if len(xs) <= 1:
        yield xs
    else:
        for p in permutations(xs[1:]):
            for i in range(len(p) + 1):
                yield p[:i] + xs[0:1] + p[i:]


def solve(P, cells):
    best = None
    for c in permutations(cells):
        prisoners = [True for x in xrange(P)]
        temp = simulate(c, prisoners)
        if (not best) or (temp < best):
            best = temp

    return best


N = int(raw_input())

for t in xrange(N):
    P, Q = map(int, raw_input().split())
    cells = map(int, raw_input().split())
    cells = map(lambda x: x - 1, cells)

    print 'Case #%d: %d' % (t+1, solve(P, cells))
