import sys, os

puzzles = list()

FILENAME = 'A-small-attempt0.in'

def printPuzzle(puzzle):
    print 'Puzzle'
    for (i, round) in enumerate(puzzle):
        print 'Round #', i+1
        for line in round[1]:
            print line
        print 'Answer : ', round[0]
        print

def solve(puzzle):
    candidates = set()
    start = True
    for round in puzzle:
        if start:
            candidates = set([int(a) for a in round[1][round[0]-1]])
            start = False
            continue
        candidates = candidates.intersection(set([int(a) for a in round[1][round[0]-1]]))
    if len(candidates) > 1:
        return 'Bad magician!'
    elif len(candidates) == 0:
        return 'Volunteer cheated!'
    else:
        return candidates.pop()



with open(FILENAME, 'r') as f:
    nbTestCases = int(f.readline())
    for _ in range(nbTestCases):
        currentPuzzle = list()
        for _ in range(2):
            currentGrid = list()
            answer = int(f.readline().strip())
            for _ in range(4):
                currentGrid.append(f.readline().strip().split())
            currentPuzzle.append((answer, currentGrid))
        puzzles.append(currentPuzzle)

printResult = ''
for (i, puzzle) in enumerate(puzzles):
    #printPuzzle(puzzle)
    #print 'Case #%s: %s\n' % (i+1, solve(puzzle))
    printResult += 'Case #%s: %s\n' % (i+1, solve(puzzle))

print printResult
#sys.exit(0)

if os.path.isfile('result'):
    os.remove('result')
with open('result', 'w') as f:
    f.write(printResult[:-1])