def checkrange(A, x, y, b, c):
    for i in range(x, y+1):
        if A[i][b] != '?' and A[i][b] != c:
            return False
    return True
    
def expand(A, i, j, n, m):
    x = y = i
    a = b = j
    while x > 0 and (A[x-1][j] == '?' or A[x-1][j] == A[i][j]):
        x -= 1
    while y+1 < n and (A[y+1][j] == '?' or A[y+1][j] == A[i][j]):
        y += 1
    while a > 0 and checkrange(A, x, y, a-1, A[i][j]) == True:
        a -= 1
    while b+1 < m and checkrange(A, x, y, b+1, A[i][j]) == True:
        b += 1
    for ii in range(x, y+1):
        for jj in range(a, b+1):
            A[ii][jj] = A[i][j]

def expand1(A, i, j, n, log):
    x = y = i
    while x > 0 and (A[x-1][j] == '?' or A[x-1][j] == A[i][j]):
        x -= 1
    while y+1 < n and (A[y+1][j] == '?' or A[y+1][j] == A[i][j]):
        y += 1
    log[A[i][j]] = [x, y, j]
    for ii in range(x, y+1):
        A[ii][j] = A[i][j]
    return log

def expand2(A, x, y, j, c):
    a = b = j
    while a > 0 and checkrange(A, x, y, a-1, c) == True:
        a -= 1
    while b+1 < m and checkrange(A, x, y, b+1, c) == True:
        b += 1
    for ii in range(x, y+1):
        for jj in range(a, b+1):
            A[ii][jj] = c

def solve(A, n, m):
    expanded = set([])
    log = {}
    for i in range(n):
        for j in range(m):
            if A[i][j] != '?' and A[i][j] not in expanded:
                #expand(A, i, j, n, m)
                #expanded.add(A[i][j])
                expand1(A, i, j, n, log)
    for c in log:
        l = log[c][2]
        x = log[c][0]
        y = log[c][1]
        expand2(A, x, y, l, A[x][l])

    return A

def check(A, B, n, m):
    for i in range(n):
        for j in range(m):
            if B[i][j] == '?':
                return False
            if A[i][j] != '?' and A[i][j] != B[i][j]:
                return False
    return True

T = int(input())
for I in range(T):
    line = input().split()
    n = int(line[0])
    m = int(line[1])
    A = [['' for i in range(m)] for j in range(n)]
    for i in range(n):
        line = input()
        for j in range(m):
            A[i][j] = line[j]
    print('Case #%d:' % (I+1))
    B = solve(A, n, m)
    for i in range(n):
        print(''.join(B[i]))
    if check(A, B, n, m) == False:
        print('False')
