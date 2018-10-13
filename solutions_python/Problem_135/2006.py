#
# problemA.py
#

# Import
from gcj import Problem
from gcj.utils import Timer, getFunctions

# Parser
def parser(fin):
    ans1 = fin.readInt()
    arr1 = []
    for _ in xrange(4):
        arr1.append(fin.readInts())
    ans2 = fin.readInt()
    arr2 = []
    for _ in xrange(4):
        arr2.append(fin.readInts())
    
    return [arr1[ans1-1], arr2[ans2-1]]
        

# Solver
def intersect(a,b):
    return list(set(a) & set(b))

def solver(data):
    a,b = data
    i = intersect(a,b)
    l = len(i)
    if l == 1:
        return i[0]
    elif l == 0:
        return 'Volunteer cheated!'
    else:
        return 'Bad magician!'
    return None

# Main
if __name__ == '__main__':
    with Timer('Problem A'):
        Problem(parser, solver, getFunctions(globals())).run()
