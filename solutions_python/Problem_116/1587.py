filename = "A-small-attempt0.in" # change later
f = open(filename)
T = int(f.readline())
for case in range(1,T+1):
    board = []
    dot_flag = 0
    for i in range(1,5):
        s = f.readline()
        if '.' in s:
            dot_flag = 1
        board.append(s[:-1])
    f.readline() # waste 1 empty line
    O_win_flag = 0
    X_win_flag = 0
    # yoko check
    for i in range(4):
        if board[i][0] == 'O' or (board[i][0] == 'T' and board[i][1] == 'O'):
            for j in range(1,4):
                if board[i][j] != 'O' and board[i][j] != 'T':
                    break
                if j == 3:
                    O_win_flag = 1
        elif board[i][0] == 'X' or (board[i][0] == 'T' and board[i][1] == 'X'):
            for j in range(1,4):
                if board[i][j] != 'X' and board[i][j] != 'T':
                    break
                if j == 3:
                    X_win_flag = 1
    # tate check
    for i in range(0,4):
        if board[0][i] == 'O' or (board[0][i] == 'T' and board[1][i] == 'O'):
            for j in range(0,4):
                if board[j][i] != 'O' and board[j][i] != 'T':
                    break
                if j == 3:
                    O_win_flag = 1
        elif board[0][i] == 'X' or (board[0][i] == 'T' and board[1][i] == 'X'):
            for j in range(0,4):
                if board[j][i] != 'X' and board[j][i] != 'T':
                    break
                if j == 3:
                    X_win_flag = 1
    # hidari naname check
    if board[0][0] == 'O' or (board[0][0] == 'T' and board[1][1] == 'O'):
            for j in range(0,4):
                if board[j][j] != 'O' and board[j][j] != 'T':
                    break
                if j == 3:
                    O_win_flag = 1
    elif board[0][0] == 'X' or (board[0][0] == 'T' and board[1][1] == 'X'):
            for j in range(0,4):
                if board[j][j] != 'X' and board[j][j] != 'T':
                    break
                if j == 3:
                    X_win_flag = 1
    # migi naname check
    if board[0][3] == 'O' or (board[0][3] == 'T' and board[1][2] == 'O'):
            for j in range(1,4):
                if board[j][3-j] != 'O' and board[j][3-j] != 'T':
                    break
                if j == 3:
                    O_win_flag = 1
    elif board[3][0] == 'X' or (board[3][0] == 'T' and board[2][1] == 'X'):
            for j in range(1,4):
                if board[j][3-j] != 'X' and board[j][3-j] != 'T':
                    break
                if j == 3:
                    X_win_flag = 1
                    
    print "Case #" + str(case) + ": " ,
    if X_win_flag == 1:
        print "X won"
    if O_win_flag == 1:
        print "O won"
    if X_win_flag == 0 and O_win_flag == 0 and dot_flag == 0:
        print "Draw"
    if X_win_flag == 0 and O_win_flag == 0 and dot_flag == 1:
        print "Game has not completed"
