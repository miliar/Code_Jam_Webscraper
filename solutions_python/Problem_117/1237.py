import math, sys

fin = open('B-large.in', 'r')
sys.stdout = open('B-large.out', 'w')

T = int(fin.readline())
for t in range(1, T+1):
    N, M = (int(x) for x in fin.readline().split(' '))
    max_r = [0 for i in range(N)]
    max_c = [0 for i in range(M)]
    table = [[] for i in range(N)]
    result = 'YES'
    for r in range(N):
        table[r] = [int(x) for x in fin.readline()[:-1].split(' ')]
        max_r[r] = max(table[r])
    for c in range(M):
        mx = 0
        for r in range(N):
            mx = max(mx, table[r][c])
        max_c[c] = mx
    for r in range(N):
        for c in range(M):
            if table[r][c] < max_r[r] and table[r][c] < max_c[c]:
                result = 'NO'
    print('Case #' + str(t) + ': ' + result)
fin.close()
temp = sys.stdout
temp.close()
