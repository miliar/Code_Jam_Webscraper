input_file = open("A-large.in", "r")

def get_param():
    board = []
    for i in range(4):
        line = input_file.readline()
        row = []
        for e in line:
            row.append(e)
        board.append(row)
    return board

def is_in_row(symbol, board):
    count = 0
    for row in board:
        for e in row:
            if e == symbol or e == 'T':
                count += 1
        if count == 4:
            return True
        else:
            count = 0
    return False

def is_in_col(symbol, board):
    count = 0
    for i in range(4):
        for row in board:
            if row[i] == symbol or row[i] == 'T':
                count += 1
        if count == 4:
            return True
        else:
            count = 0
    return False

def is_in_diag(symbol, board):
    count = 0
    for i in range(4):
        if board[i][i] == symbol or board[i][i] == 'T':
            count += 1
        if count == 4:
            return True
    count = 0
    for i in range(4):
        if board[i][3-i] == symbol or board[i][3-i] == 'T':
            count += 1
        if count == 4:
            return True
    return False

def is_win(symbol, board):
    if is_in_row(symbol, board) or is_in_col(symbol, board) or is_in_diag(symbol, board):
        return True
    else:
        return False

def judgement(case, board):
    if is_win('X', board):
        print "Case #" + str(case) + ": X won"
    elif is_win('O', board):
        print "Case #" + str(case) + ": O won"
    else:
        for row in board:
            if '.' in row:
                print "Case #" + str(case) + ": Game has not completed"
                return
        print "Case #" + str(case) + ": Draw"

case = input_file.readline()
for i in range(int(case)):
    board = get_param()
    judgement(i+1, board)
    input_file.readline()
input_file.close()
