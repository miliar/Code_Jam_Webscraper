import sys
import re
import os
import time
from itertools import *
from pprint import pprint


def can_separate(P, V, D, walk):
    if not P:
        return True

    x = -1e14
    for p, v in zip(P, V):
        new_x = max(x+D, p-walk) + D*(v-1)
        if new_x > p+walk:
            return False
        x = new_x

    return True


def solve():
    C, D = map(int, next(fin).split())
    P = []
    V = []
    for _ in range(C):
        p, v = map(int, next(fin).split())
        P.append(p)
        V.append(v)

    assert sorted(P) == P

    left = 0.0
    right = 1e12
    eps = 1e-7

    #print P, V, D, can_separate(P, V, D, 2.6)
    #return

    while right-left > eps and right-left > left*eps:
        mid = 0.5*(left+right)
        if can_separate(P, V, D, mid):
            right = mid
        else:
            left = mid


    print>>fout, mid


if len(sys.argv) != 2:
    print 'specify input file'
    exit()

startTime = time.clock()

fin = open(sys.argv[1])
fout = open(os.path.splitext(sys.argv[1])[0]+'.out', 'w')

numCases = int(next(fin))
for caseNo in range(numCases):
    print '\b'*10, 100*caseNo/numCases, '%',
    print>>fout, 'Case #%s:'%(caseNo+1),
    solve()

try:
    next(fin)
    assert False, 'not all lines are processed'
except StopIteration:
    pass

fin.close()
fout.close()

print '\b'*10+'it took %.1fs'%(time.clock()-startTime)