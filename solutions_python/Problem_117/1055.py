import numpy as np
import pprint

__author__ = 'vasilisakoinoglou'

DEVEL = False

inputf = open('s_in.txt', 'r') if DEVEL else open('in.txt', 'r')

outputf = open('s_out.txt', 'w') if DEVEL else open('out.txt', 'w')

T = 0

patterns = []


def readInput():
    global T, patterns
    with inputf as f:
        T = int(f.readline())
        for case in range(0, T):
            N, M = f.readline().split()
            grid = []
            for n in range(0, int(N)):
                grid.append([int(x) for x in f.readline().split()])
            patterns.append(grid)


def validatePattern(pattern):
    # Each element should have
    # a valid point of entry
    rows = np.array(pattern)
    columns = rows.T
    for row in rows:
        for index, e in enumerate(row):
            if not (e == max(row)) and not (e == max(columns[index])):
                return False
    return True


readInput()

output = []
for index, pattern in enumerate(patterns):
    case = index + 1
    isValid = "YES" if validatePattern(pattern) else "NO"
    sout = "Case #%i: %s\n" % (case, isValid,)
    output.append(sout)
outputf.writelines(output)

print "=" * 80
for pattern in patterns:
    pprint.pprint(pattern, width=40)
    print validatePattern(pattern)
    print "=" * 80


