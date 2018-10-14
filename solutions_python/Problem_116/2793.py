#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Demo-User
#
# Created:     13/04/2013
# Copyright:   (c) Demo-User 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------


SIZE=4

EX='X'
OR='O'
TE='T'
DOT='.'

nEX=1
nOR=0
nTE=0.5
nDOT=SIZE+1

def main():

    file=open('A-small-attempt1.in')
    lines=file.readlines()
    file.close()
    inp=int(lines.pop(0))
    matIn=[]
    for x in range(0,(inp*SIZE)+(inp)):
        l=lines[x]
        if (l!='\n' and l!=''):
            matIn.append(l)
    file=open('1.out','w+')
    for x in range(0,inp*SIZE,4):
        mat=[]
        mat.append(matIn[x])
        mat.append(matIn[x+1])
        mat.append(matIn[x+2])
        mat.append(matIn[x+3])
        nmat=conMat(mat)
        winner=getWin(nmat)

        if winner=='NOT':
            print('Case #'+str(x//SIZE+1)+":",'Game has not completed',file=file)
        elif(winner=="Draw"):
            print('Case #'+str(x//SIZE+1)+":",winner,file=file)
        else:
            print('Case #'+str(x//SIZE+1)+":",winner,'won',file=file)
    file.close()



def conMat(mat):
    nmat=[]
    for x in range(SIZE):
        nmat.append([0]*SIZE)
    for x in range(SIZE):
        for y in range(SIZE):
            if(mat[x][y]==EX):
                nmat[x][y]=nEX
            elif(mat[x][y]==OR):
                nmat[x][y]=nOR
            elif(mat[x][y]==TE):
                nmat[x][y]=nTE
            elif(mat[x][y]==DOT):
                nmat[x][y]=nDOT

    return nmat

def getWin(mat):

    winner='Draw'
    xRawSum=[0]*SIZE
    yRawSum=[0]*SIZE
    dia,idea=0,0
    for x in range(SIZE):
        for y in range(SIZE):
            xRawSum[x]+=mat[x][y]
            yRawSum[x]+=mat[y][x]
            if x==y :
                dia+=mat[x][y]
            if x+y==SIZE-1:
                idea+=mat[x][y]

    for x in range(SIZE):
        if(xRawSum[x]==0 or yRawSum[x]==0 or dia==0 or idea==0 or xRawSum[x]==0.5 or yRawSum[x]==0.5 or dia==0.5 or idea==0.5):
            winner=OR
            break
        elif(xRawSum[x]==SIZE or yRawSum[x]==SIZE or dia==SIZE or idea==SIZE or xRawSum[x]==SIZE-0.5 or yRawSum[x]==SIZE-0.5 or dia==SIZE-0.5 or idea==SIZE-0.5):
            winner=EX
            break
        elif(xRawSum[x]>SIZE and yRawSum[x]>SIZE and dia>SIZE and idea>SIZE):
            winner='NOT'
    return winner

if __name__ == '__main__':
    main()


