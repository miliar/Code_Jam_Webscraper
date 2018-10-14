
f1=file('in.in')
f2=file('outputwar.txt','w')

t=int(f1.readline())
a=[]
b=[]
for k in range(t):
    n=int(f1.readline())
    row1=f1.readline()
    row2=f1.readline()
    a=row1.split();
    b=row2.split();
    a.sort()
    b.sort()
    
    c1=0
    j=n-1
    i=n-1
    while (i>=0 and j>=0):
        if(a[i]>b[j]):
            c1=c1+1
            i=i-1
            j=j-1
        else:
            j=j-1

    c2=0
    j=n-1
    i=n-1
    while (i>=0 and j>=0):
        if(b[j]>a[i]):
            c2=c2+1
            i=i-1
            j=j-1
        else:
            i=i-1

    ans1=c1
    ans2=n-c2
    if(k!=t-1):
        f2.write('Case #'+repr(k+1)+': '+repr(ans1)+' '+repr(ans2)+'\n')
    if(k==t-1):
        f2.write('Case #'+repr(k+1)+': '+repr(ans1)+' '+repr(ans2))
f1.close()
f2.close()
            
    
    
