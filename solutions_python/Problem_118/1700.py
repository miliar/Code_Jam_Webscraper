import sys
import math

def ispalin(n):
    x, y = n, 0
    while x > 0:
        y = (y * 10) + (x % 10)
        x = x / 10
    return n == y

def isfsq(n):
    return ispalin(n) and ispalin(n*n)

def solve_old(a, b):
    #a, b = map(int, sys.stdin.readline().split())
    p = int(math.sqrt(a))
    q = int(math.sqrt(b))
    if p * p < a:
        p += 1
    if q * q > b:
        q -= 1
    c = 0
    for n in xrange(p, q+1):
        if isfsq(n):
            c += 1
            print n,
    return c

fsqs = [1,2,3,11,22,101,111,121,202,212,1001,1111,2002,10001,10101,10201,11011,11111,11211,20002,20102,100001,101101,110011,111111,200002,1000001,1001001,1002001,1010101,1011101,1012101,1100011,1101011,1102011,1110111,1111111,2000002,2001002]

def solve():
    a, b = map(int, sys.stdin.readline().split())
    c = 0
    for n in fsqs:
        if b >= n*n >= a:
            c += 1
    return c

T = int(sys.stdin.readline())
for i in range(T):
    print 'Case #{0}: {1}'.format(i+1, solve())

