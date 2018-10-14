import sys
import math

def fits( x, r, c ):
    val = int( math.ceil(x/2.0) )
    squareFit = val <= r and val <= c
    lengthFit = x <= r or x <= c
    return squareFit and lengthFit
        

def solve( x, r, c ):
    if r*c%x == 0 and fits( x, r, c):
        if (x,r,c) == (4,4,2) or (x,r,c) == (4,2,4):
            return "RICHARD"
        return "GABRIEL"
    return "RICHARD"


with open(sys.argv[1]) as f:
    num_cases = int(f.readline().rstrip())
    case = 0
    while num_cases:
        num_cases -= 1
        case +=1
        x,r,c = [ int(x) for x in f.readline().rstrip().split()]
        #print 'Data: ', data
        print "Case #%d: %s" % (case, solve(x,r,c))
