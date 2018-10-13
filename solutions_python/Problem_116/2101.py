#!C:\Python27\python

case_num = int(raw_input())

for case in range(1, case_num+1):
    row_win = False
    col_win = False
    diag_win = False
    draw = True
    board = []

    for i in range(4):
        board.append(raw_input())

    raw_input()	#Read new line after test case

    for row in board:
        if '.' in row:
            draw = False

        if row == 'XXXX' or ''.join(sorted(row)) == 'TXXX':
            print "Case #" + str(case) + ": X won"
            row_win = True
            break
        elif row == 'OOOO' or ''.join(sorted(row)) == 'OOOT':
            print "Case #" + str(case) + ": O won"
            row_win = True
            break

    if row_win:
        continue

    for col in range(4):
        curr_col = ''.join([board[0][col], board[1][col], board[2][col], board[3][col]])
        if curr_col == 'XXXX' or ''.join(sorted(curr_col)) == 'TXXX':
            print "Case #" + str(case) + ": X won"
            col_win = True
            break
        elif curr_col == 'OOOO' or ''.join(sorted(curr_col)) == 'OOOT':
            print "Case #" + str(case) + ": O won"
            col_win = True
            break

    if col_win:
        continue

    diag1 = ''.join([board[0][0], board[1][1], board[2][2], board[3][3]])
    if diag1 == 'XXXX' or ''.join(sorted(diag1)) == 'TXXX':
        print "Case #" + str(case) + ": X won"
        continue
    elif diag1 == 'OOOO' or ''.join(sorted(diag1)) == 'OOOT':
        print "Case #" + str(case) + ": O won"
        continue

    diag2 = ''.join([board[3][0], board[2][1], board[1][2], board[0][3]])
    if diag2 == 'XXXX' or ''.join(sorted(diag2)) == 'TXXX':
        print "Case #" + str(case) + ": X won"
        continue
    elif diag2 == 'OOOO' or ''.join(sorted(diag2)) == 'OOOT':
        print "Case #" + str(case) + ": O won"
        continue

    if draw:
        print "Case #" + str(case) + ": Draw"
    else:
        print "Case #" + str(case) + ": Game has not completed"
