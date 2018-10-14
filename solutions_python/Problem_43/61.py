import sys
import re
import os
import time
from itertools import *
from pprint import pprint

if len(sys.argv) != 2:
    print 'specify input file'
    exit()

startTime = time.clock()

fin = open(sys.argv[1])
fout = open(os.path.splitext(sys.argv[1])[0]+'.out','w')

def symbols(n):
    s = set()
    m = 0
    for i in n.strip():
        if not i in s:
            s.add(i)
            m = m+1
    return s,m

def minint(n):
    s, base = symbols(n)
    if base==1:
        base = 2
    vals = {}
    vals[n[0]]=1
    num = 0
    last = 1
    for x in n.strip():
        print "working with",x
        if not vals.has_key(x):
            if last == 1:
                last = 0
            elif last == 0:
                last = 2
            else:
                last = last+1
            vals[x] = last
        num = num*base + vals[x]
    return num 

def solve():
    n = str(fin.readline())
    print>>fout,minint(n)


numCases = int(fin.readline())
for caseNo in range(numCases):
    print '\b'*10,100*caseNo/numCases,'%',
    print>>fout, 'Case #%s:'%(caseNo+1),
    solve()

fin.close()
fout.close()

print '\b'*10+'it took %.1fs'%(time.clock()-startTime)

