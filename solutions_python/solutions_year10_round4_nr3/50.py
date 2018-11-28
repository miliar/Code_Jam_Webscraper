import sys,collections
import os

def advance(state):
    # state is a dictionary mapping row index to live intervals
    res = {}
    for r,lst in state.iteritems():
        tmp = []
        for x1,x2 in lst:
            Z = state.get(r-1,())
            u = x1   if any(a<=x1  <=b for a,b in Z) else x1+1
            v = x2+1 if any(a<=x2+1<=b for a,b in Z) else x2
            if tmp and tmp[-1][1] == u-1:
                tmp[-1][1] = v
            else:
                if u<=v: tmp.append([u,v])
        if tmp: res[r] = tmp
    return res

#NAME = 'C-example'
NAME = 'C-small-attempt1'
#NAME = 'C-large'

BASEDIR = os.path.expanduser('~/Projects/Challenge/Google CodeJam/GCJ 2010 Round 2/%s')
inname  = BASEDIR % (NAME + '.in')
outname = BASEDIR % (NAME + '.out')

with open(inname) as fin:
    with open(outname,'w') as fout:
        num_cases = int(fin.readline())
        for case_idx in range(1,1+num_cases):
            R = int(fin.readline())
            state = {}
            for r in range(R):
                X1,Y1,X2,Y2 = map(int,fin.readline().split())
                assert X1 <= X2 and Y1 <= Y2
                for y in range(Y1,Y2+1): state.setdefault(y,[]).append((X1,X2))
            
            for answer in range(1,100000):
                state = advance(state)
                if not state: break

            print answer               
            print >> fout, "Case #%d: %d" % (case_idx, answer)
