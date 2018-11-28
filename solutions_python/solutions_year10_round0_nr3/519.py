f=open('C-small-attempt0.in','r')
fo=open('output.txt','w')
t=int(f.readline())
for i in range(t):
    r,k,n=f.readline().split()
    r,k,n=int(r),int(k),int(n)
    a=f.readline().split()
    b=[]
    c=0
    for j in a:
        b.append(int(j))
    for j in range(r):
        a=0
        for m in range(n):
            a+=b[0]
            if a<=k:
                b.append(b[0])
                del b[0]
            else:
                a-=b[0]
                break
        c+=a
    fo.write('Case #{0}: {1}\n'.format(i+1,c))
