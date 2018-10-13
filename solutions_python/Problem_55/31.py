from collections import deque

def solve(R, k, gs):
    return sum(turns(R, k, gs))

def turns(R, k, gs):
    G = len(gs)

    def turn(i):
        limit = G
        n = 0
        while n + gs[i] <= k and limit:
            limit -= 1
            n += gs[i]
            i = (i + 1) % G
        return n, i

    i = 0
    sums = []
    idxs = []
    seen = set()
    for remain in xrange(R, 0, -1):
        if i in seen: break
        idxs.append(i)
        seen.add(i)
        n, i = turn(i)
        sums.append(n)
        yield n
    else:
        return

    sums = sums[idxs.index(i):]
    cycle = len(sums)
    q, r = divmod(remain, cycle)
    yield q * sum(sums) + sum(sums[:r])

if __name__ == '__main__':
    import sys
    it = iter(sys.stdin)
    T = int(next(it))
    for i in range(1, T+1):
        R, k, N = map(int, next(it).split())
        gs = map(int, next(it).split())
        print 'Case #{0}: {1}'.format(i, solve(R, k, gs))
