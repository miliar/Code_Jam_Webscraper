T=input()
f=open("Mushroom Monster","w")
for i in range(T):
    N=input()
    a=[int(x) for x in raw_input().split()]
    x,y=0,0
    for j in range(1,N):
        if a[j]<a[j-1]:
            x+=a[j-1]-a[j]
    c=0
    for k in range(1,N):
        if c<a[k-1]-a[k]:
            c=a[k-1]-a[k]
    for k in range(N-1):
        if a[k]>c:
            y+=c
        else:
            y+=a[k]
    f.write("Case #%d: %d %d\n"%(i+1,x,y))
