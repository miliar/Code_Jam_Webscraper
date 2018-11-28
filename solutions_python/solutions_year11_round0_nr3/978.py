def add(a):
    su=0
    for i in a:
        su^=i
    return su

def rotate(a):
    b=a[1:]
    b.append(a[0])
    return b

def part(a):
    x=[]
    for i in range(1,len(a)//2 +1):
        for j in range(len(a)):
            e=a[i:]
            f=a[:i]
            x.append([e,f])
            a=rotate(a)
    return x

fi=open('C-small-attempt0.in','r')
fo=open('candy','w')

cnt=0
no=0
fi.readline()
for i in fi.readlines():
    if cnt%2==1:
        no+=1
        ans=-1
        print i
        a=i.split()
        b=[int(i) for i in a]
        a=b
        a=part(a)
        for j in a:
            if add(j[0])==add(j[1]):
                ans=max(ans,sum(j[0]),sum(j[1]))
        if ans==-1:
            fo.write('Case #%d: %s\n'%(no,'NO'))
        else:
            fo.write('Case #%d: %d\n'%(no,ans))
    cnt+=1

fi.close()
fo.close()
