def calc(a,b,x,y):
    dic={}
    ans=[]
    for i in a[x-1]:
        dic[i]=1
    for i in b[y-1]:
        if i in dic:
            ans.append(i)
    return ans


f=open('A-small-attempt0.in','r+')

t=int(f.readline())

for case in xrange(t):
    r1=int(f.readline())
    arr1=[0]*4
    for i in xrange(4):
        arr1[i]=[int(e) for e in f.readline().split()]
    r2=int(f.readline())
    arr2=[0]*4
    for i in xrange(4):
        arr2[i]=[int(e) for e in f.readline().split()]
    ans=calc(arr1,arr2,r1,r2)
    if len(ans)>1:
        print 'Case #%d: Bad magician!'%(case+1)
    elif len(ans)<1:
        print 'Case #%d: Volunteer cheated!'%(case+1)
    else:
        print 'Case #%d: %d'%(case+1,ans[0])
f.close()
