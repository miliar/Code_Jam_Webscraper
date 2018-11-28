'''
Created on Apr 13, 2013

@author: melegy
'''
import copy
inf = open('in')
outf = open ('out','w')

notyet=False
def isequal(x,y):
    if x==y or x=='T' or y=='T':
        return True
def iswinpoint(board,x,y):
    if board[x][y]=='.':
        return False
    try:
        if board[x][y]==board[x][y+1]==board[x][y+2]==board[x][y+3]:
            return True
    except:
        pass
    try:
        if board[x][y]==board[x+1][y]==board[x+2][y]==board[x+3][y]:
            return True
    except:
        pass
    try:
        if board[x][y]==board[x+1][y+1]==board[x+2][y+2]==board[x+3][y+3]:
            return True
    except:
        pass
    try:
        if y<3:
            return False
        if board[x][y]==board[x+1][y-1]==board[x+2][y-2]==board[x+3][y-3]:
            return True
    except:
        pass
    return False
        
    
    
def checkBoard(board):
    notyet=False
    xboard=copy.deepcopy(board)
    for n in range(4):
        for m in range(4):
            if board[n][m]=='T':
                board[n][m]='X'
    for g in range(4):
        for h in range(4):
            if xboard[g][h]=='T':
                xboard[g][h]='O'
                
    for j in range(len(board)):
            for k in range(len(board[j])):
                if board[j][k]=='.':
                    notyet=True
                if board[j][k]=='X':
                    if iswinpoint(board,j,k) :
                        outf.write('Case #'+str(i)+': X won\n')
                        return
                if board[j][k]=='O':
                    if iswinpoint(xboard,j,k) :
                        outf.write('Case #'+str(i)+': O won\n')
                        return
    if not notyet:            
        outf.write('Case #'+str(i)+': Draw\n')   
    else:
        outf.write('Case #'+str(i)+': Game has not completed\n')
        

if __name__=="__main__":

    k=inf.readline()
    for i in range (1,int(k)+1):
        notyet=False
        board=[]
        for l in range(1,5):
            l=inf.readline().replace('\n','')
            board.append(list(l))
        checkBoard(board)
        inf.readline()
             
        
            