from sortedcontainers import SortedList
from math import ceil

def gcd(a, b, res):
    if a == b:
        return res * a
    elif (a % 2 == 0) and (b % 2 == 0):
        return gcd(a // 2, b // 2, 2 * res)
    elif (a % 2 == 0):
        return gcd(a // 2, b, res)
    elif (b % 2 == 0):
        return gcd(a, b // 2, res)
    elif a > b:
        return gcd(a - b, b, res)
    else:
        return gcd(a, b - a, res)

def getMaxMin(n):
    max = ceil((n-1)/2)
    min = (n-1)//2
    return max, min

cases = int(input()) 
for c in range(1, cases + 1):
    N, K = [int(s) for s in input().split()]
    if K/N > 0.525:
        max, min = (0, 0)        
    else:
        # d = gcd(N, K, 1)
        # N //= d
        # K //= d
        intervals = SortedList([N])
        for person in range(K):
            top = intervals.pop()
            max, min = getMaxMin(top)
            intervals.update([max, min])
    print("Case #{}: {} {}".format(c, max, min))
