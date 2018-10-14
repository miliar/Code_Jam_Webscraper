lines = [line.strip() for line in open('A-large.in')]
o = open('output.txt', 'w')

T = int(lines.pop(0))


def evalLine(line):
    if(line.count('X') == 4):
        return (True, 'X')
    if(line.count('O') == 4):
        return (True, 'O')
    if(line.count('X') == 3 and line.count('T') == 1):
        return (True, 'X')
    if(line.count('O') == 3 and line.count('T') == 1):
        return (True, 'O')
    return (False, '.')


def evaluate(board):
    points = False

    # Eval diagonals
    downDiagonal = []
    downDiagonal.append(board[0][0])
    downDiagonal.append(board[1][1])
    downDiagonal.append(board[2][2])
    downDiagonal.append(board[3][3])
    gdd = evalLine(downDiagonal)
    if(gdd[0]):
        return '%s won' % gdd[1]

    upDiagonal = []
    upDiagonal.append(board[0][3])
    upDiagonal.append(board[1][2])
    upDiagonal.append(board[2][1])
    upDiagonal.append(board[3][0])
    gup = evalLine(upDiagonal)
    if(gup[0]):
        return '%s won' % gup[1]

    for i in range(4):
        # Eval Horizontal lines
        gl = evalLine(board[i])
        if(gl[0]):
            return '%s won' % gl[1]

        # Eval Columns
        column = []
        column.append(board[0][i])
        column.append(board[1][i])
        column.append(board[2][i])
        column.append(board[3][i])
        gc = evalLine(column)
        if(gc[0]):
            return '%s won' % gc[1]

        if(board[i].count('.') > 0):
            points = True

    # No lines, does it have completed ?
    if not points:
        return 'Draw'
    return 'Game has not completed'


def matricize(board):
    newBoard = []
    for line in board:
        newBoard.append(list(line))
    return newBoard


for i in range(T):
    carriage = i*5
    board = matricize(lines[carriage:carriage+4])

    o.write('Case #%d: %s\n' % (i+1, evaluate(board)))
