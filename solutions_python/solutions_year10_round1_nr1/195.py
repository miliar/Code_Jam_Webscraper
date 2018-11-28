#!/usr/bin/python

def row_k(board,p,N,K,i,j):
    if(j+K > N):
        return False
    for k in range(0,K):
        if(board[i][j+k] != p):
            return False
    return True

def col_k(board,p,N,K,i,j):
    if(i+K > N):
        return False
    for k in range(0,K):
        if(board[i+k][j] != p):
            return False
    return True


def leftDiagonal_k(board,p,N,K,i,j):
    if(i-K+1 < 0):
        return False
    if(j-K+1 < 0):
        return False
    for k in range(0,K):
        if(board[i-k][j-k] != p):
            return False
    return True

def rightDiagonal_k(board,p,N,K,i,j):
    if(i+K > N):
        return False
    if(j+K > N):
        return False
    for k in range(0,K):
        if(board[i+k][j+k] != p):
            return False
    return True


def CheckWin(board,p,N,K):
    for i in range(0,N):
        for j in range(0,N):
            if(board[i][j]==p):
                if(row_k(board,p,N,K,i,j)):
                    return True
                elif(col_k(board,p,N,K,i,j)):
                    return True
                elif(leftDiagonal_k(board,p,N,K,i,j)):
                    return True
                elif(rightDiagonal_k(board,p,N,K,i,j)):
                    return True
                
def rearrange(l,N):
    i = N-1
    while(i>=0 and l[i]!='.'):
        i = i-1
    lDot=i
    while(i>=0):
        if(l[i] != '.'):
            l[lDot]=l[i]
            l[i]='.'
            lDot=lDot-1
        i = i-1
    return l
    
def getColumn(board,N,col):
    l = []
    i=N-1
    while i >= 0:
        l.append(board[i][col])
        i = i-1
    return l

def Rotate(board,N):
    for i in range(0,N):
        board[i] = rearrange(board[i],N)
    
    board1 = []
    for i in range(0,N):
        board1.append(getColumn(board,N,i))
        
    return board1
    

filename=raw_input("Enter the file name : ")
inFilename=filename+".in"
outFilename=filename+".out"
infile=open(inFilename)     
outfile = open(outFilename,"w")

C = int(infile.readline())
cases = 1
while(cases <= C):
    inStr  = infile.readline()
    inList = inStr.split()
    N = int(inList[0])
    K = int(inList[1])
    
    board = []
    for i in range(0,N):
        inStr  = infile.readline()
        inList = []
        for i in range(0,N):
            inList.append(inStr[i])
        board.append(inList)

        
 
#    print board
    
    board=Rotate(board,N)
    R=CheckWin(board,'R',N,K)
    B=CheckWin(board,'B',N,K)

    if(R and B):
        oStr="Both"
    elif(R):
        oStr="Red"
    elif(B):
        oStr="Blue"
    else:
        oStr="Neither"

    outStr = "Case #%d: " %(cases) +oStr+"\n"
 #   outStr=outStr+'**************************************************\n\n'
    outfile.write(outStr)
    cases = cases+1
