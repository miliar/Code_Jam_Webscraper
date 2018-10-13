def check_rows(board):
    draw = True
    for line in board:
        if line[0] in 'XT' and line[1] in 'XT' and line[2] in 'XT' and line[3] in 'XT':
            return 'X'
        if line[0] in 'OT' and line[1] in 'OT' and line[2] in 'OT' and line[3] in 'OT':
            return 'O'
        if '.' in line:
            draw = False
    if draw:
        return 'D'
    else:
        return '.'
    
def check_cols(board):
    for i in xrange(4):
        if board[0][i] in 'XT' and board[1][i] in 'XT' and board[2][i] in 'XT' and board[3][i] in 'XT':
            return 'X'
        if board[0][i] in 'OT' and board[1][i] in 'OT' and board[2][i] in 'OT' and board[3][i] in 'OT':
            return 'O'

def check_diag(board):
    if board[0][0] in 'XT' and board[1][1] in 'XT' and board[2][2] in 'XT' and board[3][3] in 'XT':
        return 'X'
    if board[0][3] in 'XT' and board[1][2] in 'XT' and board[2][1] in 'XT' and board[3][0] in 'XT':
        return 'X'
    if board[0][0] in 'OT' and board[1][1] in 'OT' and board[2][2] in 'OT' and board[3][3] in 'OT':
        return 'O'
    if board[0][3] in 'OT' and board[1][2] in 'OT' and board[2][1] in 'OT' and board[3][0] in 'OT':
        return 'O'

MSG = {
    'X': 'X won',
    'O': 'O won',
    'D': 'Draw',
    '.': 'Game has not completed'
}

for i in xrange(int(raw_input())):
    lines = []
    for j in xrange(4):
        lines.append(raw_input())
    raw_input()
    ans = check_diag(lines)
    if not ans: ans = check_cols(lines)
    if not ans: ans = check_rows(lines)
    print 'Case #%d:' % (i+1), MSG[ans]
