import sys
import math
from decimal import Decimal
sys.setrecursionlimit(20000000)

surface = lambda (ri, hi): Decimal(2.0 * math.pi * ri**2 + 2.0 * math.pi * ri * hi)

def get_optimal_surface(n, k, pancakes, area=Decimal(0.0), depth=0):
    if depth == k:
        return area
    return max([get_optimal_surface(n-(i+1), k, pancakes[i+1:], area + surface(pancakes[i]) - Decimal(1.0 if depth==0 else 2.0) * Decimal(math.pi) * pancakes[i][0]**2, depth+1) for i in range(n-(k-depth)+1)])



t = int(raw_input())
for i in xrange(1, t + 1):
    n, k = [int(s) for s in raw_input().split(" ")]
    pancakes = []
    for j in range(n):
        ri, hi = [int(s) for s in raw_input().split(" ")]
        pancakes.append((ri, hi))
    pancakes = sorted(pancakes, reverse=True)
    print "Case #{}: {}".format(i, '{:.{}f}'.format(get_optimal_surface(n, k, pancakes), 9))