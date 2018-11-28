def getOutput(board,m):
    transpose = map(list,zip(*board))
    flag = 0
    minVal = []
    minV = -1
    maxV = 1
    for column in transpose:
        minV = min(column)
        maxV = max(column)
        #print minV,maxV
        if minV == maxV:
            if flag == 0:
                flag = 1
        else:
            flag = -1 
            count = 0
            for val in column:
                if val == minV:
                    minVal.append((minV,count))
                count = count + 1
    
    if flag == 1:
        #print 'Stage 1'
        return ' YES'  
    
          
    for val in minVal:
        #print val
        if board[val[1]].count(val[0]) == m:
            flag = 1
        else:
            flag = -1
            break
    #print 'Stage 2'
    if flag == 1:
        return ' YES' 
    else:
        return ' NO'
        
if __name__ == "__main__":
    t = input()
    
    orig = t
    output = []
    #print t
    while True:
        gridsize = [int(j) for j in raw_input().strip().split()]
        #print gridsize
        n = gridsize[0]
        m = gridsize[1]
        #print n,m
        board = []       
        for i in xrange(0,n):
            j = raw_input().strip().split()
            board.append(j)
        j = 'Case #'+str(orig-t+1)+':'+getOutput(board,m)
        output.append(j)
        #print board
        t =t -1
        if t == 0:
            break
    for val in output:
        print val