def solve(x,y,n):
    m=0
    for i in range(n):
        for j in range(i,n):
            for k in range(j,n):
                if(i==j) or (j==k) or (k==i):
                    continue
                X=x[i]+x[j]+x[k]
                Y=y[i]+y[j]+y[k]
                if (X%3==0) and (Y%3==0):
                    
                    m+=1
    return m
                
                
a=file('A-small.in')
b=file('A-small.out','w')
T=int(a.readline())

for i in range(T):
    n,A,B,C,D,x0,y0,m=[int(l) for l in a.readline().split()]
    x=[]
    y=[]
    z=[]
    x.append(x0)
    y.append(y0)
    X=x0
    Y=y0
    for j in range(1,n):
        X = (A * X + B)%m
        Y = (C * Y + D)%m
        x.append(X)
        y.append(Y)
    
    k=solve(x,y,n)
    b.write('Case#'+str(i+1)+':'+' '+str(k)+'\n')
a.close()
b.close()
print 'finish'
    
