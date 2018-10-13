import sys

def check_rows(board, sym):
    for row in board:
        is_win = True
        for c in row:
            if c != sym and c != 'T':
                is_win = False
                break
        if is_win:
            return True
    return False
    
def check_cols(board, sym):
    for col in range(len(board)):
        is_win = True
        for row in range(len(board)):
            if (board[row][col] != sym and
                    board[row][col] != 'T'):
                is_win = False
                break
        if is_win:
            return True
    return False

def check_diags(board, sym):
    is_win = True
    board_sz = len(board)
    for i in range(board_sz):
        if board[i][i] != sym:
            is_win = False
            break
    if is_win:
        return True
        
    is_win = True
    for i in range(board_sz):
        if (board[i][board_sz - 1 - i] != sym and
                board[i][board_sz - 1 - i] != 'T'):
            is_win = False
            break
    if is_win:
        return True
    return False
    
def is_winning(board, sym):
    return (check_rows(board, sym) or check_cols(board, sym)
        or check_diags(board, sym))
        
def has_blank(board):
    for row in board:
        for c in row:
            if c == '.':
                return True
    return False
    
case = 1
f = open(sys.argv[1], 'r')
total_cases = int(f.readline())

while case <= total_cases:
    board = []
    for row in range(4):
        board.append(f.readline().strip())
    result = 'Draw'
    if is_winning(board, 'X'):
        result = 'X won'
    elif is_winning(board, 'O'):
        result = 'O won'
    elif has_blank(board):
        result = 'Game has not completed'
        
    print 'Case #' + str(case) + ': ' + result 
    
    f.readline() # read the blank line
    case += 1