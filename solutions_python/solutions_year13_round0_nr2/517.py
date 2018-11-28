def isPossible(board):
    rowheights = [0]*len(board)
    colheights = [0]*len(board[0])
    for rowi in range(len(board)):
        rowheights[rowi] = max(board[rowi])

    for coli in range(len(board[0])):
        maxh = 0
        for rowi in range(len(board)):
            if board[rowi][coli] > maxh:
                maxh = board[rowi][coli]
        colheights[coli] = maxh

    #print rowheights, colheights
    for rowi in range(len(board)):
        for coli in range(len(board[0])):
            temp = board[rowi][coli]
            if temp < rowheights[rowi] and temp < colheights[coli]:
                #print 'false at ',rowi, coli
                return False
    return True

data = [line.strip() for line in open("input.txt")]
numBoards = int(data[0])
output = []
lineindex = 1 #always point to next read
for a in range(numBoards): #for each board
    line = [int(token) for token in data[lineindex].split()]
    nrows = line[0]
    ncols = line[1]
    board = [0]*nrows
    for a in range(nrows):
        board[a] = [int(token) for token in data[lineindex+a+1].split()]
    #print "board", board
    if isPossible( board ):
        output.append("YES")
    else:
        output.append("NO")
        
    lineindex+=nrows+1

#print "output", output

f = open("output.txt", 'w')
for i in range(len(output)):
    f.write("Case #"+str(i+1)+": "+output[i]+"\n")
f.close()
                      
