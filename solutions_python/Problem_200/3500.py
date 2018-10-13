#
# problemB.py
#

# Import
import sys
sys.dont_write_bytecode = True
sys.path.append('../')
from gcj import Problem
from gcj.utils import Timer

def isTidy(n):
    n = str(n)
    return n == ''.join(sorted(list(n)))

# Parser
def parser(fin):
    return fin.readInt()

def solver(data):
    N = data
    while N > 0:
        if isTidy(N):
            return N
        N -= 1

# Main
if __name__ == '__main__':
    with Timer('Problem B'):
        Problem(parser, solver).run()
