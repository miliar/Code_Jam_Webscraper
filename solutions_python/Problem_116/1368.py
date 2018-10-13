def win(board, player):
    lines = board
    for i in range(4):
        lines.append(board[0][i] + board[1][i] + board[2][i]\
                + board[3][i])
    lines.append(board[0][0] + board[1][1] + board[2][2] + board[3][3])
    lines.append(board[0][3] + board[1][2] + board[2][1] + board[3][0])

    for line in lines:
        if line.count(player) + line.count('T') == 4:
            return True
    return False

def unfinished(board):
    for i in range(4):
        if board[i].count('.') != 0:
            return True
    return False

f = open('tttt.in', 'r')
fout = open('tttt.out', 'w')
total_test_case = int(f.readline())
for test_case_number in range(total_test_case):
    board = []
    for i in range(4):
        board.append(f.readline())
    f.readline()

    print >> fout, 'Case #' + str(test_case_number + 1) + ':',
    if win(board, 'X'):
        print >> fout, 'X won'
    elif win(board, 'O'):
        print >> fout, 'O won'
    elif unfinished(board):
        print >> fout, 'Game has not completed'
    else:
        print >> fout, 'Draw'
