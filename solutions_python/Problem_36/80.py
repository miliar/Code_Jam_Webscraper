import psyco
psyco.full()

import sys
import re
import os
from pprint import pprint

if len(sys.argv) != 2:
    print 'specify input file'
    exit()
    
with open(sys.argv[1]) as fin:
    lines = fin.readlines()

N, = map(int,lines[0].split())

cases = lines[1:1+N]

fout = open(os.path.splitext(sys.argv[1])[0]+'.out','wt')

s = 'welcome to code jam'
M = 10000
    
for caseNo,case in enumerate(cases):
    print '\b'*10,100*caseNo/len(cases),'%',

    x = [[1]*(len(case)+1)]
    for i in range(len(s)):
        x.append([None]*(len(case)+1))
        x[-1][0] = 0
        for j in range(len(case)):
            if s[i] != case[j]:
                x[-1][j+1] = x[-1][j]
            else:
                x[-1][j+1] = (x[-1][j]+x[-2][j])%M
    print>>fout, 'Case #%s: %04d'%(caseNo+1,x[-1][-1])
            
fout.close()    
print

