def createList(zz):
    zz=half(zz)
    if zz==[]:
        return
    for i in zz:
        z.append(i)
        createList(i)

def half(a):
        x=a//2
        y=a//2-1+a%2
        if x==0:
            return []
        if y==0:
            if x==0:
                return []
            return [x]
        return [x,y]
tt=int(input())
for t in range(1,tt+1):
    [n,k]=list(map(int,input().split()))
    z=[n]
    createList(n)
    z.sort()
    z=z[::-1]
    ans=z[k-1]//2,z[k-1]//2-1+z[k-1]%2
    print("Case #"+str(t)+":",ans[0],ans[1])

