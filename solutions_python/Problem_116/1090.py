inputFile = open("A-large.in")

rows = 4

line = inputFile.readline()[:-1]
number = int(line)

def checkRows(game, board):
    for i in range(len(board)):
        winner = True
        player = board[i][0]
        if player == "T":
            player = board[i][1]
        for j in range(len(board[0])):
            if (board[i][j] != player and board[i][j] != "T") or board[i][j] == ".":
                winner = False
                break
        if winner:
            print "Case #" + str(game + 1) + ": " + player + " won"
            return True
    return False

def checkCols(game, board):
    for j in range(len(board[0])):
        winner = True
        player = board[0][j]
        if player == "T":
            player = board[1][j]
        for i in range(len(board)):
            if (board[i][j] != player and board[i][j] != "T") or board[i][j] == ".":
                winner = False
                break
        if winner:
            print "Case #" + str(game + 1) + ": " + player + " won"
            return True
    return False

def checkDiags(game, board):
    winner = True
    player = board[0][0]
    if player == "T":
        player = board[1][1]
    for i in range(len(board)):
        if (board[i][i] != player and board[i][i] != "T") or board[i][i] == ".":
            winner = False
            break
    if winner:
        print "Case #" + str(game + 1) + ": " + player + " won"
        return True
    winner = True
    player = board[3][0]
    if player == "T":
        player = board[2][1]
    for i in range(len(board)):
        if (board[len(board) - 1 - i][i] != player and board[len(board) - 1 - i][i] != "T") or board[len(board) - 1 - i][i] == ".":
            winner = False
            break
    if winner:
        print "Case #" + str(game + 1) + ": " + player + " won"
        return True
    return False

def checkIncomplete(game, board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == ".":
                return True

for game in range(number):
    board = []
    for row in range(rows):
        row = []
        line = inputFile.readline()[:-1]
        for char in line:
            row.append(char)
        board.append(row)
    line = inputFile.readline()
    if checkRows(game, board):
        continue
    if checkCols(game, board):
        continue
    if checkDiags(game, board):
        continue
    if checkIncomplete(game, board):
        print "Case #" + str(game + 1) + ": Game has not completed"
        continue
    print "Case #" + str(game + 1) + ": Draw"
