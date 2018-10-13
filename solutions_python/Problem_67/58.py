def decay(board):
    dieList = set()
    bornList = set()
    for x,y in board:
        if (x,y-1) not in board and (x-1,y) not in board:
            dieList.add((x,y))
        
        if (x-1,y+1) in board and (x,y+1) not in board: 
            bornList.add((x,y+1))
        elif (x+1,y-1) in board and (x+1,y) not in board:
            bornList.add((x+1,y))
            
    for x,y in dieList:
        del board[(x,y)]
    for x,y in bornList:
        board[x,y] = 1

C = int(raw_input())

board = {}
for c in range(1, C + 1):
        R = int(raw_input())
        for _ in range(R):
            x1,y1,x2,y2 = map(int, raw_input().split())
            for i in range(x1,x2+1):
                for j in range(y1,y2+1):
                    board[(i,j)] = 1
        
        counter = 0
        while len(board) > 0:
            decay(board)
            counter += 1
                                 
        print "Case #%d: %s" % (c, counter)
    