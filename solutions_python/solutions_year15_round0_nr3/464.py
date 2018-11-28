import pdb
import copy
from sets import Set as set

def op(x, y):
    if type(x) != tuple:
        x = (1, x)
    if type(y) != tuple:
        y = (1, y)
        
    sign = x[0]*y[0]
    
    if x[1] == 1:
        return (sign, y[1])
    if y[1] == 1:
        return (sign, x[1])
    
    if x[1] == y[1]:
        sign *= -1
        return (sign, 1)
    
    if x[1] > y[1]:
        sign *= -1
        temp = x
        x = y
        y = temp
    

    
    if x[1] == 'i' and y[1] == 'j':
        return (sign, 'k')
    if x[1] == 'i' and y[1] == 'k':
        return (-sign, 'j')
    if x[1] == 'j' and y[1] == 'k':
        return (sign, 'i')

    raise Exception('All cases exhausted')
    

def solve_case(ln):
    # pdb.set_trace()
    product =  reduce(op, ln)
    print product
    
    if product != (-1, 1):
        return "NO"
    L = len(ln)
    
    running_product = (1,1)
    split1 = -1
    
    for i in xrange(L):
        running_product = op(running_product, ln[i])
        if running_product == (1, 'i'):
            split1 = i
            break
    
    if split1 == -1:
        return "NO"
    
    split2 = 0
    running_product = (1,1)
    
    for i in xrange(L):
        running_product = op(ln[L - 1 - i], running_product)
        if running_product == (1, 'k'):
            split2 = L -1 - i
            break
    
    if split2 == 0:
        return "NO"
    
    if split2 - split1 < 2:
        return "NO"
    
    return "YES"

with open('C-small-attempt0.in') as fin, \
open('C-small-attempt0.out', 'w') as fout:
    case = 0
    NumCases = int(fin.next())
    for case in xrange(1, NumCases+1):
        line = fin.next().strip().split(' ')
        L, X = int(line[0]), int(line[1])
        print L, X
        line = fin.next().strip()
        line = list(line)*X
        fout.write("Case #%d: " % case + str(solve_case(line)) + '\n')
        # print line

