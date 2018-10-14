#!/usr/bin/env python
import copy

X='x'
O='o'
P='+'

def remove(mat, row, col,ch):
    try:
        mat[row][col].remove(ch)
    except:
        pass

def clearX(mat,row,col):
    tmp=[]
    tmp+=mat[row][col]
    for j in range(len(mat)):
        remove(mat, row, j,X)
        remove(mat, row, j,O)
    for i in range(len(mat)):
        remove(mat,i,col,X)
        remove(mat,i,col,O)
    mat[row][col]=tmp
    remove(mat,row,col,P)
    remove(mat,row,col,X)

def clearPlus(mat,row,col):
    tmp=[]
    tmp+=mat[row][col]
    s=row+col
    d=row-col 
    for i in range(len(mat)):
        for j in range(len(mat)):
            if i+j == s or i-j == d:
                remove(mat,i,j,O)
                remove(mat,i,j,P)
    mat[row][col]=tmp
    remove(mat,row,col,P)
    remove(mat,row,col,X)

def maximizeProfit(options,mat,score):
    changes=[]
    row=0
    for col in range(len(mat)):
        score+=maximizeProf(options,mat,row,col,changes)

    row=len(mat)-1
    for col in range(len(mat)):
        score+=maximizeProf(options,mat,row,col,changes)
    
    for row in range(len(mat)):
        for col in range(len(mat)):
            score+=maximizeProf(options,mat,row,col,changes)
           
    return score,changes

def maximizeProf(options, mat, row, col,changes):
    if not options[row][col]:
        return 0
    ch=options[row][col][0]
    options[row][col]=[]
    options = reduceConflicts(options,ch,row,col)
    changes += [[ch,row+1,col+1]]
    return 1 if mat[row][col] is not '.' else scoreChar(ch)

def scoreChar(ch):
    if ch == X or ch == P:
        return 1
    elif ch == O:
        return 2
    else:
        return 0

def scoreMat(mat):
    score = 0
    for i in range(len(mat)):
        for j in range(len(mat)):
            score += scoreChar(mat[i][j])
    return score

def reduceConflicts(MatrixOptions, ch, row, col):
    if ch == P:
        clearPlus(MatrixOptions, row, col)
    if ch == X:
        clearX(MatrixOptions, row, col)
    if ch == O:
        clearX(MatrixOptions, row, col)
        clearPlus(MatrixOptions, row, col)
        remove(MatrixOptions, row, col, O)
    return MatrixOptions

def solve(N,M):
    N=int(N)
    M=int(M)
    MatrixOptions = [[[O,P,X] for _ in range(N)] for __ in range(N)]
    Matrix = [['.' for _ in range(N)] for __ in range(N)]
    for _ in range(M):
        ch,rowStr,colStr = raw_input().split()
        row = int(rowStr)-1
        col = int(colStr)-1
        Matrix[row][col]=ch
        MatrixOptions = reduceConflicts(MatrixOptions, ch, row, col)
    return maximizeProfit(MatrixOptions,Matrix,scoreMat(Matrix))

if __name__ == "__main__":
    t = int(raw_input())
    for cas in xrange(1,t+1):
        score,changes = solve(*raw_input().split())
        print "Case #{}: {} {}".format(cas,score,len(changes))
        for line in changes:
            print line[0],line[1],line[2]
