
def split_grids(N, A):
    B = [['.'] * N for i in xrange(N)]
    for x in A:
        B[x[1] - 1][x[2] - 1] = x[0]
    r1 = [[int(B[i][j] in '+o') for j in xrange(N)] for i in xrange(N)]
    r2 = [[int(B[i][j] in 'xo') for j in xrange(N)] for i in xrange(N)]
    return r1, r2

def iter_diag(N, p, rev=False):
    x, y = max(p - N + 1, 0), max(N - p - 1, 0)
    while x < N and y < N:
        yield (x, y) if not rev else (N - y - 1, x)
        x, y = x + 1, y + 1

def iter_spec(N, odd=True):
    for i in xrange(N):
        yield i
        if not odd or i != N - 1:
            yield 2 * N - i - odd - 1

def solve_P(N, A):
    res = [x[:] for x in A]
    for col in iter_spec(N):
        diag = list(iter_diag(N, col))
        if any(res[y][x] for x, y in diag):
            continue
        M = len(diag)
        row = N - M
        for i in iter_spec((M + 1) / 2, M % 2):
            diag_rev = list(iter_diag(N, row + i * 2, rev=True))
            if not any(res[y][x] for x, y in diag_rev):
                x, y = diag[i]
                res[y][x] = 1
                break
    return res

def solve_X(N, A):
    cols = set(j for i in xrange(N) for j in xrange(N) if A[i][j])
    available = [i for i in xrange(N) if i not in cols]
    res = []
    for line in A:
        if not sum(line):
            line = [0] * N
            line[available.pop()] = 1
        res.append(line)
    return res

T = int(raw_input())
for t in xrange(T):
    N, M = map(int, raw_input().split(' '))
    A = []
    for i in xrange(M):
        v, r, c = raw_input().split(' ')
        A.append((v, int(r), int(c)))
    g1, g2 = split_grids(N, A)
    g1_new = solve_P(N, g1)
    g2_new = solve_X(N, g2)
    pts, res = 0, []
    for i in xrange(N):
        for j in xrange(N):
            v1, v2 = g1_new[i][j], g2_new[i][j]
            if v1 + v2 != g1[i][j] + g2[i][j]:
                res.append(('o' if v1 and v2 else ('+' if v1 else 'x'), i + 1, j + 1))
            pts += v1 + v2
    print 'Case #%d: %s %s' % (t + 1, pts, len(res))
    for item in res:
        print ' '.join(map(str, item))
