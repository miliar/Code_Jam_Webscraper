f=open('A-large.in','r')
fo=open('output1.txt','w')
t=int(f.readline())
for j in range(t):
    n,m=f.readline().split()
    n,m=int(n),int(m)
    c=[]
    ans=0
    for i in range(n):
        a=f.readline().strip('\n')
        b=a.split('/')
        del b[0]
        a=''
        for k in b:
            a+='/'+k
            if a not in c:
                c.append(a)
    for i in range(m):
        a=f.readline().strip('\n')
        b=a.split('/')
        del b[0]
        a=''
        for k in b:
            a+='/'+k
            if a not in c:
                ans+=1
                c.append(a)
    fo.write('Case #{0}: {1}\n'.format((j+1),ans))
