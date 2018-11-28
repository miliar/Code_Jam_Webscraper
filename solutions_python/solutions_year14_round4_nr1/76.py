rl = lambda: raw_input().strip()

cases = int(rl())

for cc in xrange(cases):
    n, density = map(int, rl().split())
    sizes = sorted(map(int, rl().split()))
    taken = [False] * n
    ret = 0
    for i in xrange(n-1, -1, -1):
        if not taken[i]:
            ret += 1
            last = -1
            for j in xrange(i):
                if not taken[j] and sizes[i] + sizes[j] <= density:
                    last = j
            taken[i] = taken[last] = True
    print 'Case #%d: %d' % (cc+1, ret)
            

