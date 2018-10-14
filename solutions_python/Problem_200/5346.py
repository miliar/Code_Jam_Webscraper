t=int(input())
g=[]
y=0
for x in range(0,t):
    n=int(input())
    h=[]
    j=n
    c=0
    for l in range(0,j):
        n=j-l
        for o in range(0,len(str(n))):
            h.append(n%10)
            n=n//10
        if len(h)==1:
            g.append(j)
            break
        for y in range(0,len(h)-1):
            if h[y]>=h[y+1]:
                c=c+1
        if c==len(h)-1:
            g.append(j-l)
            break
        c=0
        h=[]
for f in range(0,t):
    print("Case #%d:"%(f+1),g[f])

