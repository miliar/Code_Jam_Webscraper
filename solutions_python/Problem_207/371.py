from collections import defaultdict
from operator import itemgetter
import copy

def solve2(testLines):
    n, r, o, y, g, b, v = [int(x) for x in testLines[0].split()]
    c2c = {'R':r, 'O':o, 'Y':y, 'G':g, 'B':b, 'V':v, }
    print(c2c.items())
    if n == 1:
        m = max(c2c.items(), key = itemgetter(1))
        return m[0]
    if max(c2c.values()) > n / 2:
        return 'IMPOSSIBLE'
    res = '.'
    while n > 0:
        n -= 1
        m = max(filter(lambda x: x[0] != res[-1], c2c.items()), key = itemgetter(1))[0]
        c2c[m] -= 1
        res += m
    res = res[1:]
    if res[0] == res[-1]:
        res = res[:-2] + res[-1] + res[-2]
    return res


with open('out2', 'wt') as o:
    lines = [l.strip() for l in open('B-small-attempt1.in').readlines()]
    numTests = int(lines[0])
    nextTestLine = 1
    testsCounter = 0
    while testsCounter < numTests:
        testsCounter += 1
        testLines = lines[nextTestLine : nextTestLine + 1]
        nextTestLine += 1
        print('\nsolving: %s' % ([testLines]))
        res = solve2(testLines)
        result = 'Case #%d: %s' % (testsCounter, res)
        print(result)
        _ = o.write(result + '\n')

