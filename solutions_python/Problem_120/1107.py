import sys
import math

def solve():
    r, t = map(int, sys.stdin.readline().split())
    b = 2 * r - 1
    n = (math.sqrt(b * b + 8 * t) - b) * 0.25
    n = int(n)
    if n * (2 * n + b) > t:
        return n - 1
    return n

for i in range(int(sys.stdin.readline())):
    print 'Case #{0}: {1}'.format(i+1, solve())

