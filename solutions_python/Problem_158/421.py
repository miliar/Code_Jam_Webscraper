import pdb
import copy
from sets import Set as set

def solve_case(X, R, C):
    R, C = min(R,C), max(R,C)
    if X == 1:
        return "GABRIEL"
    
    if X == 2:
        if R%2 == 0 or C%2 == 0:
            return "GABRIEL"
        else:
            return "RICHARD"
    
    if X == 3:
        if C < 3:
            return "RICHARD"
        if C == 3:
            if R == 1:
                return "RICHARD"
            else:
                return "GABRIEL"
        if C == 4:
            if R == 1:
                return "RICHARD"
            if R == 2:
                return "RICHARD"
            if R == 3:
                return "GABRIEL"
            if R == 4:
                return "RICHARD"
    
    if X == 4:
        if C < 4:
            return "RICHARD"
        if R == 1:
            return "RICHARD"
        if R == 2:
            return "RICHARD"
        if R == 3:
            return "GABRIEL"
        if R == 4:
            return "GABRIEL"
        
    pdb.set_trace()
    raise Exception("all cases exhausted")
            
        
        
    

with open('D-small-attempt0.in') as fin, \
open('D-small-attempt0.out', 'w') as fout:
    NumCases = int(fin.next())
    for case in xrange(1, NumCases+1):
        line = fin.next().strip().split(' ')
        print line
        X, R, C = tuple([int(x) for x in line])
        print X, R, C
        fout.write("Case #%d: " % case + str(solve_case(X, R, C)) + '\n')
        # print line

