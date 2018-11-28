#!/usr/bin/python
import string
res = None
b = 0
def N(m,i,j):
    if i==0: return m[i][j]+1
    return m[i-1][j]
def S(m,i,j):
    if i==len(m)-1: return m[i][j]+1
    return m[i+1][j]
def W(m,i,j):
    if j==0: return m[i][j]+1
    return m[i][j-1]
def E(m,i,j):
    if j==len(m[0])-1: return m[i][j]+1
    return m[i][j+1]    
def getBasin(m,i,j):
    global b
    if res[i][j] != '':
        return res[i][j]
    l = m[i][j]
    ll = min(N(m,i,j),S(m,i,j),W(m,i,j),E(m,i,j))
    if ll>=l:
        res[i][j]=string.lowercase[b]
        b+=1
    elif N(m,i,j)==ll:
        res[i][j] = getBasin(m,i-1,j)
    elif W(m,i,j)==ll:
        res[i][j] = getBasin(m,i,j-1)
    elif E(m,i,j)==ll:
        res[i][j] = getBasin(m,i,j+1)
    elif S(m,i,j)==ll:
        res[i][j] = getBasin(m,i+1,j)
    return res[i][j]
    
def solve(m,h,w):
    for i in xrange(h):
        for j in xrange(w):
            res[i][j] = getBasin(m,i,j)
if __name__ == "__main__":
    import sys
    n = int(sys.stdin.readline())
    for i in xrange(n):
        (h,w) = map(int,sys.stdin.readline().split())
        m = []
        b = 0
        res = []
        for j in xrange(h):
            res.append(['']*w)
            m.append(map(int,sys.stdin.readline().strip().split()))
        solve(m,h,w)
        print "Case #%d:" %(i+1,)
        for j in xrange(h):
            print ' '.join(res[j])

