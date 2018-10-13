def parse_sample():
    f = open('lm_sample.txt', 'r+')
    f2 = open('lm_sample_out.txt', 'r+')
    
    rounds = int(f.readline())
    
    for i in range(rounds):
        line = f.readline().split(" ")
        line = (int(line[0]), int(line[1]))
        lines = []
        for i2 in range(line[0]):
            lines.append(f.readline().strip().split(" "))
        print ("Case #" + str(i+1) + ": " + solveboard(lines))
        f2.write ("Case #" + str(i+1) + ": " + solveboard(lines))
    f.close()
    f2.close()

def parse_small():
    f = open('lm_small.txt', 'r+')
    f2 = open('lm_small_out.txt', 'r+')
    
    rounds = int(f.readline())
    
    for i in range(rounds):
        line = f.readline().split(" ")
        line = (int(line[0]), int(line[1]))
        lines = []
        for i2 in range(line[0]):
            lines.append(f.readline().strip().split(" "))
        print ("Case #" + str(i+1) + ": " + solveboard(lines))
        f2.write ("Case #" + str(i+1) + ": " + solveboard(lines) + "\n")
    f.close()
    f2.close()

def parse_large():
    f = open('lm_large.txt', 'r+')
    f2 = open('lm_large_out.txt', 'r+')
    
    rounds = int(f.readline())
    
    for i in range(rounds):
        line = f.readline().split(" ")
        line = (int(line[0]), int(line[1]))
        lines = []
        for i2 in range(line[0]):
            lines.append(f.readline().strip().split(" "))
        # print ("Case #" + str(i+1) + ": " + solveboard(lines))
        f2.write ("Case #" + str(i+1) + ": " + solveboard(lines) + "\n")
    f.close()
    f2.close()

def solveboard(board):
    # print (board)
    if len(board) == 0:
        return "YES"
    if len(board[0]) == 0:
        return "YES"
    smallestheight = 100
    smallestheightcoord = (0,0)
    for i in range(len(board)):
        for i2 in range(len(board[i])):
            if int(board[i][i2]) < smallestheight:
                smallestheight = int(board[i][i2])
                smallestheightcoord = (i, i2)
    if columnequal(smallestheightcoord[0], board):
        return solveboard(removerow(smallestheightcoord[0], board))
    elif rowequal(smallestheightcoord[1], board):
        return solveboard(removecolumn(smallestheightcoord[1], board))
    else:
        return "NO"

def rowequal(i, board):
    x = board[0][i]
    for i2 in range(len(board)):
        if board[i2][i] != x:
            return False
    return True

def columnequal(i, board):
    x = board[i][0]
    for i2 in range(len(board[0])):
        if board[i][i2] != x:
            return False
    return True

def removerow(i, board):
    board.pop(i)
    return board

def removecolumn(i, board):
    for i2 in range(len(board)):
        board[i2].pop(i)
    return board
