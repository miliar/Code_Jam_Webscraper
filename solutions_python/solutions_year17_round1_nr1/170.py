from collections import defaultdict

def helper(r, c, board):
    for line in board:
        if (line != '?').sum() == 0:
            continue
        first = np.where(line != '?')[0][0]
        last = np.where(line != '?')[0][-1]
        line[:first] = line[first]
        line[last:] = line[last]
        pad = line[first]
        for i in range(c):
            if line[i] == '?':
                line[i] = pad
            else:
                pad = line[i]
    return board
def solve1(r, c, lines):
    board = np.array([np.array([c for c in l]) for l in lines])
    board = helper(r, c, board)
    board = helper(c, r, board.T).T
    return '\n'.join(''.join(l) for l in board)

with open('out1', 'wt') as o:
    lines = [l.strip() for l in open('A-small-attempt0.in').readlines()]
    numTests = int(lines[0])
    nextTestLine = 1
    testsCounter = 0
    while testsCounter < numTests:
        testsCounter += 1
        r, c = [int(i) for i in lines[nextTestLine].split()]
        testLines = lines[nextTestLine + 1 : nextTestLine + 1 + r]
        nextTestLine += r + 1
        print('\nsolving: r=%s c=%s, board=\n%s' % (r, c, '\n'.join(testLines)))
        board = solve1(r, c, testLines)
        result = 'Case #%d:\n%s' % (testsCounter, board)
        print(result)
        _ = o.write(result + '\n')

