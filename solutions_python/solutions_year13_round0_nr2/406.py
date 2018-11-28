#!python
import sys

def gets():
    return sys.stdin.readline().rstrip('\r\n')

def readint():
    return int(gets())

def readints():
    return [int(x) for x in gets().split()]

#leq = less than or equal to
def all_leq(vals, x):
    for v in vals:
        if v > x:
            return False
    return True


def solve(a, n, m):
    for i in xrange(n):
        for j in xrange(m):
            if all_leq((a[r][j] for r in range(n)), a[i][j]) or all_leq((a[i][c] for c in range(m)), a[i][j]):
                pass
            else:
                return "NO"
    return "YES"


T = readint()
for nCase in xrange(T):
    n, m = readints()
    a = []
    for i in range(n):
        a.append(readints())

    ans = solve(a, n, m)
    print("Case #%d: %s" % (nCase+1, ans))
