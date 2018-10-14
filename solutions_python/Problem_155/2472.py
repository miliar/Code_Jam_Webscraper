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
    A = fin.readWords()
    return A[1]

# Solver
def solver(data):
    audience = data
    friends = 0
    shyness = 0
    for s,a in enumerate(audience):
        a = int(a)
        if a > 0:
            if shyness < s:
                friends += (s - shyness)
                shyness = s
            shyness += a    
        
    return friends

# Main
if __name__ == '__main__':
    with Timer('Problem A'):
        Problem(parser, solver).run()
