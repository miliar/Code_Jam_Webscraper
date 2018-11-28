from collections import defaultdict
import copy

def solve1(testLines):
    d = int(testLines[0].split()[0])
    maxt = 0
    for l in testLines[1:]:
        k, s = [int(x) for x in l.split()]
        t = (d - k) / s
        print(k, s, t)
        if t > maxt:
            maxt = t
    return d / maxt

with open('out1', 'wt') as o:
    lines = [l.strip() for l in open('A-small-attempt0.in').readlines()]
    numTests = int(lines[0])
    nextTestLine = 1
    testsCounter = 0
    while testsCounter < numTests:
        testsCounter += 1
        d, n = [int(x) for x in lines[nextTestLine].split()]
        testLines = lines[nextTestLine : nextTestLine + 1 + n]
        nextTestLine += 1 + n
        print('\nsolving: %s' % ([testLines]))
        res = solve1(testLines)
        result = 'Case #%d: %s' % (testsCounter, res)
        print(result)
        _ = o.write(result + '\n')

