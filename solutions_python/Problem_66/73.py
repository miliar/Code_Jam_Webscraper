import sys,collections
import os

def solve_unit(P, M):
    if all(m >= P for m in M):
        return 0
    assert P
    return 1+solve_unit(P-1, M[:2**(P-1)]) + solve_unit(P-1, M[2**(P-1):])

def solve(P, M, C):
    p = MixedIntegerLinearProgram(maximization=False)
    b = p.new_variable(dim=2)
    p.set_binary(b)
    p.set_objective(sum(sum(C[r,j]*b[r][j] for j in range(2**r)) for r in range(P)))
    for i in range(2**P):
        p.add_constraint( sum(sum(b[r][j] for j in range(2**r) if j* 2**(P-r)<=i<(j+1)* 2**(P-r)) for r in range(P)), min=P-M[i])
    return p.solve(solver='Coin')
    
#NAME = 'B-example'
NAME = 'B-small-attempt1'
#NAME = 'B-large'

BASEDIR = os.path.expanduser('~/Projects/Challenge/Google CodeJam/GCJ 2010 Round 2/%s')
inname  = BASEDIR % (NAME + '.in')
outname = BASEDIR % (NAME + '.out')

with open(inname) as fin:
    with open(outname,'w') as fout:
        num_cases = int(fin.readline())
        for case_idx in range(1,1+num_cases):
            P = int(fin.readline())
            M = map(int,fin.readline().split())
            assert len(M) == 2**P
            C = {}
            for r in range(P):
                X = map(int,fin.readline().split())
                assert len(X) == 2**(P-1-r)
                for j in range(2**(P-1-r)):
                    C[P-1-r,j] = X[j]
                    assert X[j]==1
                    
            answer = solve_unit(P,M)
            #answer = solve(P,M,C)
            print >> fout, "Case #%d: %d" % (case_idx, answer)
