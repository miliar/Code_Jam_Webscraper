f=open('A-large (1).in','r')
fo=open('output3.txt','w')

t=int(f.readline())
for i in range(t):
    n=int(f.readline())
    a=[]
    b=[]
    ans=0
    for j in range(n):
        d,e=f.readline().split()
        d,e=int(d),int(e)
        a.append(d)
        b.append(e)
    for j in range(n):
        for k in range(j+1,n):
            if a[j]<a[k]:
                if b[j]>b[k]:
                    ans+=1
            elif a[j]>a[k]:
                if b[j]<b[k]:
                    ans+=1
    fo.write('Case #{0}: {1}\n'.format(i+1,ans))
