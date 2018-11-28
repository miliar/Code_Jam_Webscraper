from sys import stdin, stdout
lines = stdin.read().split('\n')
ntests = int(lines.pop(0))

for test in range(ntests):
    stdout.write("Case #"+str(test+1)+": ")
    board = []
    for i in range(4):
        board.append(lines.pop(0))
    winner = ''
    #print board
    for row in range(4):
        rowsum = sum(map(ord,board[row]))
        #print rowsum
        if rowsum in [348,352]: winner = 'X'
        elif rowsum in [321,316]: winner = 'O'
    for col in range(4):
        colsum = sum(map(ord,[board[i][col] for i in range(4)])) 
        #print colsum
        if colsum in [348,352]: winner = 'X'
        elif colsum in [321,316]: winner = 'O'
    lrdsum = sum(map(ord,[board[i][i] for i in range(4)]))
    rldsum = sum(map(ord,[board[i][3-i] for i in range(4)]))
    #print lrdsum, rldsum
    if lrdsum in [348,352]: winner = 'X'
    elif lrdsum in [321,316]: winner = 'O'
    elif rldsum in [348,352]: winner = 'X'
    elif rldsum in [321,316]: winner = 'O'
    if winner: stdout.write(winner+ " won\n")
    else:
        if min(map(min,board)) == '.': stdout.write("Game has not completed\n")
        else: stdout.write("Draw\n")
    lines.pop(0)
