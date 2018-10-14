def win(cells):
    t = cells.count('T')
    if t + cells.count('X') == 4:
        return 'X'
    if t + cells.count('O') == 4:
        return 'O'
    return None

cases = input()
for case in range(1, cases + 1):
    not_full = False
    board = list()
    for _ in range(4):
        r = raw_input()
        if r.count('.') > 0:
            not_full = True
        board.append(r)
    done = False
    # Horiz
    for row in board:
        result = win(row)
        if result == 'X' or result == 'O':
            print "Case #%d: %s won" % (case, result)
            done = True
            break
    # Vert
    if not done:
        for i in range(4):
            col = "".join([board[j][i] for j in range(4)])
            result = win(col)
            if result == 'X' or result == 'O':
                print "Case #%d: %s won" % (case, result)
                done = True
                break
    # Diag1
    if not done:
        diag1 = "".join([board[i][i] for i in range(4)])
        result = win(diag1)
        if result == 'X' or result == 'O':
            print "Case #%d: %s won" % (case, result)
            done = True
    # Diag2
    if not done:
        diag2 = "".join([board[3 - i][i] for i in range(4)])
        result = win(diag2)
        if result == 'X' or result == 'O':
            print "Case #%d: %s won" % (case, result)
            done = True
    if not done:
        if not_full:
            print "Case #%d: Game has not completed" % case
        else:
            print "Case #%d: Draw" % case
    if case != cases:
        raw_input() # Get extra line