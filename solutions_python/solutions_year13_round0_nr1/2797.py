'''
Created on Apr 13, 2013

@author: Kenneth
'''
def won(board,x,y,side,summ,xD,yD,):
    if(side == '.' or side == 'T'):
        return False
    
    if summ == 4:
        return True
    if(x > 3 or y>3 or x <0 or y < 0):
        return False
    if(board[x][y] == side or board[x][y] == 'T'):
        summ = summ+1
        if won(board,x+xD,y+yD,side,summ,xD,yD):
            print "(%d,%d)"%(x,y)
            print "(%c,%c)"%(board[x][y],side)
            return True
    return False
def solve(board):
    for i in xrange(0,4):
        
        if won(board,i,0,board[i][0],0,0,1) or won(board,i,0,board[i][0],0,1,1) or won(board,i,0,board[i][0],0,1,0) or won(board,i,0,board[i][0],0,1,-1) :
            if(board[i][0] == 'X'):
                return 1
            else :
                return 2
        if won(board,0,i,board[0][i],0,0,1) or won(board,0,i,board[0][i],0,1,0) or won(board,0,i,board[0][i],0,1,1)or won(board,0,i,board[0][i],0,1,-1):
            if(board[0][i] == 'X'):
                return 1
            else:
                return 2
    for i in xrange(0,4):
        for j in xrange(0,4):
            if board[i][j] == '.':
                return -1
    return 0
        



if __name__ == '__main__':
    output = open ("C:\\jam\\tic\\out.txt",'w')
    inp = open ("C:\\jam\\tic\\A-small-attempt1.in",'r')
    num = int(inp.readline())
    for i in xrange(1,num+1):
        print i
        board = []
        for j in xrange(0,4):
            row = []
            line = inp.readline()
            for char in line:
                row.append(char)
            board.append(row)
        inp.readline()
        res = solve(board)
        res2 = ''
        if res == -1 :
            res2 = 'Game has not completed'
        elif res == 0:
            res2 = 'Draw'
        elif res == 1:
            res2 = 'X won'
        elif res == 2:
            res2 = 'O won'
        output.write("Case #%d: %s" %(i,res2 ))
        output.write("\n")
    output.close()
    inp.close()