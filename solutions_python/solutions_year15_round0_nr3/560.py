mx = {}
mx["i"] = [[0,1,0,0],[-1,0,0,0],[0,0,0,-1],[0,0,1,0]]
mx["j"] = [[0,0,1,0],[0,0,0,1],[-1,0,0,0],[0,-1,0,0]]
mx["k"] = [[0,0,0,1],[0,0,-1,0],[0,1,0,0],[-1,0,0,0]]

mxorig = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
mxneg = [[-1,0,0,0],[0,-1,0,0],[0,0,-1,0],[0,0,0,-1]]

def mxclone(mx):
    return [[el for el in row] for row in mx]

def mxmult(mx1, mx2):
    return [[sum(mx1[i][j] * mx2[j][k] for j in xrange(4)) for k in xrange(4)] for i in xrange(4)]

def mxpower(mx, n):
    k = mxorig
    v = mx
    j = 1
    while j <= n:
        if (n & j):
            k = mxmult(k, v)
        j = j << 1
        v = mxmult(v, v)
    return k

def verify(X, seq):
    a = mxorig
    for i in seq:
        a = mxmult(a,mx[i])
    a = mxpower(a, X)
    if a != mxneg:
        return False
    a = mxorig
    timesThrough = 0
    lettersThrough = 0
    while (timesThrough < min(4,X)) and a != mx["i"]:
        a = mxmult(a,mx[seq[lettersThrough]])
        lettersThrough += 1
        if lettersThrough == len(seq):
            lettersThrough = 0
            timesThrough += 1
    if timesThrough == min(4, X):
        return False
    a = mxorig
    timesThrough2 = 0
    lettersThrough2 = 0
    while (timesThrough2 < min(4,X)) and a != mx["k"]:
        a = mxmult(mx[seq[-(1+lettersThrough2)]],a)
        lettersThrough2 += 1
        if lettersThrough2 == len(seq):
            lettersThrough2 = 0
            timesThrough2 += 1
    if timesThrough2 == min(4, X):
        return False
    timesThrough += timesThrough2
    lettersThrough += lettersThrough2
    if lettersThrough >= len(seq):
        lettersThrough -= len(seq)
        timesThrough += 1
    return timesThrough < X

from sys import stdin

for cn in xrange(1,1+int(stdin.readline())):
    (v,X) = tuple(int(z) for z in stdin.readline().split())
    seq = stdin.readline().strip()
    print "Case #%d: %s" % (cn, "YES" if verify(X, seq) else "NO")
