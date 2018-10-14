def checkVector(vector):
    
    if (vector.count('X') + vector.count('T')) == 4:
        return 1
    elif (vector.count('O') + vector.count('T')) == 4:
        return -1        
    else:
        return 0
    
def getOutput(board):
    flag = 0
    for row in board:
        flag = checkVector(row)
        if flag == 1:
            return ' X won'
        elif flag == -1:
            return ' O won'
        
    
    board = map(list,zip(*board))
    #For Columns
    for row in board:
        flag = checkVector(row)
        if flag == 1:
            return ' X won'
        elif flag == -1:
            return ' O won'
    vector = []    
    for i in xrange(0,4):
        vector.append(board[i][i])
    flag = checkVector(vector)
    if flag == 1:
        return ' X won'
    elif flag == -1:
        return ' O won'
    
    vector = []    
    for i in xrange(0,4):
        vector.append(board[i][3-i])
    flag = checkVector(vector)
    if flag == 1:
        return ' X won'
    elif flag == -1:
        return ' O won'
    
    count = 0
    for row in board:
        count = count + row.count('.')
    if count == 0:
        return ' Draw'   
    if flag == 0:
        return ' Game has not completed'
    
if __name__ == "__main__":
    t = input()
    orig = t
    output = []
    #print t
    while True:
        board = [[j for j in raw_input().strip()] for i in range(4)]
        
        output.append('Case #'+str(orig-t+1)+':'+getOutput(board))
        #output.append(p)
        t = t-1
        #print board
        #print temp
        #print t
        
        if t == 0:
            break
        else:
            temp = raw_input()
            
    for val in output:
        print val
            
    