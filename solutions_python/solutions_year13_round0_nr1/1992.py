def printBoard(B):
    print B[0],  B[1],  B[2],  B[3]
    print B[4],  B[5],  B[6],  B[7]
    print B[8],  B[9],  B[10], B[11]
    print B[12], B[13], B[14], B[15]
    
def checkBoard(B):
    
    result = ""
    won = [
           [0,5,10,15], [3,6,9,12],
           [0,1,2,3],   [4,5,6,7],  [8,9,10,11], [12,13,14,15],
           [0,4,8,12],  [1,5,9,13], [2,6,10,14], [3,7,11,15]
          ]

    #X
    temp = B[:]
    for i in range(0,len(temp)):
        if temp[i] == 'T':
            temp[i] = 'X'
    for i in range(0,len(won)):
        if(temp[won[i][0]] == temp[won[i][1]] == temp[won[i][2]] == temp[won[i][3]] == 'X'):
            result = "X won"
    #Y
    temp = B[:]
    for i in range(0,len(temp)):
        if temp[i] == 'T':
            temp[i] = 'O'
    for i in range(0,len(won)):
        if(temp[won[i][0]] == temp[won[i][1]] == temp[won[i][2]] == temp[won[i][3]] == 'O'):
            result = "O won"

    #Draw or Game has not completed
    complete = 0
    if(result == "") :
        for i in range(0,len(B)):
            if(B[i] != '.'):
                complete = complete + 1
        if(complete == 16):
            result = "Draw"
        else:
            result = "Game has not completed"
        
    return result
    

#-----------------------------------------------------------------------------

f = open("A-small-attempt1.in","r")
x = f.readline()
x = x.split()
N  = int(x[0])


Boards = []
for i in range(0,N):
    board = []
    for j in range(0,4):
        x = f.readline()
        for k in range(0, len(x)):
            if(x[k] != '\n'):
                board.append(x[k])
    x = f.readline() #skip line
    Boards.append(board)

for i in range(0,N):
    #printBoard(Boards[i])
    s = "Case #" + str(i+1) + ":"
    print s, checkBoard(Boards[i])
    

