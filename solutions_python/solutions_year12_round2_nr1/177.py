#!/usr/bin/python

import re
from sys import stdin

def p(a, prom, X):
    return (2.*prom - a) / float(X)

def magia(A, X):
    N = len(A)
    d = (X + sum(A)) / float(N)
    result = []
    for a in A:
        p = (d - a)/ float(X)
        result.append(p)
    if all([i >= 0 for i in result]):
        return result
    else:
        ceros = [False] * N
        for i in reversed(range(len(result))):
            if result[i] < 0:
                A[:] = A[:i] + A[i+1:]
                ceros[i] = True
        subresult = magia(A, X)
        i = 0
        j = 0
        while i < N:
            if ceros[i]:
                result[i] = 0
            else:
                result[i] = subresult[j]
                j += 1
            i += 1
        return result


if True:
    ncases = int(stdin.readline().strip())

    for i, line in enumerate(stdin.xreadlines()):
        line = re.split(' +', line.strip())
        N, A = int(line[0]), [int(a) for a in line[1:]]
        X = sum(A)
        sol = magia(A, X)
        answer = "Case #%i: " % (i+1)
        for s in sol:
            #answer += "%.6f " % (100*p(a, X, N))
            answer += "%.7f " % (100*s)
        print(answer[:-1])
