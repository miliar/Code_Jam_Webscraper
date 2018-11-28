f = open("A-large.in")

def checkResult(board, color, size, win):
        found = checkHor(board, color, size, win)
        if found:
                return True
        found = checkVer(board, color, size, win)
        if found:
                return True
        found = checkD(board, color, size, win)
        if found:
                return True
        found = checkDO(board, color, size, win)
        if found:
                return True          
        return False

def checkHor(board, color, size, win):
    for i in range(size):
        for j in range(size-win+1):
            if board[i][j] == color:
                found = True
                k = 1
                while k < win and found == True:
                    found = checkColor(board, color, i, j+k)
                    k = k + 1
                if found:
                    return True
    return False

def checkVer(board, color, size, win):
    for i in range(size-win+1):
        for j in range(size):
            if board[i][j] == color:
                found = True
                k = 1
                while k < win and found == True:
                    found = checkColor(board, color, i+k, j)
                    k = k + 1
                if found:
                    return True
    return False

def checkD(board, color, size, win):
    for i in range(size-win+1):
        for j in range(win-1, size):
            if board[i][j] == color:
                found = True
                k = 1
                while k < win and found == True:
                    found = checkColor(board, color, i+k, j-k)
                    k = k + 1
                if found:
                    return True
    return False

def checkDO(board, color, size, win):
    for i in range(size-win+1):
        for j in range(size-win+1):
            if board[i][j] == color:
                found = True
                k = 1
                while k < win and found == True:
                    found = checkColor(board, color, i+k, j+k)
                    k = k + 1
                if found:
                    return True
    return False    
        

def checkColor(board, color, row, col):
    if board[row][col] == color:
        return True
    return False
            

def printBoard(board, size):
    for i in range(size):
        row = ""
        for j in range(size):
            row += board[i][j]
        print row

def rotateBoard(board, size):
    newBoard = []
    for i in range(size):
        checkRow(board[i], size)

def checkRow(row, size):
    found = False
    for i in range(size-1):
        if row[i] != "." and row[i+1] == ".":
            row[i+1] = row[i]
            row[i] = "."
            found = True
    if found:
        checkRow(row, size)
        

case = int(f.readline())
string = ''
for k in range(case):
    in_put = f.readline().rstrip("\n").split()
    size = int(in_put[0])
    #print size
    win = int(in_put[1])
    #print win
    board = []
    for i in range(size):
        rowstring = f.readline()
        row = []
        for j in range(size):
            c = rowstring[j]
            if c != "\n":
                row.append(c)
        board.append(row)
    #print k
    rotateBoard(board, size)
    #printBoard(board, size)
    b = checkResult(board, "B", size, win)
    r = checkResult(board, "R", size, win)
    if b and r:
        winning = "Both"
    elif b and not r:
        winning = "Blue"
    elif r and not b:
        winning = "Red"
    else:
        winning = "Neither"
    
    string += "Case #" + str(k+1) + ": " + winning + "\n"


o = open('A-large-o.in', 'w')
o.write(string)
o.close()
