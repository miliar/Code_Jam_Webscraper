from math import sqrt
from decimal import Decimal

def solve(n):
    res = Decimal('0.0')
    for k in range(n + 1):
        c = 1
        for i in range(0, k): c *= n - i
        for i in range(0, k): c /= k - i
        c *= c
        a = Decimal(3**(2*(n-k)))
        b = Decimal(5**k)
        res += (a*b*c)**Decimal('0.5') % 1000
        res = res % 1000
    return int(res)
           

for t in range(input()):
    n = input()
    print("Case #%d: %03d" % (t + 1, solve(n)))
