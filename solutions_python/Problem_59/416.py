import sys

def mkdir(parents, directories):
    n = 0
    for d in directories:
        while d and d not in parents:
            parents.add(d)
            d = d.rsplit('/', 1)[0]
            n += 1
    return n


if __name__ == '__main__':
    import sys
    rl = iter(sys.stdin).next
    for case in range(1, int(rl())+1):
        N, M = map(int, rl().split())
        parents = set(rl().strip() for i in xrange(N))
        directories = [rl().strip() for i in xrange(M)]
        print 'Case #%d: %s' % (case, mkdir(parents, directories))
