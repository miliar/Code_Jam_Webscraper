

fin = open("a.in")

cases = int(fin.readline().strip())

for c in range(cases):
    board = []

    for i in range(4):
        board.append([char for char in fin.readline().strip()])
    fin.readline()

    done = False
    found_blank = False
    o_won = False
    x_won = False

    # Rows

    for i in range(4):
        o_winning = True
        x_winning = True

        for j in range(4):
            if board[i][j] == 'X':
                o_winning = False
            elif board[i][j] == 'O':
                x_winning = False
            elif board[i][j] == '.':
                found_blank = True
                o_winning = x_winning = False
                break
    
        if x_winning:
            x_won = True
            done = True
            break
        elif o_winning:
            o_won = True
            done = True
            break

    # Columns

    if not done:
        for i in range(4):
            o_winning = True
            x_winning = True

            for j in range(4):
                if board[j][i] == 'X':
                    o_winning = False
                elif board[j][i] == 'O':
                    x_winning = False
                elif board[j][i] == '.':
                    found_blank = True
                    o_winning = x_winning = False
                    break
        
            if x_winning:
                x_won = True
                done = True
                break
            elif o_winning:
                o_won = True
                done = True
                break

    # Diagonals

    if not done:
        o_winning = True
        x_winning = True

        for i in range(4):
            if board[i][i] == 'X':
                o_winning = False
            elif board[i][i] == 'O':
                x_winning = False
            elif board[i][i] == '.':
                found_blank = True
                o_winning = x_winning = False
                break
        
        if x_winning:
            x_won = True
            done = True
        elif o_winning:
            o_won = True
            done = True

    if not done:
        o_winning = True
        x_winning = True

        for i in range(4):
            if board[i][3-i] == 'X':
                o_winning = False
            elif board[i][3-i] == 'O':
                x_winning = False
            elif board[i][3-i] == '.':
                found_blank = True
                o_winning = x_winning = False
                break
        
        if x_winning:
            x_won = True
            done = True
        elif o_winning:
            o_won = True
            done = True

    # Final

    if o_won:
        print "Case #%d: O won" % (c + 1)
    elif x_won:
        print "Case #%d: X won" % (c + 1)
    else:
        if found_blank:
            print "Case #%d: Game has not completed" % (c + 1)
        else:
            print "Case #%d: Draw" % (c + 1)

fin.close()
