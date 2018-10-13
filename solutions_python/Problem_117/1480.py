import sys

N = int(sys.stdin.readline())

def handlecase(case):
    matrix = []
    n, m = sys.stdin.readline().strip().split()
    n, m = int(n), int(m)
    for i in range(n):
        l = sys.stdin.readline().rstrip()
        matrix.append(l.replace(' ', ''))
    lawned = []
    for row in range(n):
        h = max(int(c) for c in matrix[row])
        lawned.append(str(h)*m)
    for col in range(m):
        l = ''.join([lawned[i][col] for i in range(n)])
        lneeded = ''.join([matrix[i][col] for i in range(n)])
        if l != lneeded:
            h = str(min(int(matrix[i][col]) for i in range(n)))
            for i in range(n):
                news = list(lawned[i])
                news[col] = h
                lawned[i] = ''.join(news)
    if lawned != matrix:
        print 'Case #%d: NO' % case
    else:
        print 'Case #%d: YES' % case

for x in range(N):
    handlecase(x+1)
