#!/usr/bin/python
from decimal import *
getcontext().prec = 5

def check(n, k):
    p = 0
    for i in n:
        if i > k[p]:
            p += 1
            continue
        else:
            return False
    return True

def test(n, k, caseNum, o):
    o.write('Case #' + caseNum + ': ')

    optNR = sorted(list(n), reverse=True)
    optKR = sorted(list(k), reverse=True)

    for i in n:
        for j in k:
            if j > i:
                k.remove(j)
                break
    wScore = len(k)

    while not check(optNR, optKR):
        optNR.pop()
        optKR.pop(0)

    oScore = len(optKR)
    o.write(str(oScore) + ' ' + str(wScore) + '\n')
    
f = open("/Users/tony/Downloads/D-large.in.txt")
i = int(f.readline())
o = open("a.out", 'w')

for t in xrange(0, i):
    a = f.readline()
    n = [Decimal(z) for z in f.readline().split()]
    k = [Decimal(z) for z in f.readline().split()]
    
    test(sorted(n), sorted(k), str(t + 1), o)