f = open("A-small-attempt1.in")
count = int(f.readline())
cases = f.read().split("\n\n")[:-1]
f.close()

def to_board(board_str):
    board = []
    rows = board_str.split("\n")
    for row_str in rows:
        row = []
        for cell in row_str:
            cell_val = 0
            if cell == 'X':
                cell_val = 0x1
            elif cell == 'O':
                cell_val = 0x2
            elif cell == 'T':
                cell_val = 0x4
            elif cell == '.':
                cell_val = 0x8
            row.append(cell_val)
        board.append(row)
    return board

def check_mask_and(board, mask):
    for i in range(4):
        if (board[0][i] & mask) != 0 and (board[1][i] & mask) != 0 and \
            (board[2][i] & mask) != 0 and (board[3][i] & mask) != 0:
            return True

        if (board[i][0] & mask) != 0 and (board[i][1] & mask) != 0 and \
            (board[i][2] & mask) != 0 and (board[i][3] & mask) != 0:
            return True

    if (board[0][0] & mask) != 0 and (board[1][1] & mask) != 0 and \
        (board[2][2] & mask) != 0 and (board[3][3] & mask) != 0:
        return True

    if (board[3][0] & mask) != 0 and (board[2][1] & mask) != 0 and \
        (board[1][2] & mask) != 0 and (board[0][3] & mask) != 0:
        return True
    return False


for i in range(count):
    case = cases[i]
    b = to_board(case)
    x_win = check_mask_and(b, 0x1|0x4)
    o_win = check_mask_and(b, 0x2|0x4)
    x_may_win = check_mask_and(b, 0x1|0x4|0x8)
    o_may_win = check_mask_and(b, 0x2|0x4|0x8)

    i += 1
    if x_win:
        print "Case #%d: X won" % i
    elif o_win:
        print "Case #%d: O won" % i
    elif x_may_win or o_may_win:
        print "Case #%d: Game has not completed" % i
    else:
        print "Case #%d: Draw" % i
