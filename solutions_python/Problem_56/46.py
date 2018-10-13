def read():
    sz,K = map(int,raw_input().split())
    board = []
    for i in range(sz):
        board.append(list(raw_input()))
    return board,K


def work(cases,(board,K)):
    while 1:
        update = False
        for r in range(len(board)):
            for c in range(len(board)-1):
                if board[r][c]!='.' and board[r][c+1]=='.':
                    board[r][c],board[r][c+1] = board[r][c+1],board[r][c]
                    update = True
        if not update:
            break

    bWin = False
    rWin = False
    dr = [1,0,1,1]
    dc = [0,1,-1,1]
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c]=='.': continue
            for i in range(4):
                cnt = 0
                nr = r
                nc = c
                while nr<len(board) and 0<=nc<len(board) and board[nr][nc]==board[r][c]:
                    cnt += 1
                    nr += dr[i]
                    nc += dc[i]
                if cnt>=K:
                    if board[r][c]=='B': bWin = True
                    else: rWin = True

    print "Case #%d:"%cases,
    if bWin and rWin:
        print "Both"
    elif bWin:
        print "Blue"
    elif rWin:
        print "Red"
    else:
        print "Neither"
                

for i in range(int(raw_input())):
    work(i+1,read())
