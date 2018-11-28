from sys import stdin

def read_loan():
    (n, m) = [int(x) for x in stdin.readline().strip().split()]
    l = []
    for i in xrange(n):
        row = [int(x) for x in stdin.readline().strip().split()]
        l.append(row)
    return [n, m, l]

def solve(n, m, l):
    maxr = [max(r) for r in l]
    cols = [[l[i][j] for i in xrange(n)] for j in xrange(m)]
    maxc = [max(c) for c in cols]
    for i in xrange(n):
        for j in xrange(m):
            if (l[i][j] != maxr[i] and l[i][j] != maxc[j]): return False
    return True

if __name__ == '__main__':
    T = int(stdin.readline())
    for caseNum in xrange(T):
        (n, m, l) = read_loan()
        res = solve(n, m, l)
        print 'Case #%d: %s' % (caseNum + 1, 'YES' if res else 'NO')