#Filename:B.py


fin=file('B-small-attempt0.in')
fout=file('output.txt','w')
'''
def findminindex(mat,n,m):
    min=100
    mindex=[0,0]
    for i in range(0,n):
        for j in range(0,m):
            if mat[i][j]<min:
                min=mat[i][j]
                mindex[0]=i
                mindex[1]=j

    return mindex
'''
def checkrow(mat,i,j,m):
    Allequ=True
    cur=mat[i][j]
    for k in range(0,m):
        if mat[i][k] > cur:
            Allequ=False
            break
    return Allequ
def checkcol(mat,i,j,n):
    Allequ=True
    cur=mat[i][j]
    for k in range(0,n):
        if mat[k][j] > cur:
            Allequ=False
            break
    return Allequ
'''
def alljud(flagmat,n,m):
    for i in range(0,n):
        for j in range(0,m):
            if flagmat[i][j] == False:
                return False

    return True
'''



numcase=fin.readline()


for case in range(1,int(numcase)+1):
    matrix=[]
    flagmat=[]
    line=fin.readline()
    n,m=line.split()
    for i in range(0,int(n)):
        row=fin.readline()
        row=row.split()
        matrix.append(row)
    #matrix input end
    #create flagmat
    #flagmat = [[False for col in range(int(m))] for row in range(int(n))]
    n=int(n)
    m=int(m)
    flag=False
    for xin in range(0,n):
        for yin in range(0,m):
            if (not checkrow(matrix,xin,yin,m)) and (not checkcol(matrix,xin,yin,n)):
                # flagmat[xin][yin]=True
                fout.write('Case #%d: NO\n' %(case))
                flag=True
                #print xin,yin
                break
        if flag==True:
            break
    if flag== False:    
        fout.write('Case #%d: YES\n' %(case))














fin.close()
fout.close()
