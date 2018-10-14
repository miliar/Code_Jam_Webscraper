from fractions import gcd
import math

inf = open("A-large.in")
outf = open("A-large.out", "w")

EPS = 1e-10

numTests = int(inf.readline().rstrip())



def solve(points, D):
    dp = [0] * len(points)
    dp[0] = points[0][0]
    for i in xrange(len(points)):
        x, L = points[i]
        h = dp[i]
        if not h:
            continue
        if x + h >= D:
            return True
        for j in xrange(i + 1, len(points)):
            if points[j][0] - x <= h:
                dp[j] = max(dp[j], min(points[j][1], points[j][0] - x))
            else:
                break
    return False

for test in xrange(numTests):
    print test
    n = int(inf.readline().strip())
    points = []
    for i in xrange(n):
        points.append(list(map(int, inf.readline().split())))
    D = int(inf.readline().strip())
    print >>outf, "Case #%d: %s" % (test + 1, "YES" if solve(points, D) else "NO")

