import sys, math

def input_case():
    case = {}
    f.readline()
    case['x1'] = f.readline().split()
    case['x1'] = [int(x) for x in case['x1']]
    case['x2'] = f.readline().split()
    case['x2'] = [int(x) for x in case['x2']]
    return case       

def solve_case(case):
    x1 = case['x1']
    x2 = case['x2']
    x1.sort()
    x2.sort()
    x2.reverse()
    return vprod(x1, x2)
    
    
def vprod(x1, x2):
    prod = 0
    for i in xrange(len(x1)):
        prod += x1[i] * x2[i]
    
    return prod
    

f = open(sys.argv[-1], 'r')
num_cases = int(f.readline())

for i in xrange(int(num_cases)):
    case = input_case()
    print 'Case #%u: %d' % (i + 1, solve_case(case))

f.close()