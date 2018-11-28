def solve(board):
    #horiz
    for k in xrange(4):
        countX = 0
        countO = 0
        for l in xrange(4):
            if board[k][l] == "X" or board[k][l] == "T":
                countX += 1
            if board[k][l] == "O" or board[k][l] == "T":
                countO += 1
        if countO == 4:
            return "O won"
        elif countX == 4:
            return "X won"
    #vert
    for k in xrange(4):
        countX=0
        countO=0
        for l in xrange(4):
            if board[l][k] == "X" or board[l][k] == "T":
                countX+=1
            if board[l][k] == "O" or board[l][k] == "T":
                countO+=1
        if countO == 4:
            return "O won"
        elif countX == 4:
            return "X won"
    #\ diag
    s = board[0][0] + board[1][1] + board[2][2] + board[3][3]
    t = board[0][3] + board[1][2] + board[2][1] + board[3][0]
    if s.count('X') == 4 or ( s.count('X') + s.count('T') ) == 4:
        return "X won"
    if s.count('O') == 4 or ( s.count('O') + s.count('T') ) == 4:
        return "O won"
    if t.count('X') == 4 or ( t.count('X') + t.count('T') ) == 4:
        return "X won"
    if t.count('O') == 4 or ( t.count('O') + t.count('T') ) == 4:
        return "O won"
    #Complete
    for k in xrange(4):
        for l in xrange(4):
            if board[k][l] == '.':
                return "Game has not completed"
    return "Draw"
    

##    
##print solve( ["XXXX", "....", "....", "...."] )
##print solve( ["....", "XXXX","....", "...."] )
##print solve( ["....", "....","XXXX", "...."] )
##print solve( ["....", "....", "....", "XXXX"] )
##
##print solve( ["OOOO", "....", "....", "...."] )
##print solve( ["....", "OOOO","....", "...."] )
##print solve( ["....", "....","OOOO", "...."] )
##print solve( ["....", "....", "....", "OOOO"] )
##
##print solve( ["X...", "X...","X...","X..."])
##print solve( [".X..",".X..",".X..",".X.."])
##print solve( ["..X.","..X.","..X.","..X."])
##print solve( ["...X", "...X", "...X", "...X"])
##
##print solve( ["O...", "O...","O...","O..."])
##print solve( [".O..",".O..",".O..",".O.."])
##print solve( ["..O.","..O.","..O.","..O."])
##print solve( ["...O", "...O", "...O", "...O"])
##
##print solve( ["X...", ".X..", "..X.", "...X"])
##print solve( ["O...", ".O..", "..O.", "...O"])
##
##print solve( ["...X", "..X.", ".X..", "X..."])
##print solve( ["...O", "..O.", ".O..", "O..."])
##






a = open(r"D:\downloads\A-large.in", "r")
count = int(a.readline())
ans = ""
for k in xrange(count):
    board = []
    for l in xrange(4):
        board += [a.readline().strip()]
    a.readline()
    ans +=  "Case #%d: %s" % ( k+1 , solve(board) )
    if k+1<count:
        ans += "\n"

a.close()

b=open(r"D:\downloads\a-large.out", "w")
b.write(ans)
b.close()

print ans
