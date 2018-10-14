def comb(items, n):
    if n==0: yield []
    else:
        for i in xrange(len(items)):
            for cc in comb(items[i+1:],n-1):
                yield [items[i]]+cc

f=open('in.txt')
k=0
m=0
for l in f:
    k += 1
    if k>1:
        c=0
        L=[]
        n,A,B,C,D,x0,y0,M=map(int,l.split(' '))
        X,Y=x0,y0
        L+=[(X,Y)]
        for i in range(1,n):
            X=(A*X+B)%M
            Y=(C*Y+D)%M
            L+=[(X,Y)]
        for i in comb(L,3):
            center=((i[0][0]+i[1][0]+i[2][0]),(i[0][1]+i[1][1]+i[2][1]))
            if center[0]%3==0 and center[1]%3==0:
                c+=1
        m+=1
        print 'Case #'+str(m)+': '+str(c)
