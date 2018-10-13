i = int(raw_input())
j = 0
x_win = ['XXXX','TXXX','XTXX','XXTX','XXXT']
o_win = ['OOOO','TOOO','OTOO','OOTO','OOOT']
for j in range(i):
    board = []
    r = False
    is_empty = False
    for k in range(4):
        line = raw_input()
        if not is_empty and '.' in line:
            is_empty = True;
        if not r:
            if line in x_win:
                print 'Case #%d: X won' % (j+1)
                r = True
            if line in o_win:
                print 'Case #%d: O won' % (j+1)
                r = True
            board += [line]
    raw_input()
    if not r:
        dia_1 = ''
        dia_2 = ''
        for k in range(4):
            line = ''
            for l in range(4):
                line +=  board[l][k]
            if line in x_win:
                print 'Case #%d: X won' % (j+1)
                r = True; break
            if line in o_win:
                print 'Case #%d: O won' % (j+1)
                r = True; break
            dia_1 += board[k][k]
            dia_2 += board[k][3-k]

        if not r:
            if dia_1 in x_win:
                print 'Case #%d: X won' % (j+1); r = True
            if dia_2 in x_win:
                print 'Case #%d: X won' % (j+1); r = True
            if dia_1 in o_win:
                print 'Case #%d: O won' % (j+1); r = True
            if dia_2 in o_win:
                print 'Case #%d: O won' % (j+1); r = True
    if not r:
        if is_empty:
            print 'Case #%d: Game has not completed' % (j+1)
        else:
            print 'Case #%d: Draw' % (j+1)
