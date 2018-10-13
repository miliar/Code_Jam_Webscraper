#!/usr/bin/python

import sys

# Global variable
A = []

def findMaxCol (j):
    return max([row[j] for row in A])

def replaceRow (r,M):
    for j in xrange(M):
        A[r][j] = findMaxCol(j)

def replaceColumn (c,N):
    for i in xrange(N):
        A[i][c] = max(A[i])

def findMin (N,M):
    m = 1000
    for i in xrange(N):
        for j in xrange(M):
            if A[i][j] < m:
                (x,y)=(i,j)
                m = A[i][j]
    return (x,y,m)

def findMax (N,M):
    m = -1
    for i in xrange(N):
        for j in xrange(M):
            if A[i][j] > m:
                m = A[i][j]
    return m

def checkCol (j, x, N):
    for i in xrange(N):
        if A[i][j] != x:
            return False
    return True

T=int(sys.stdin.readline().strip())
for t in xrange(1,T+1):
    A = []
    (N,M)=map(int,sys.stdin.readline().strip().split())
    for i in xrange(N):
        A.append(map(int,sys.stdin.readline().strip().split()))
    maximo = findMax(N,M)
    (x,y,minimo) = findMin(N,M)
    possible = True
    while maximo != minimo:
        #comprobamos fila
        if A[x] == [minimo]*M:
            replaceRow(x,M)
        #comprobamos columna
        elif checkCol (y, minimo, N):
            replaceColumn(y,N)
        #si no, es imposible
        else:
            print "Case #" + str(t) + ": NO"
            possible = False
            break
        (x,y,minimo) = findMin(N,M)
    if possible:
        print "Case #" + str(t) + ": YES"
