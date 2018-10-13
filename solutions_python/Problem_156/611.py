from sys import stdin
from collections import Counter

T = int(stdin.readline())
for t in range(1, T + 1):
    D = int(stdin.readline())
    P = [int(s) for s in stdin.readline().strip().split()]
    ans = 1000
    for P_max in range(1, 1001):
        sminutes = sum(p // P_max - 1*(0==(p % P_max)) for p in P if p > P_max)
        ans = min(ans, sminutes + P_max)
    
    print("Case #%s: %s" % (t, ans))
