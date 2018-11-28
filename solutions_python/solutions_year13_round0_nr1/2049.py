def checkBoard(board):
    for el in board:
        t=0
        x=0
        o=0      
        for ch in el:
            if ch == "X": x+=1
            if ch == "O": o+=1
            if ch == "T": t+=1
        if x+t==4:
            return "X won"
        elif o+t==4: 
            return "O won"
    return False

def checkCol(board):
    col1 = ""
    col2 = ""
    col3 = ""
    col4 = ""
    for el in board:
        col1 += el[0]
        col2 += el[1]
        col3 += el[2]
        col4 += el[3]
    colboard = [col1,col2,col3,col4]
        
    return checkBoard(colboard)

def checkDiag(board):
    diag1 = board[0][0] + board[1][1] + board[2][2] + board[3][3]
    diag2 = board[0][3] + board[1][2] + board[2][1] + board[3][0]
    diagboard = [diag1,diag2]
    return checkBoard(diagboard)

def checkDraw(board):
    for el in board:
        for ch in el:
            if ch ==".": return "Game has not completed"
    
    return "Draw"

filein = open("A-large.in", "r")
fileout = open("A-large.out","w")
    
cases = int(filein.readline().strip())

case = 1
board = []
while cases>=case:
    line = filein.readline().strip()
    if line == "":
        case +=1
        continue
    else:
        board.append(line)
        board.append(filein.readline().strip())    
        board.append(filein.readline().strip())
        board.append(filein.readline().strip())
    
    results = checkBoard(board)
    if results == False: results = checkCol(board)
    if results == False: results = checkDiag(board)
    if results == False: results = checkDraw(board)

    #print("Case #" +str(case) +":", results)
    fileout.write("Case #" +str(case) +": " + results +"\n")
    results = False
    board = []
filein.close()
fileout.close()