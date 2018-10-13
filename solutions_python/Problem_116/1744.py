def process_diag(b, s):
    #Diag 1
    diag_ok = True
    for i in range(0, 4):
        if (b[i][i] != s and b[i][i] != "T"):
            diag_ok = False
            break
    if diag_ok:
        return True

    #Diag 2
    diag_ok = True
    for i in range(0, 4):
        if (b[i][3-i] != s and b[i][3-i] != "T"):
            diag_ok = False
            break
    if diag_ok:
        return True

    return False

def process_rows(b, s):
    for i in range(0, 4):
        row_ok = True
        for j in range(0, 4):
            if (b[j][i] != s and b[j][i] != "T"):
                row_ok = False
                break
        if row_ok:
            return True
    return False

def process_columns(b, s):
    for i in range(0, 4):
        column_ok = True
        for j in range(0, 4):
            if (b[i][j] != s and b[i][j] != "T"):
                column_ok = False
                break
        if column_ok:
            return True
    return False

def free_positions(b):
    for i in range(0, 4):
        for j in range(0, 4):
            if (b[i][j] == "."):
                return True
    return False

def process_board(c, b):
    o_won = process_rows(b, "O") or process_columns(b, "O") or process_diag(b, "O")
    x_won = process_rows(b, "X") or process_columns(b, "X") or process_diag(b, "X")
    if (o_won and not x_won):
        print "Case #" + str(c) + ": O won"
        return
    if (x_won and not o_won):
        print "Case #" + str(c) + ": X won"
        return
    if (x_won and o_won):
        print "Case #" + str(c) + ": Draw"
        return

    if (free_positions(b)):
        print "Case #" + str(c) + ": Game has not completed"
    else:
        print "Case #" + str(c) + ": Draw"

with open("A-large.in") as f:
    content = f.readlines()

next = 1
board = [
    [".", ".", ".", "."],
    [".", ".", ".", "."],
    [".", ".", ".", "."],
    [".", ".", ".", "."]
]
for i in range(0, int(content[0].rstrip())):
    for j in range(0, 4):
        for k in range(0, 4):
            board[j][k] = content[next+j][k]
    process_board(i+1, board)
    next = next + 5