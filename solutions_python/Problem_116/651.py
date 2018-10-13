import re
T = int(raw_input())
for qq in xrange(1,T+1):
    board = [raw_input() for x in xrange(4)]
    raw_input()
    ans = "Game has not completed"
    owins = [False]
    xwins = [False]
    o = "[TO][TO][TO][TO]"
    x = "[TX][TX][TX][TX]"
    def go(s):
        if re.match(o,s):
            owins[0] = True
        if re.match(x,s):
            xwins[0] = True
    for i in xrange(4):
        go(board[i])
        go(board[0][i]+board[1][i]+board[2][i]+board[3][i])
    go(board[0][0]+board[1][1]+board[2][2]+board[3][3])
    go(board[0][3]+board[1][2]+board[2][1]+board[3][0])
    if owins[0]:
        ans = "O won"
    elif xwins[0]:
        ans = "X won"
    elif not any(map(lambda s:any(map(lambda c: c==".",s)),board)):
        ans = "Draw"
    print "Case #%d: %s"%(qq,ans)
