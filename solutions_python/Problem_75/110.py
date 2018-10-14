import sys
import re
import os
import time
from itertools import *
from pprint import pprint


def solve():
    p = iter(next(fin).split())
    
    combination_rules = list(islice(p, int(next(p))))
    elimination_rules = list(islice(p, int(next(p))))

    length = int(next(p))
    invokes = next(p)
    assert len(invokes) == length

    stack = []
    for i in invokes:
        stack.append(i)
        if len(stack) >= 2:
            x = stack[-2]+stack[-1]
            for c in combination_rules:
                if c.startswith(x) or c.startswith(x[::-1]):
                    stack.pop()
                    stack.pop()
                    stack.append(c[-1])
                    break
            else:
                for e in elimination_rules:
                    if e[0] in stack and e[1] in stack:
                        stack = []
                        break
                        

    print>>fout, '[{0}]'.format(', '.join(stack))


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