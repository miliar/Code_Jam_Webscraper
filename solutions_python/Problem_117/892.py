def read_ints():
    return map(int, raw_input().split())

def read_str():
    return raw_input()

def row_ok(L, n, m):
    return all([L[n][i] <= L[n][m] for i in range(len(L[n]))])

def col_ok(L, n, m):
    return all([L[i][m] <= L[n][m] for i in range(len(L))])

def lawn():
    N, M = read_ints()
    L=[]
    for n in range(N):
        L.append(read_ints())
    for n in range(N):
        for m in range(M):
            if not row_ok(L, n, m) and not col_ok(L, n, m):
                return "NO"
    return "YES"

T=read_ints()[0]
for t in xrange(T):
    print "Case #%d: %s" %(t+1, lawn())

