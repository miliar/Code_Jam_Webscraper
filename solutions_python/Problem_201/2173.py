#!/usr/bin/python3
import sys
import math
from decimal import *

def scale(N, K):
    """Compute the scale of the problem, it gets worse as the 
    toilets fill up."""
    return Decimal(0.5**(1+math.floor(math.log2(K)))) * Decimal(N - K)

def show(N, K):
    print("N: %s, K: %s" % (N, K))
    for i in range(1, N+1):
        print(scale(N, i))
        
def solve(N, K):
    fraction = scale(N, K)
    lower_bound = math.floor(fraction)
    if (fraction - lower_bound) >= 0.5:
        upper_bound = lower_bound + 1
    else:
        upper_bound = lower_bound

    return (upper_bound, lower_bound)
    
def test():
    num_tests = None
    i = 1
    for line in sys.stdin:
        if not num_tests:
            num_tests = int(line.strip())
            continue
        N, K = map(int, line.strip().split(" "))
#        show(N, K)
        upper, lower = solve(N, K)
        print("Case #%s: %s %s" % (i, upper, lower))
        i = i + 1
    
if __name__ == "__main__":
    test()
