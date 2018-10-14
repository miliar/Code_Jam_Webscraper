import sys

def solve():
    n, m = map(int, sys.stdin.readline().split())
    A = [sys.stdin.readline().split() for i in range(1, n+1)]
    #print n, m
    #for line in A:
        #print ' '.join(line)
    for i in range(n):
        for j in range(m):
            if any(A[i][j] < A[i][k] for k in range(m)) and any(A[i][j] < A[k][j] for k in range(n)):
                return 'NO'
    return 'YES'

T = int(sys.stdin.readline())
for i in range(T):
    print 'Case #{0}: {1}'.format(i+1, solve())

