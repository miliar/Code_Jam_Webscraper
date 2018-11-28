from sys import stdin
from bisect import *
def solve():
    read_ints = lambda: map(int, stdin.readline().split())
    n, X = read_ints()
    a = read_ints()
    a.sort()
    u = [False] * n
    ans = 0
    for i, x in enumerate(a):
        if u[i]:
            continue
        j = bisect(a, X - x, i + 1)
        j -= 1
        while u[j] and j > i:
            j -= 1
        if j > i:
            u[j] = True
        ans += 1
    return ans
T = int(raw_input())
for t in xrange(T):
    print "Case #%d: %d" % (t+1, solve())
