
from copy import deepcopy
def isWon(board): #board is 0s and 1s
    #check rows
    for row in board:
        if sum(row)==4:
            return True
    #check cols
    for colindex in range(len(board[0])):
        num = 0
        for rowindex in range(len(board)):
            num+=board[rowindex][colindex]
        if num==4:
            return True
    #check diag 1
    num=0
    num2=0
    for index in range(4):
        num+=board[index][index]
        num2+=board[3-index][index]
    if num==4 or num2==4:
        return True
    return False

def hasEmpty(board): #does it contain any 0s
    for row in board:
        for col in row:
            if col==0:
                return True
    return False

def extractBoard( boardstrings):
    board = [ [0]*4 for a in range(4) ]
    for a in range(4):
        for b in range(4):
            if boardstrings[a][b]=='X':
                board[a][b] = 1
            elif boardstrings[a][b]=='O':
                board[a][b] = 2
            elif boardstrings[a][b] == '.':
                board[a][b] = 0
            elif boardstrings[a][b] == 'T':
                board[a][b] = 3
    return board
                
data = [line.strip() for line in open("input.txt")]
numBoards = int(data[0])
output = []
for a in range(numBoards): #for each board
    start = 1+5*a
    board = extractBoard( data[start:start+4])
    #print "board", board
    ##0 = ., 1 = X, 2 = 0, T = 3
    xboard = deepcopy(board)
    for rowindex in range(len(xboard)):
        for colindex in range(len(xboard[0])):
            if xboard[rowindex][colindex]>=2:
                xboard[rowindex][colindex]-=2
    #print "xboard", xboard
    yboard = deepcopy(board)
    for rowindex in range(len(yboard)):
        for colindex in range(len(yboard[0])):
            if yboard[rowindex][colindex]==3:
                yboard[rowindex][colindex] = 1
            elif yboard[rowindex][colindex]>=0:
                yboard[rowindex][colindex] -= 1

    #print 'yboard', yboard
    
    if isWon(xboard):
        output.append("X won")
    elif isWon(yboard):
        output.append("O won")
    elif hasEmpty(board):
        output.append("Game has not completed")
    else:
        output.append("Draw")

f = open("output.txt", 'w')
for i in range(len(output)):
    f.write("Case #"+str(i+1)+": "+output[i]+"\n")
f.close()
#print "output", output
