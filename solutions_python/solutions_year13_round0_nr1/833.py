def readboard(f):
    board = [[],[],[],[]]
    for i in range(4):
        board[i] += f.readline()
        while(board[i].count('\n')!= 0):
            board[i].remove('\n')
    return board 

def checkboard(board):
    xwin = 0
    owin = 0
    notFinished = 0
    for i in board:
        if i.count('X')+i.count('T') == 4:
            xwin = 1
        if i.count('O')+i.count('T') == 4:
            owin = 1
        if i.count('.') != 0:
            notFinished = 1
    column = [[i[j] for i in board] for j in range(4)]       
    for i in column:
        if i.count('X')+i.count('T') == 4:
            xwin = 1
        if i.count('O')+i.count('T') == 4:
            owin = 1

    cross = [board[j][j] for j in range(4)]      
    if cross.count('X')+cross.count('T') == 4:
        xwin = 1
    if cross.count('O')+cross.count('T') == 4:
        owin = 1 
                
    cross = [board[3-j][j] for j in range(4)]      
    if cross.count('X')+cross.count('T') == 4:
        xwin = 1
    if cross.count('O')+cross.count('T') == 4:
        owin = 1 
                    
    if xwin == 1 and owin == 1:
        return "Draw"
    if xwin == 1:
        return "X won"
    if owin == 1:
        return "O won"
    if notFinished == 1:
        return "Game has not completed"
    return "Draw"
def main():
    f = open("input.txt")
    counter = int(f.readline())
    result = "Draw"
    case = 1
    while case<= counter:
        board = readboard(f)
        print "Case #%s: %s"%(case,checkboard(board))
        f.readline()
        case +=1
        
main()