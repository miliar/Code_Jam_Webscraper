#!/usr/bin/python

# google code jam - c.durr - 2013
# Lawnmower
# ad-hoc (I hope)

    
t = int(raw_input())

def solve(A, n,m):
    r = [max(Ai) for Ai in A]
    c = [max(A[i][j] for i in range(n)) for j in range(m)]

    for i in range(n):
        for j in range(m):
            if A[i][j] < r[i] and A[i][j] < c[j]:
                return "NO"
    return "YES"
    
def readInts(): return [int(i) for i in raw_input().split()]
for test in range(t):
    n,m = readInts()
    A = []
    for i in range(n):
        A.append(readInts())

    print 'Case #%d:' % (test+1), solve(A, n,m)
