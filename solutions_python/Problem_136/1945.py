#
# problemB.py
#

# Import
from gcj import Problem
from gcj.utils import Timer, getFunctions

# Parser
def parser(fin):
    data = fin.readFloats()
    return data

# Solver

def solver(data):

    C,F,X = data
    P = 2.0
    T = 0.0
    M = 0.0

    while True:
        if X/P < (C/P + X/(P+F)):
            return '{0:.7f}'.format((T + X/P))
        T += C/P
        P += F

# Main
if __name__ == '__main__':
    with Timer('Problem B'):
        Problem(parser, solver, getFunctions(globals())).run()
