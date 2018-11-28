import sys
import numpy as np

def applyGravity(grid, N):
    for row in grid:
        lastpos = N-1
        pos = N-1
        while(pos >= 0):
            if row[pos] != '.':
                row[lastpos] = row[pos]
                if pos != lastpos:
                    row[pos] = '.'
                lastpos -= 1
            pos -= 1

def checkWins(grid, N, K):
    matches = set()
    for row in grid:
        matches = matches.union(checkRow(row, N, K))
        if len(matches) == 2:
            return matches

    for i in xrange(N):
        col = grid[:, i]
        matches = matches.union(checkRow(col, N, K))
        if len(matches) == 2:
            return matches

    for i in xrange(-N+1, N):
        col = grid.diagonal(i)
        matches = matches.union(checkRow(col, N, K))
        if len(matches) == 2:
            return matches
    
    grid = np.fliplr(grid)
    for i in xrange(-N+1, N):
        col = grid.diagonal(i)
        matches = matches.union(checkRow(col, N, K))
        if len(matches) == 2:
            return matches

    return matches

def checkRow(row, N, K):
    l = 0
    prev = '.'
    matches = set()
    for i, c in enumerate(row):
        if l + N - i < K:
            break

        if c == '.':
            l = 0
        elif c != prev:
            l = 1
        else:
            l += 1

        prev = c
        
        if l == K:
            matches.add(c)

    return matches

def printGrid(grid):
    for row in grid:
        for c in row:
            print c,
        print

def main(argv=None):
    global caseNo
    if not argv:
        argv = sys.argv[1:]
    if len(argv) >= 1:
        inFileName= argv[0]
    else:
        inFileName = "test.in"
    if len(argv) >= 2:
        outFileName = argv[1]
    else:
        outFileName = "out.out"

    with open(inFileName) as inFile:
        with open(outFileName, 'w') as outFile:
            numCases = int(inFile.readline())
            for caseNo in xrange(1, numCases+1):
                toks = inFile.readline().split()
                N, K = [long(tok) for tok in toks]
                grid = []
                for i in xrange(N):
                    line = inFile.readline()[:-1]
                    grid.append([c for c in line])
                grid = np.array(grid)
                applyGravity(grid, N)
                matches = checkWins(grid, N, K)
                
                if len(matches) == 2:
                    desc = 'Both'
                elif len(matches) == 0:
                    desc = 'Neither'
                elif 'R' in matches:
                    desc = 'Red'
                else:
                    desc = 'Blue'

                outFile.write('Case #{0}: {1}\n'.format(caseNo, desc))

if __name__ == "__main__":
    main()
