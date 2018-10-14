choose=[[1]]
for i in range(1,1000):
    ch=1
    chosen=[1]
    for j in range(1,i+1):
        ch=ch*(i-j+1)
        ch=ch/j
        chosen.append(ch)
    choose.append(chosen)

def parse():
    f=open('B-small-attempt2.in', 'r')
    g=open('fileout.txt','w')
    cases=int(f.readline())
    for i in range(cases):
        n,x,y=f.readline().split(' ')
        n,x,y=int(n),int(x),int(y)
        ans=prob(n,x,y)
        s='Case #'+str((i+1))+': '+str(ans)+'\n'
        g.write(s)

def prob(n,x,y):
    j=0
    s=0
    while (not s>n):
        s+=1+4*j
        j+=1
    j=j-1
    s=s-1-4*j
    if j*2>=abs(x)+abs(y)+2:
        return 1.0
    if abs(x)+abs(y)-2>=j*2:
        return 0.0
    balls=n-s
    slots=1+4*j
    return probrow(balls,slots,y)


def probrow(n,m,y):
    h=(m-1)/2
    if n-y>m/2:
        return 1.0
    if y>=n:
        return 0.0
    if y>=h:
        return 0.0
    s=0
    a=[0]*(n+1)
    for i in range(y+1,n+1):
        a[i]=1
    for i in range(0,n-h-y):
        a[i]=1
    for j in range(n+1):
        if a[j]==1:
            s=s+choose[n][j]
    return (s*1.0/(2**n))

parse()
