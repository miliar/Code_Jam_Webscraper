def symbolMap(c):
    if c==".":
        return 0
    if c=="X":
        return 1
    if c=="O":
        return 2
    if c=="T":
        return 3


T = int(raw_input())
for t in range(1, T+1):
    board = [ [symbolMap(x) for x in raw_input()] for x in range(4)]
    blank = raw_input()

    print "Case #"+str(t)+":",
    if max(max(sum(x%2 for x in row) for row in board),max(sum([l[i]%2 for l in board]) for i in range(4)),sum(board[i][i]%2 for i in range(4)),sum(board[i][3-i]%2 for i in range(4)))==4:
        print "X won"
    elif max(max(sum(x/2 for x in row) for row in board),max(sum([l[i]/2 for l in board]) for i in range(4)),sum(board[i][i]/2 for i in range(4)),sum(board[i][3-i]/2 for i in range(4)))==4:
        print "O won"
    elif min(min(l) for l in board)==0:
        print "Game has not completed"
    else:
        print "Draw"
