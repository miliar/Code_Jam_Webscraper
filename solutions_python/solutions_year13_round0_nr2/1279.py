def get_max(row):
    max=row[0]
    for i in row:
        if i > max:
            max=i            
    return max

def column(matrix, i):
    return [row[i] for row in matrix] 
    
def get_after_cut(max,x):
    diff=100-max
    return x-diff

def get_result(input,n,m):
    matrix=[]
    rowmax=[]
    colmax=[]
    minmatrix=[]
    for i in range(0,n):
            matrix.append([])
            rowmax.append([])
            colmax.append([])
            minmatrix.append([])
            for j in range(0,m):
                matrix[i].append(100)
                rowmax[i].append(100)
                colmax[i].append(100)
                minmatrix[i].append(100)
    for i in range(0,n):
        max=get_max(input[i])
        for j in range(0,m):
            rowmax[i][j]=max            
    for j in range(0,m):
        col=column(input,j)
        max=get_max(col)
        for i in range(0,n):
            colmax[i][j]=max
    
    for i in range(0,n):
        for j in range(0,m):
            minmatrix[i][j]=min(rowmax[i][j],colmax[i][j])
    if input==minmatrix:
        return "YES"
    return "NO"
        
            
t=input()
for i in range(0,t):
    n,m=raw_input().split(' ')
    n=int(n)
    m=int(m)    
    matrix=[]
    for j in range(0,n):        
        matrix.append(map(int,raw_input().split(' ')))
    print "Case #{0}: {1}".format(i+1,get_result(matrix,n,m))    
    
    