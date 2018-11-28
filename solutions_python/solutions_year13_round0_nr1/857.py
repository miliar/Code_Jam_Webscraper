# tic-tac-toe-tomek problem

def importData(filename):
    fin = open(filename)

    cases = int(fin.readline().strip())
    print cases
    boards = []
    for c in range(cases):
        boards.append([])
        for j in range(4):
            boards[c].append( list(fin.readline().strip()))
        fin.readline()

    for b in boards:
        for l in b:
            print l
        print "         (break)"

    return boards


def checkForEmptySpaces(board):
    for line in board:
        for item in line:
            if item == '.':
                return True
    return False

def checkLine(board, player, coords):
    # coords is of the format:
    # [(x,y), (x,y), (x,y), (x,y)]
    in_a_row = 0
    for c in coords:
        #print c
        if board[c[0]][c[1]] == player or board[c[0]][c[1]] == 'T':
            in_a_row += 1
    if in_a_row == 4:
        return True
    else:
        return False

def checkVerticals(board, player):
    # generate coords lists that are vertical. X is the same, y differs.
    found = False
    for x in range(4):
        coords = []
        for y in range(4):
            coords.append((x, y))
        #print coords
        found = found or checkLine(board, player, coords)
    return found

def checkHorizontals(board, player):
    # generate coords lists that are vertical. X is the same, y differs.
    found = False
    for x in range(4):
        coords = []
        for y in range(4):
            coords.append((y, x))
        found = found or checkLine(board, player, coords)
    return found

def checkDiagonals(board, player):
    diag1 = [(0,0), (1,1), (2,2), (3,3)]
    diag2 = [(0,3), (1,2), (2,1), (3,0)]
    found = False or checkLine(board, player, diag1)
    found = found or checkLine(board, player, diag2)
    return found

def checkBoard(board):
    for player in ['O', 'X']:
        if checkVerticals(board, player):
            return "%s won" % player
        if checkHorizontals(board, player):
            return "%s won" % player
        if checkDiagonals(board, player):
            return "%s won" % player

    if checkForEmptySpaces(board):
        return "Game has not completed"
    else:
        return "Draw"

def main(boards):
    answers = []
    for board in boards:
        answers.append(checkBoard(board))
    return answers

if __name__ == "__main__":
    filename = "a.in"
    filename = "A-small-attempt0.in"
    filename = "A-large.in"
    boards = importData(filename)
    answers = main(boards)
    fout = open("a.out", 'w')
    for i in range(len(answers)):
        fout.write("Case #%s: %s\n" % (i + 1, answers[i]))
    print answers

