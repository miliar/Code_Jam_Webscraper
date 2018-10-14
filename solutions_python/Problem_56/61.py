def rotate(board,n):
    new_board = []
    for i in xrange(0,n):
        s = ""
        for j in xrange(n-1,-1,-1):
            s += board[j][i]
        new_board.append(s)
    return new_board


t = int(raw_input())
for case in xrange(0,t):
    n,k = [int(x) for x in raw_input().split(" ")]
    board = []
    for j in xrange(0,n):
        board.append(raw_input().strip())

    new_board = rotate(board,n)
    new_board = rotate(new_board,n)
    for i in xrange(0,n):
        new_board[i] = new_board[i].replace(".","")
        new_board[i] = new_board[i].ljust(n,".")

    red = False
    blue = False
    
    for i in xrange(0,n):
        for j in xrange(0,n):
            c = new_board[i][j]
            if c == ".": continue
            if c == "R" and red: continue
            if c == "B" and blue: continue
            dx = [0,1,1,1]
            dy = [1,0,1,-1]    
            for d in xrange(0,4):
                x = i
                y = j
                count = 0
                while (x<n) and (y<n) and (new_board[x][y] == c):
                    count +=1
                    x += dx[d]
                    y += dy[d]

                if c == "R" and count >= k:
                    red = True
                if c == "B" and count >= k:
                    blue = True            
        
    if red and blue:
        print "Case #%d: Both" % (case+1)
    elif red and not blue:
        print "Case #%d: Red" % (case+1)
    elif not red and blue:
        print "Case #%d: Blue" % (case+1)
    else:
        print "Case #%d: Neither" % (case+1)
