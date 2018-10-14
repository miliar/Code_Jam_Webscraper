def  readfile(filename):
    f= open(filename)
    num=int(f.next())
    tic_tac_toe=[]
    board=[]
    for line in f:
        line= line.strip()
        if len(line)>0:
            board.append(line)
        else:
            tic_tac_toe.append(board)
            board=[]
            
    tic_tac_toe.append(board)
    
    for num,  brd in enumerate(tic_tac_toe):
        if brd == []:
            continue
        case = 'Case #'+str(num+1)+":"
        win = judgeBoard(brd)
        bcomplete = isCompleted(brd)
        if win is not None:
            print case,  win,  'won'
        elif bcomplete:
            print case,  'Draw'
        else:
            print case,  'Game has not completed'

def isCompleted(board):
    for line in board:
        if '.' in line:
            return False
    return True

def judgeBoard(board):
    for line in board:
        win = whoWin(line)
        if win is not None:
            return win
    for i in range(4):
        row = ''.join(line[i] for line in board)
        win = whoWin(row)
        if win is not None:
            return win
            
    diagonal = ''
    for i in range(4):
        diagonal += board[i][i]
    win = whoWin(diagonal)
    if win is not None:
            return win
            
    anti_diagonal = ''
    for i in range(4):
        anti_diagonal += board[3-i][i]
    win = whoWin(anti_diagonal)
    if win is not None:
            return win
            
    return None
def whoWin(fourSymbols):
    sortedSymbols = "".join(sorted(fourSymbols))
    if sortedSymbols == 'XXXX' or sortedSymbols == 'TXXX':
        return 'X'
    elif sortedSymbols =='OOOO' or sortedSymbols == 'OOOT':
        return 'O'
    return None
    
if __name__ == "__main__":
    readfile("A-large.in")
    
