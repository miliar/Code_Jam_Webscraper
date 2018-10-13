inp = open('A-small-attempt0.in')
oup = open('A-small.out', 'w')
import sys

sys.stdout = oup

numCases = int(next(inp))
for case in range(1, numCases + 1):
    print 'Case #' + str(case) + ': ',
    r, t = [int(x) for x in next(inp).split()]
    s = 0
    n = 0
    while s < t:
        n += 1
        s += (n * 2 - 1) ** 2 - (n * 2 - 2) ** 2 + 2 * r
    if s > t:
        n -= 1
    print n

oup.close()
