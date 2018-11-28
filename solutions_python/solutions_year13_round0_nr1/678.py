"""
Tic-Tac-Toe-Tomek
"""
def analyze_board(board):
    rows = board[:]
    for i in xrange(4):
        rows.append([x[i] for x in board])
    rows.append([board[0][0],board[1][1],board[2][2],board[3][3]])
    rows.append([board[0][3],board[1][2],board[2][1],board[3][0]])
    empties = False
    for row in rows:
        t = row.count("T")
        if(t+row.count("O")==4):
            return "O won"
        elif(t+row.count("X")==4):
            return "X won"
        elif(not empties and row.count(".")>0):
            empties = True
    if(empties):
        return "Game has not completed"
    else:
        return "Draw"
    
f = open("input1.txt", "rb")
g = open("output1.txt", "wb")
t = int(f.readline().strip())
for i in xrange(t):
    board = []
    for j in xrange(4):
        board.append(list(f.readline().strip()))
    f.readline()
    status = analyze_board(board)
    g.write("Case #%d: %s" % (i+1, status))
    g.write("\n")