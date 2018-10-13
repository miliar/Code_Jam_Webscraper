def calc(M, m, n):
    S = [[None for j in xrange(n)] for i in xrange(m)]
    indices = sorted([(i, j) for i in xrange(m) for j in xrange(n)],
        cmp = lambda a, b: cmp(M[a[0]][a[1]], M[b[0]][b[1]]), reverse=True)

    marks = {}
    mark = 1
    for (i, j) in indices:
        if not S[i][j]:
            marks[mark] = mark
            marks[mark] = marks[fill(M, S, m, n, i, j, mark)]
            mark += 1
            
    char = 'a'
    chars = {}
    for i in xrange(m):
        for j in xrange(n):
            if S[i][j] in marks:
                if not marks[S[i][j]] in chars:
                    chars[marks[S[i][j]]] = char
                    char = chr(ord(char) + 1)
                S[i][j] = chars[marks[S[i][j]]]
    
    return S

def fill(M, S, m, n, i, j, mark):
    assert not S[i][j]
    while i >= 0 and j >= 0:
#        print i, j, S[i][j], '->',
        if S[i][j]: 
#            print 'old mark', S[i][j]
            return S[i][j]
        S[i][j] = mark
        i, j = flow_down(M, S, m, n, i, j)

#    print 'new mark', mark
    return mark

def flow_down(M, S, m, n, i, j):
    a = []
    if i > 0: a.append((i - 1, j))
    if j > 0: a.append((i, j - 1))
    if j < n - 1: a.append((i, j + 1))
    if i < m - 1: a.append((i + 1, j))
    a = [(ii, jj) for (ii, jj) in a if M[ii][jj] < M[i][j]]
    if not a:
        return -1, -1
    min_val = min(M[ii][jj] for (ii, jj) in a)
    a = [(ii, jj) for (ii, jj) in a if M[ii][jj] == min_val]
    return a[0]

T = input()
for t in xrange(T):
    m, n = [int(s) for s in raw_input().split()]
    M = []
    for i in xrange(m):
        M.append([int(s) for s in raw_input().split()])
    
    print 'Case #%i:' % (t + 1)
    S = calc(M, m, n)
    for row in S:
        print ' '.join(row)
