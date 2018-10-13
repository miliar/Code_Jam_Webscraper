def checkLine(line):
    if line[0] != 'T':
        player = line[0]
    else:
        player = line[1]
    if player == '.':
        return player
    for i in range(4):
        if line[i] != player and line[i]!='T':
            if line[i] == '.':
                return '.'
            else:
                return None
    else:
        return player


def checkWin(board):
    full_board = True
    #check row
    for i in range(4):
        status = checkLine([board[i][j] for j in range(4)])
        if not status:
            continue
        if status == '.':
            full_board = False
            continue
        return status


    #check column
    for i in range(4):
        status = checkLine([board[j][i] for j in range(4)])
        if not status:
            continue
        if status == '.':
            full_board = False
            continue
        return status

    #check diagonal
    diagonal = [[board[i][i] for i in range(4)], [board[i][3-i] for i in range(4)]]
    for i in diagonal:
        status = checkLine(i)
        if not status:
            continue
        if status == '.':
            full_board = False
            continue
        return status
    if full_board:
        return 'D'
    else:
        return None

with open('input.txt','r') as inf:
    with open('output.txt','w') as ouf:
        n = int(inf.readline().strip())
        for t in xrange(n):
            board = [None for _ in range(4)]
            for i in xrange(4):
                board[i] = list(inf.readline().strip())
            inf.readline()
            status = checkWin(board)
            result = 'Case #%i: '%(t+1)
            if status == 'X' or status == 'O':
                result += '%s won'%status
            elif status=='D':
                result += 'Draw'
            elif status==None:
                result += 'Game has not completed'
            ouf.write('%s\n'%result)
