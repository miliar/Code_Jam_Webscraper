class Snapper:
    def __init__(self):
        self.on = False
    def snap(self):
        self.on = not self.on

def snap(snappers):
    for snapper in snappers:
        snapper.snap()
        if snapper.on: break

def solve(N, K):
    return (K+1) % (1<<N) == 0
    #snappers = [Snapper() for _ in xrange(N)]
    #for i in xrange(K):
    #    snap(snappers)
    #    print ''.join('XO'[snapper.on] for snapper in snappers), i+1
    #return all(snapper.on for snapper in snappers)

if __name__ == '__main__':
    import sys
    it = iter(sys.stdin)
    next(it)
    for i, line in enumerate(it, 1):
        n, k = map(int, line.split())
        print 'Case #{0}: {1}'.format(i, 'ON' if solve(n, k) else 'OFF')
