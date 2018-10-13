import math
from match import Match
fin=open("fash.in","r")
fout=open("fash.out","w")
T=int(fin.readline())
for dummy in range(T):
    print dummy
    if dummy>0:
        fout.write('\n')
    fout.write("Case #"+str(dummy+1)+": ")
    N,M=[int(x) for x in fin.readline().split()]
    R=set([i+1 for i in range(N)])#set of rows
    C=set([i+1 for i in range(N)])#set of columns
    SD=set([i for i in range(2,2*N+1)]) # set of sum diagonals
    CD=set([i for i in range(1-N,N)]) # set of difference diagonals
    Grid=[['.' for i in range(N)] for j in range(N)]# Gride[i][j] is row i+1, col j+1
    RD={}#row dictionary
    DD={}#diagonal dictionary
    points=0
    for dummy2 in range(M):
        [c,x,y]=fin.readline().split()
        x=int(x)
        y=int(y)
        Grid[x-1][y-1]=c
        if c!='+':
            R.remove(x)
            C.remove(y)
            points+=1
        if c!='x':
            SD.remove(x+y)
            CD.remove(x-y)
            points+=1
    for r in R:
        RD[r]=set([])
    for d in SD:
        DD[d]=set([])
    for i in range(1,N+1): #Initializing the dictionaries
        for j in range(1,N+1):
            if i in R and j in C:
                RD[i].add(j)
            if i+j in SD and i-j in CD:
                DD[i+j].add(i-j)
    for i in R:
        RD[i]=list(RD[i])
    for i in SD:
        DD[i]=list(DD[i])
    Rows=Match(RD)[0]# note that this goes from columns to rows
    Diag=Match(DD)[0]#note that this goes from difference diagonals to sum diagonals
    points+=len(Rows)+len(Diag)
    K={}
    #number of new lines
    new=0
    for c in Rows:
        K[(Rows[c],c)]='x'
    for diff in Diag:
        sum=Diag[diff]
        i=(sum+diff)/2
        j=(sum-diff)/2
        if (i,j) in K:
            K[(i,j)]='o'
        else:
            K[(i,j)]='+'
    fout.write(str(points)+' '+str(len(K)))
    for (x,y) in K:
        if K[(x,y)]=='o' or Grid[x-1][y-1]!='.':
            fout.write('\no '+str(x)+' '+str(y))
        else:
            fout.write('\n'+K[(x,y)]+' '+str(x)+' '+str(y))
fin.close()
fout.close()

                    
