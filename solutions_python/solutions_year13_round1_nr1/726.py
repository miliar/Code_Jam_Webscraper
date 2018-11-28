# https://code.google.com/codejam/contest/2418487/dashboard
import sys

def readline():
    return sys.stdin.readline().rstrip()

t = int(readline())
for x in range(t):
    line = readline()
    (r, t) = [int(s) for s in line.split()]
    n = 0
    p = 0
    while p <= t:
        p += 2*r + 1 + 4*n
        n += 1
    n -= 1
    print 'Case #{}: {}'.format(x+1, n)

