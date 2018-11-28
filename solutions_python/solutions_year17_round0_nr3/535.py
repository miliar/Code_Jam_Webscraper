import sys

sys.setrecursionlimit(100000)

inp = sys.stdin
outp = sys.stdout

def doit(S, n1, n2, K):
    if S == 1:
        return (0, 0)
    if K <= n1:
        return (S/2, (S-1)/2)
    if K <= n1+n2:
        return ((S-1)/2, (S-2)/2)

    if S % 2 == 0:
        return doit(S/2, n1, n1+2*n2, K-n1-n2)
    else:
        return doit(S/2, 2*n1+n2, n2, K-n1-n2)

def solve():
    (N, K) = map(int, sys.stdin.readline().split())
    (y, z) = doit(N, 1, 0, K)
    print '%d %d' % (y, z)

T = int(inp.readline())
for i in range(T):
    outp.write('Case #%d: ' % (i+1))
    solve()
