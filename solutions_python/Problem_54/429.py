import sys
import re
import os
import time
from itertools import *
from pprint import pprint

from fractions import gcd


if len(sys.argv) != 2:
    print 'specify input file'
    exit()

startTime = time.clock()

fin = open(sys.argv[1])
fout = open(os.path.splitext(sys.argv[1])[0]+'.out','w')

def solve():
    t = map(int,next(fin).split())
    t.pop(0)
    t.sort()

    d = reduce(gcd,[x-t[0] for x in t[1:]])

    print>>fout, (-t[-1])%d

numCases = int(next(fin))
for caseNo in range(numCases):
    print '\b'*10,100*caseNo/numCases,'%',
    print>>fout, 'Case #%s:'%(caseNo+1),
    solve()

fin.close()
fout.close()

print '\b'*10+'it took %.1fs'%(time.clock()-startTime)