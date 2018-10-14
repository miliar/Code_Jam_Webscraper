import sys
import re
import os
import time
from itertools import *
from pprint import pprint


def solve():
    length = int(next(fin))
    items = map(int, next(fin).split())
    assert sorted(items) == range(1, length+1)

    not_in_place = sum(1 for i, x in enumerate(items) if i+1 != x)
    print>>fout, float(not_in_place)


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

fin.close()
fout.close()

print '\b'*10+'it took %.1fs'%(time.clock()-startTime)