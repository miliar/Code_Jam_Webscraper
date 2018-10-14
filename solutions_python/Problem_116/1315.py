import sys

def read_int(fp=sys.stdin):
    return int(fp.readline().strip())

def read(fp=sys.stdin):
    board = []
    for i in range(4):
        line = fp.readline().strip()
        board.extend(list(line))
    fp.readline()
    return board

def write(board, fp=sys.stdout):
    for i in range(0, 12+1, 4):
        print >>fp, " ".join(board[i:i+4])

def state(board):
    is_x = lambda v: v in "XT"
    is_o = lambda v: v in "OT"
    is_empty = lambda v: v == "."

    #  0  1  2  3
    #  4  5  6  7
    #  8  9 10 11
    # 12 13 14 15

    diagonal1 = board[0:15+1:5]
    diagonal2 = board[3:12+1:3]

    if all(map(is_x, diagonal1)) or all(map(is_x, diagonal2)):
        return "X won"
    if all(map(is_o, diagonal1)) or all(map(is_o, diagonal2)):
        return "O won"

    for i in range(4):
        horizontal = board[i*4:i*4+4]
        vertical   = board[i::4]
        if all(map(is_x, horizontal)) or all(map(is_x, vertical)):
            return "X won"
        if all(map(is_o, horizontal)) or all(map(is_o, vertical)):
            return "O won"

    if any(map(is_empty, board)):
        return "Game has not completed"
    else:
        return "Draw"

if __name__ == "__main__":
    T = read_int()
    for i in range(T):
        board = read()
        print "Case #%d: %s" % (i + 1, state(board))
