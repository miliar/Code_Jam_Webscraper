# Google Code Jam 2013 qualification round B.
# Keep track of highest setting for each row and column.
# If a square needs to be lower than the highest of its row and column,
# answer NO.
import sys

def doCase(file):
    (rows, cols) = [int(c) for c in file.readline().split()]
    rowHighest = [0 for i in range(rows)]
    colHighest = [0 for i in range(cols)]
    pattern = []
    for r in range(rows):
        row = file.readline().split()
        pattern += [row]
        for c in range(cols):
            rowHighest[r] = max(rowHighest[r], row[c])
            colHighest[c] = max(colHighest[c], row[c])
    for r in range(rows):
        for c in range(cols):
            if pattern[r][c] < min(rowHighest[r], colHighest[c]):
                return 'NO'
    return 'YES'

def run():
    file = open(sys.argv[1])
    numCases = int(file.readline())
    for case in range(1, numCases+1):
        answer = doCase(file)
        print 'Case #{0}: {1}'.format(case, answer)
run()
