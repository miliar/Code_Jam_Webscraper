f=open("B-large.in","r")
f2=open("ans.out","w")
x=int(f.readline())
for a in range(x):
    s=f.readline().split()
    n,m=int(s[0]),int(s[1])
    grass=[[0]*m for i in range(n)]
    for b in range(n):
        s=f.readline().split()
        for c in range(m):
            grass[b][c]=int(s[c])
    ans=True
    row=[]
    col=[]
    for i in range(n):
        row.append(max(grass[i]))
    for i in range(m):
        tem=[]
        for j in range(n):
            tem.append(grass[j][i])
        col.append(max(tem))
    for i in range(n):
        for j in range(m):
            if row[i]>grass[i][j] and col[j]>grass[i][j]:
                ans=False
                break
        if ans==False: break
    t=a+1
    if ans==True:
        f2.write("Case #%d: YES\n"%t)
    else:
        f2.write("Case #%d: NO\n"%t)
f.close()
f2.close()
        