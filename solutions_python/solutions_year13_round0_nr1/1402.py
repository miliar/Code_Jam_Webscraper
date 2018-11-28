numcases = int(raw_input())

for case in range(numcases):
    board = [raw_input() for x in range(4)]
    print "Case #%d:" % (case+1),
    slices = board + [''.join([board[x][i] for x in range(4)]) for i in range(4)] + [''.join([board[j][j] for j in range(4)])] + [''.join([board[j][3-j] for j in range(4)])]
    finished = False
    for s in slices:
        if s.count('.') != 0:
            continue
        if s.count('X') == 0:
            print "O won"
            finished = True
            break
        if s.count('O') == 0:
            print "X won"
            finished = True
            break
    if not finished:
        board = ''.join(board)
        if board.count('.') == 0:
            print "Draw" 
        else:
            print "Game has not completed"
    if (case != numcases-1):
        raw_input()