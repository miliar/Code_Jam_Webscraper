f = open("A-large.in")

count = 0
numcases = int(f.readline())
boards = []

lines = [i.strip() for i in f.readlines() if i.strip()]
boards = [lines[4*i:4*i+4] for i in range(numcases)]

def check(board):
    # row check
    count = 0
    for i in range(4):
        if (board[i].count("X") + board[i].count("T")) == 4:
            return "X"
        elif (board[i].count("O") + board[i].count("T")) == 4:
            return "O"

    # column check
    for j in range(4):
        column = [board[i][j] for i in range(4)]
        if (column.count("X") + column.count("T")) == 4:
            return "X"
        elif (column.count("O") + column.count("T")) == 4:
            return "O"

    # left diagonal check
    left_diagonal = [board[i][i] for i in range(4)]
    if (left_diagonal.count("X") + left_diagonal.count("T")) == 4:
        return "X"
    elif (left_diagonal.count("O") + left_diagonal.count("T")) == 4:
        return "O"

    # right diagonal check
    right_diagonal = [board[3-i][i] for i in range(4)]
    if (right_diagonal.count("X") + right_diagonal.count("T")) == 4:
        return "X"
    elif (right_diagonal.count("O") + right_diagonal.count("T")) == 4:
        return "O"

    # completeness check
    full = True
    for row in board:
        if "." in row:
            full = False

    if full:
        return "D"
    else:
        return "I"
        
for i, board in enumerate(boards):
    i += 1
    res = check(board)
    if res == "X":
        print "Case #%s: X won" % str(i)
    elif res == "O":
        print "Case #%s: O won" % str(i)
    elif res == "D":
        print "Case #%s: Draw" % str(i)
    else:
        print "Case #%s: Game has not completed" % str(i)
