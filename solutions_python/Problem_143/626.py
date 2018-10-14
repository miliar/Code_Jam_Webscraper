import sys, os
from collections import defaultdict

puzzles = list()

FILENAME = 'B-small-attempt1.in'

sys.setrecursionlimit(100000)


def solve(puzzle):
    [mini, maxi, k] = puzzle
    #mini -= 1
    #maxi -= 1
    #k -= 1
    #bMini = bin(min(mini, maxi))
    #bMaxi = bin(max(mini, maxi))
    #maxBitLen = len(bMaxi) - 2



    #result = set()
    result = 0
    #for ik in range(k):
    for m in range(mini):
        for n in range(maxi):
            if m&n < k:
                result += 1
                #result.add((m,n))
    #return len(result)
    return result


with open(FILENAME, 'r') as f:
    nbTestCases = int(f.readline())

    for _ in range(nbTestCases):
        puzzles.append([int(n) for n in f.readline().strip().split()])

printResult = ''
for (i, puzzle) in enumerate(puzzles):
    print puzzle
    #print 'Case #%s: %s\n' % (i+1, solve(puzzle))
    printResult += 'Case #%s: %s\n' % (i+1, solve(puzzle))

print printResult
#sys.exit(0)

if os.path.isfile('result'):
    os.remove('result')
with open('result', 'w') as f:
    f.write(printResult[:-1])