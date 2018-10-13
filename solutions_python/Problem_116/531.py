fin  = open('A-large.in', 'r')
fout = open('A-large.out', 'w')

def evaluateboard():
    board = []
    for i in range(4):
        l = fin.readline().strip('\n')
        if l == '':
            l = fin.readline().strip('\n')
        board.append(list(l))

    if(checkWin('X', board)): return 'X won'
    if(checkWin('O', board)): return 'O won'
    
    for line in board:
        if '.' in line:
            return 'Game has not completed'
        
    return 'Draw'
    
def checkWin(c, board):
    for line in board:
        l = [x for x in line if x == c or x == 'T']
        if len(l) == 4:
            return True
     
    tboard = [[l[j] for l in board] for j in range(4)]
    for line in tboard:
        l = [x for x in line if x == c or x == 'T']
        if len(l) == 4:
            return True
        
    l = [x for x in [board[i][i] for i in range(4)] if x == c or x == 'T']
    if len(l) == 4:
        return True
    
    m = [board[i][j] for i in range(4) for j in range(4) if i + j == 3]
    l = [x for x in m if x == c or x == 'T']
    if len(l) == 4:
        return True
    
    return False 
    
if __name__ == '__main__':
    count = fin.readline()
    for j in range(int(count)):
        fout.write('Case #{0}: {1}\n'.format(j + 1, evaluateboard()))

    fin.close()
    fout.close()
    
