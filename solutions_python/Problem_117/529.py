global a
a=open("B-large.in","r")
def IsPossible(board):
    i=0
    while(i<len(board)):
        j=0
        while(j<len(board[i])):           
            if(isRowPath(board,i,j)==False and isColumnPath(board,i,j)==False):
                return False
            j+=1
        i+=1
    return True
def isRowPath(board,i,j):
    #first we check the right side
    isRight=True
    k=j+1
    while(k<len(board[i])):
        if(board[i][k]>board[i][j]):
            isRight=False
        k+=1
    #Left side
    isLeft=True
    k=j-1
    while(k>=0):
        if(board[i][k]>board[i][j]):
            isLeft=False
        k-=1
    return isLeft and isRight
def isColumnPath(board,i,j):
    #first we check the bottom side
    isDown=True
    k=i+1
    while(k<len(board)):
        if(board[k][j]>board[i][j]):
            isDown=False
        k+=1
    #upper side
    isUp=True
    k=i-1
    while(k>=0):
        if(board[k][j]>board[i][j]):
            isUp=False
        k-=1
    return isDown and isUp
line=a.readline()
T=int(line[:len(line)-1])
i=1
n=[]
m=[]
boards=[]
while(i<=T):
    j=0
    line=a.readline()
    dimstr=line[:len(line)-1]
    fnum=""
    lnum=""
    isAfterSpace=False
    while(j<len(dimstr)):
        if(dimstr[j]!=" "):
            if(isAfterSpace==False):
                fnum+=dimstr[j]
            else:
                lnum+=dimstr[j]
        else:
            isAfterSpace=True
        j+=1
    n+=[int(fnum)]
    m+=[int(lnum)]
    ntag=0
    board=[]
    while(ntag<n[i-1]):
        line=a.readline()
        rowstr=line[:len(line)-1]
        mtag=0
        row=[]
        subnum=""
        while(mtag<len(rowstr)):        
            if(rowstr[mtag]==" "):                
                row+=[int(subnum)]
                subnum=""
            else:
                subnum+=rowstr[mtag]
            mtag+=1
        row+=[int(subnum)]
        board+=[row]
        ntag+=1
    boards+=[board]
    i+=1
i=0
while(i<T):
    prints='YES'
    if(IsPossible(boards[i])==False):
        prints='NO'
    print("Case #"+str(i+1)+": "+prints)
    i+=1
