n = int(raw_input())

for N in range(n):
    board = []
    for i in range(4):
        board.append([j for j in raw_input()])
    if N < n-1:
        raw_input()
    done = ""
    # rows
    for row in range(4):
        # X
        x_win = True
        for i in board[row]:
            if i != "X" and i != "T":
                x_win = False
                break
        if x_win:
            done = "X"
            break
        # O
        o_win = True
        for i in board[row]:
            if i != "O" and i != "T":
                o_win = False
                break
        if o_win:
            done = "O"
            break
    # cols
    for col in range(4):
        # X
        x_win = True
        for j in range(4):
            i = board[j][col]
            if i != "X" and i != "T":
                x_win = False
                break
        if x_win:
            done = "X"
            break
        # O
        o_win = True
        for j in range(4):
            i = board[j][col]
            if i != "O" and i != "T":
                o_win = False
                break
        if o_win:
            done = "O"
            break
    # diags
    ld = [board[0][0], board[1][1], board[2][2], board[3][3]]
    rd = [board[0][3], board[1][2], board[2][1], board[3][0]]
    x_win = True
    for i in ld:
        if i != "X" and i != "T":
            x_win = False
            break
    if x_win:
        done = "X"
    o_win = True
    for i in ld:
        if i != "O" and i != "T":
            o_win = False
            break
    if o_win:
        done = "O"
    x_win = True
    for i in rd:
        if i != "X" and i != "T":
            x_win = False
            break
    if x_win:
        done = "X"
    o_win = True
    for i in rd:
        if i != "O" and i != "T":
            o_win = False
            break
    if o_win:
        done = "O"
    print "Case #{0}:".format(N+1),
    if done == "X":
        print "X won"
    elif done == "O":
        print "O won"
    else:
        unfinished = False
        for i in range(4):
            for j in range(4):
                if board[i][j] == ".":
                    unfinished = True
                    break
            if unfinished:
                break
        if unfinished:
            print "Game has not completed"
        else:
            print "Draw"
