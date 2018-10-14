import sys

# xxxx-
# xxxx-
# xxxx-
# xxxx-
# find(".") != -1 Game has not completed
# find("XXXX") != -1 => X won
# find("OOOO") != -1 => O won

# cols
# 0, 5, 10, 15
# 1, 6, 11, 16
# 2, 7, 12, 17
# 3, 8, 13, 18

# 0, 6, 12, 18 todos iguales => m[0] won
# 3, 7, 11, 15   "      "    => m[3] won

def won_with_items(items):
    if len(items) == 1 or items == {"X", "T"} or items == {"O", "T"}:
        if "X" in items:
            print "X won"
            return True
        if "O" in items:
            print "O won"
            return True
    return False

def figure_out_state(board):
    if board.find("X"*4) != -1 or \
            board.find("X"*3+"T") != -1:
        print "X won"
        return

    if board.find("O"*4) != -1 or \
            board.find("O"*3+"T") != -1:
        print "O won"
        return

    diag1 = {board[0], board[6], board[12], board[18]}
    diag2 = {board[3], board[7], board[11], board[15]}
    column1 = {board[0], board[5], board[10], board[15]}
    column2 = {board[1], board[6], board[11], board[16]}
    column3 = {board[2], board[7], board[12], board[17]}
    column4 = {board[3], board[8], board[13], board[18]}
    possibilities = [diag1, diag2, column1, column2, column3, column4]
    for pos in possibilities:
        if won_with_items(pos):
            return

    if board.find(".") != -1:
        print "Game has not completed"
        return
    print "Draw"

if __name__ == "__main__":
    boards = []
    with open(sys.argv[1], "r") as f:
        testcases = int(f.readline().strip())
        for case in xrange(testcases):
            board = f.read(20)
            boards.append(board)
            f.readline()  # empty line

    case = 0
    for board in boards:
        case += 1
        print "Case #%d:" % (case,),
        figure_out_state(board)
