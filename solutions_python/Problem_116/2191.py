from sys import stdin

def testSet(tSet):
    if '.' in tSet:
        return 'U'
    elif 'X' not in tSet:
        return 'O'
    elif 'O' not in tSet:
        return 'X'
    else:
        return '?'

def getResult(board):
    tests = [
        [0, 1, 2, 3],
        [0, 4, 8, 12],
        [0, 5, 10, 15],
        [1, 5, 9, 13],
        [2, 6, 10, 14],
        [3, 6, 9, 12],
        [3, 7, 11, 15],
        [4, 5, 6, 7],
        [8, 9, 10, 11],
        [12, 13, 14, 15]
    ]
    results = []
    emptySpaces = False

    for i in tests:
        tSet = []
        for j in i:
            tSet.append(board[j])
        r = testSet(tSet)
        if r == 'X':
            return 'X won'
        elif r == 'O':
            return 'O won'
        elif r == 'U':
            emptySpaces = True

    if not emptySpaces:
        return 'Draw'
    else:
        return 'Game has not completed'

counter = 0
while True:
    try:
        if stdin.readline() == '':
            break
        board = []
        counter += 1
        for i in range(4):
            for j in stdin.readline().strip('\n'):
                board.append(j)
        print 'Case #%r: %s' % (counter, getResult(board))
    except:
        break