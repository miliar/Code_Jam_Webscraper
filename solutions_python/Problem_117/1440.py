n=int(input())
for L in range(n):
    n,m=map(int,input().split())
    A=[]
    for i in range(n):
        A.append(list(map(int,input().split())))
        k=0
        for j in range(m):
            if A[i][j]==1: k+=1
            else: break
        if k==m:
            for j in range(m):
                A[i][j]=0
    for j in range(m):
        k=0
        for i in range(n):
            if A[i][j]<2: k+=1
            else: break
        if k==n:
            for i in range(n):
                A[i][j]=0
    k=0            
    for i in range(n): 
        for j in range(m):
            if A[i][j]==1: 
                k=1
                break
        if k==1: break 
    if k==0: 
        print('Case #'+str(L+1)+':','YES')
    else:    
        print('Case #'+str(L+1)+':','NO')