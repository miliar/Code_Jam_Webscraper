
import sys
from math import *
from sage.all import *
#from sage.rings.fast_arith import prime_range
tol = 0.00000000001

nCases = int(sys.stdin.readline())
for caseN in range(1, nCases+1):
    n = int(sys.stdin.readline())
    sqrtN = floor(sqrt(float(n))+tol)
    ps = prime_range( sqrtN+1)
    result = sum((floor(log(float(n), p)+tol) - 1 for p in ps))
    if(n > 1):
        result = result + 1
    print "Case #" + str(caseN) + ": " + str(result)
