T = int(raw_input())
def rotated(b):
    N = len(b)
    c = []
    for i in xrange(N):
        row = []
        for j in xrange(N):
            row.append('.')
        c.append(row)
      #  c.append('.'*N)
    for j in xrange(N):
        row = b[j]
        while '.' in row:
            row.remove('.')
        for i in xrange(1, len(row)+1):
            currrow = c[-i]
            currrow[-j-1] = row[-i]
    return c
def wins(b, col, K):
    N = len(b)
    for i in xrange(N):
        for j in xrange(N):
            if b[i][j] == col:
                for dir in [(0, 1), (1, 0), (1, 1), (1, -1)]:
                    ilim = i + (K-1) * dir[0]
                    jlim = j + (K-1) * dir[1]
                    if ilim in range(N) and jlim in range(N):
                        if all(b[i + delta*dir[0]][j + delta*dir[1]] == col for delta in range(K)): return True
    return False
def result(b, K):
    B = wins(b, 'B', K)
    R = wins(b, 'R', K)
    if B and R:
        return "Both"
    elif B:
        return "Blue"
    elif R:
        return "Red"
    else:
        return "Neither"
for case in xrange(1, T + 1):
    N, K = map(int, raw_input().split())
    b = []
    for i in xrange(N):
        row = raw_input().strip()
        b.append([c for c in row])
    x = rotated(b)
    res = result(x, K) 
    print "Case #%s: %s" % (case, res)
