
XWON = "X won"
OWON = "O won"
DRAW = "Draw"
NOTOVER = "Game has not completed"

def alllines(board):
    for line in board:
        yield "".join(line)
    for line in zip(*board):
        yield "".join(line)
    size = len(board)
    yield "".join(board[i][i] for i in xrange(size))
    yield "".join(board[i][size-i-1] for i in xrange(size))

def line_is_win_for(player, line):
    allowed = "T" + player
    return all(cell in allowed for cell in line)

def board_contains_blank(board):
    return any('.' in line for line in board)

def evaluate(board):
    lines = list(alllines(board))
    if any(line_is_win_for("X", line) for line in lines):
        return XWON
    if any(line_is_win_for("O", line) for line in lines):
        return OWON
    if board_contains_blank(board):
        return NOTOVER
    return DRAW

def main():
    t = int(raw_input().strip())
    for case in xrange(1,t+1):
        board = [raw_input().strip() for i in xrange(4)]
        raw_input()
        print "Case #{}: {}".format(case, evaluate(board))

if __name__=="__main__":
    main()
