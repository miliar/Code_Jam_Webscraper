def compute(lawn, N, M):
    nm = min(min(x for x in line) for line in lawn)
    while True:
        m = nm
        lines = [False] * N
        cols = [False] * M
        for l in xrange(N):
            lines[l] = all(lawn[l][c] == m for c in xrange(M))
        for c in xrange(M):
            cols[c] = all(lawn[l][c] == m for l in xrange(N))
        for l in xrange(N):
            for c in xrange(M):
                if lawn[l][c] == m and (not lines[l] and not cols[c]):
                    print 'NO'
                    return
        try:
            nm = min(min(x for x in line if x != m) for line in lawn)
        except ValueError:
            print 'YES'
            return
        for l in xrange(N):
            for c in xrange(M):
                if lawn[l][c] == m:
                    lawn[l][c] = nm


def run():
    T = int(raw_input())
    for i in xrange(T):
        N, M = [int(x) for x in raw_input().split()]
        lawn = []
        for _ in xrange(N):
            line = [int(x) for x in raw_input().split()]
            lawn.append(line)
        print 'Case #%d:' % (i + 1),
        compute(lawn, N, M)

if __name__ == '__main__':
    run()
