
def solve(D, L, dist, pos=0, idx=0):
    mlen = D[idx] - pos
    pmax = pos + mlen * 2
    if L[idx] < mlen:
        return False
    if pmax >= dist:
        return True
    for i in xrange(idx + 1, len(D)):
        if D[i] > pmax:
            break
        if solve(D, L, dist, max(D[idx], D[i] - L[i]), i):
            return True
    return False

def main(f):
    T = int(f.readline())
    for i in xrange(T):
        N = int(f.readline())
        D, L = [], []
        for j in xrange(N):
            d, l = map(int, f.readline().split(' '))
            D.append(d)
            L.append(l)
        DD = int(f.readline())
        res = solve(D, L, DD)
        print 'Case #%d: %s' % (i + 1, res and 'YES' or 'NO')

if __name__ == '__main__':
    import sys
    main(sys.stdin)
