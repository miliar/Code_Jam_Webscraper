#!/usr/bin/env python
import sys
import scipy as S

if __name__ == '__main__':
    #read input
    inp = open(sys.argv[1])
    out = open('scalar.out','w')
    n_cases = int(inp.readline().strip())
    for n in range(n_cases):
        #parsing
        n_dig = inp.readline().strip().split()
        a = map(int, inp.readline().strip().split())
        b = map(int, inp.readline().strip().split())
        a.sort()
        b.sort()
        b.reverse()
        print >> out, 'Case #%i: %i' % (n+1, (S.array(a)*S.array(b)).sum())
    out.close()

