def fillQues(r,c,a,v):
    for i in range(r):
        for j in range(c):
            if a[i][j]=='?':
                a[i][j]=v

def fillRow(r,c,a,v,n):
    for i in range(c+1,n):
        if a[r][i]=='?':
            a[r][i]=v
        else:
            break
    for i in range(c-1,-1,-1):
        if a[r][i]=='?':
            a[r][i]=v
        else:
            break

        
for t in range(input()):
    r,c=map(int,raw_input().split())
    a=[]
    for i in range(r):
        a.append(list(raw_input()))

    
    for i in range(r):
        for j in range(c):
            if a[i][j]=='?':
                continue
            else:
                fillRow(i,j,a,a[i][j],c)

    
    for i in range(1,r):
        for j in range(c):
            if a[i][j]=='?':
                a[i][j]=a[i-1][j]

    for i in range(r-2,-1,-1):
        for j in range(c-1,-1,-1):
            if a[i][j]=='?':
                a[i][j]=a[i+1][j]
    
        
    print "Case #"+str(t+1)+":"
    for i in range(r):
        s=""
        for j in range(c):
            s+=a[i][j]
        print s
