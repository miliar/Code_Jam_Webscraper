from math import ceil
n=int(input())
for x in range(n):
    m,n=input().split()
    m='0'*int(m)
    n=int(n)
    while n>1:
        p=m.split('1')
        t=max(p)
        t=list(t)
        t[int(ceil(len(t)/2))-1]='1'
        p[p.index(max(p))]=''.join(t)
        m='1'.join(p)
        n=n-1
    p=m.split('1')
    t=max(p)
    t=list(t)
    y=len(t[:int(ceil(len(t)/2))-1])
    z=len(t[int(ceil(len(t)/2)):])
    print(r'Case #'+str(x+1)+': '+str(max(y,z))+' '+str(min(y,z)))
