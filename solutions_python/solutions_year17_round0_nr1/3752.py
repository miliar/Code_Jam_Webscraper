#!/usr/bin/env sage

# import sys
# from sage.all import *

def string2vec(x):
    S = len(x)
    V = VectorSpace(GF(2), S)
    y = map(lambda c: 1 if c == '-' else 0, x)
    return V(y)

def makeMat(S,K):
    M = MatrixSpace(GF(2), S - K + 1, S)
    m = []
    for s in range(S - K + 1):
        a = [0] * S
        for i in range(s, s + K):
            a[i] = 1
        m.append(a)
        
    return M(m).transpose()

def determine(S, K):
    v = string2vec(S)
    S = len(S)
    M = makeMat(S, K)
    return M \ v

if __name__=='__main__':
    c = 0
    TOTAL = 0
    for line in sys.stdin:
        line = line.strip()

        if c > 0:
            line = line.split()
            try:
                soln = determine(line[0], int(line[1]))
                y = 0
                for z in soln:
                    if z == GF(2)(1):
                        y += 1
                print 'Case #%d: ' % c + str(y)
            except:
                print 'Case #%d: IMPOSSIBLE' % c
        else:
            TOTAL = int(line)

        if c == TOTAL:
            break

        c += 1

# vim: set ft=python
