import os
def rowWin(symbol,board):
 
 
    for r in range(0,4):
        count = 0
        for c in range(0,4):
            if(board[r][c] == symbol or board[r][c] == 'T'):
                count = count + 1
            if(count == 4):
                return True

    return False

def colWin(symbol,board):

 
    for c in range(0,4):
        count = 0
        for r in range(0,4):
            if(board[r][c] == symbol or board[r][c] == 'T'):
                count = count + 1
            if(count == 4):
                return True

    return False

def diagonalWin(symbol,board):
    count = 0
    for i in range(0,4):
        if(board[i][i] == symbol or board[i][i] == 'T'):
            count = count +1
    if(count == 4):
        return True
    count = 0
   
    r=0
    c=3
    while(r< 4):
        if(board[r][c] == symbol or board[r][c] == 'T'):
            count = count + 1
        r += 1
        c -=1
    if(count == 4):
        return True
    return False
        
        
        
def win(symbol,board):

    if(colWin(symbol,board) or rowWin(symbol,board) or diagonalWin(symbol,board)):
        return True
    return False

def find(board,key):
     for index, sublist in enumerate(lists):
       if sublist[0] == key:
            return index
f = open('A-large.in')
lines = f.readlines()
f.close()

numcases = int(lines[0])



board = [[0 for x in xrange(4)] for x in xrange(4)] 
f = open("A-large.out",'w')
j = 1
for i in range(1,numcases+1):
   
       board[0] = list(lines[j].strip())
       board[1] = list(lines[j+1].strip())
       board[2] = list(lines[j+2].strip())
       board[3] = list(lines[j+3].strip())
       if(win('O',board)):
           f.write("Case #{0}: O won\n".format(i))
       elif(win('X',board)):
           f.write("Case #{0}: X won\n".format(i))
       elif(not ('.' in board[0]) and not ('.' in board[1]) and not ('.' in board[2]) and not('.' in board[3])): 
           f.write("Case #{0}: Draw\n".format(i))
       else:
           f.write("Case #{0}: Game has not completed\n".format(i))
            
       j += 5
    

f.close()  
