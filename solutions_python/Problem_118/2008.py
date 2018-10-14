"""
    Problem C. Fair and square
"""
import sys
from math import sqrt, ceil, floor

def solve(A, B):
    result = 0
    lBound = int(ceil(sqrt(A)))
    uBound = int(floor(sqrt(B)))
    #sys.stdout.write('a %d b %d\n' % (lBound, uBound) )
    for x in range(lBound, uBound+1):
        if isPali(x):
            y = x * x
            if isPali(y):
                result = result + 1
    return str(result)

def isPali(n):
    if n > 0  and n < 10:
        return True
    strN = str(n)
    strR = ''.join(reversed(strN))
    if strN == strR:
        return True
    return False

if  __name__ == '__main__':
    T = int(raw_input()) 
    t = 0 
    while t < T:
        t = t+1
        (A,B) = raw_input().split()[:2]
        A = int(A)
        B = int(B)
        answer = solve(A, B)
        sys.stdout.write('Case #%d: %s\n' % (t, answer) )
