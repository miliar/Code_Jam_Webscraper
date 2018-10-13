__author__ = 'vasilisakoinoglou'

DEVEL = False

inputf = open('s_in.txt', 'r') if DEVEL else open('in.txt', 'r')

outputf = open('s_out.txt', 'w') if DEVEL else open('out.txt', 'w')

T = 0
boards = []

player1 = 'X'
player2 = 'O'
wild = 'T'
empty = '.'


def readInput():
    global T, boards
    with inputf as f:
        T = int(f.readline())
        lines = f.read().split('\n')
        cboard = []
        for line in lines:
            if line == '' and cboard != []:
                boards.append(cboard)
                cboard = []
            else:
                cboard.append(line)


def checkSequence(player, sequence):
    if (sequence.count(player) == 4) or (sequence.count(player)==3 and sequence.count(wild)==1):
        return True
    return False


def solveBoard(board, player):
    # For each row
    for index, row in enumerate(board):
        # Check horizontally
        if checkSequence(player, row):
            return True
            # Check vertically (first row is enough)
        if index == 0:
            for index, c in enumerate(row):
                column = [cc[index] for cc in board]
                if checkSequence(player, column):
                    return True
    # Check diagonal ([0][0] and [-1][0] are enough)
    firstd = []
    secondd = []
    for index, row in enumerate(board):
        firstd.append(row[index])
        secondd.append(row[-1 - index])
    if checkSequence(player, firstd):
        return True
    if checkSequence(player, secondd):
        return True

    return False


readInput()
results = []

solveBoard(boards[4], player1)

for index, board in enumerate(boards):
    case = index+1
    one = solveBoard(board, player1)
    two = solveBoard(board, player2)
    if one:
        results.append("Case #%i: %s won\n" % (case, player1,))
    elif two:
        results.append("Case #%i: %s won\n" % (case, player2,))
    # Check for a draw
    elif (not one) and (not two) and (not empty in ''.join(board)):
        results.append("Case #%i: Draw\n" % (case,))
    else:
        results.append("Case #%i: Game has not completed\n" % (case,))

outputf.writelines(results)

for result in results:
    print result