#
# problemA.py
#

# Import
import sys
sys.dont_write_bytecode = True
sys.path.append('../')
from gcj import Problem
from gcj.utils import Timer

# Parser
def parser(fin):
    [S,K] = fin.readWords()
    return list(S),int(K)

# Solver
def solver(data):
    S,K = data
    count = 0
    print len(S)
    while True:
        if len(S) == K and not (S == ['+']*K or S == ['-']*K):
            return 'IMPOSSIBLE'
        if S[0] == '+':
            S = S[1:]
            if len(S) == 0:
                return count
        else:
            count += 1
            for i in xrange(K):
                S[i] = '+' if S[i] == '-' else '-'

# Main
if __name__ == '__main__':
    with Timer('Problem A'):
        Problem(parser, solver).run()
