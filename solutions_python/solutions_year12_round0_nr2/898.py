fi=open('B-large.in','r')
a=fi.readlines()
fi.close()
t=int(a[0])
f=open('out.txt','w')
for i in range(t):
    tmp=map(lambda x:int(x),a[i+1].split())
    f.write('Case #%d: '%(i+1))
    n=tmp[0]
    s=tmp[1]
    p=tmp[2]
    if p==0:
        f.write(str(n))
        f.write('\n')
        continue
    if p==1:
        cnt=0
        for j in range(n):
            if tmp[3+j]>0:
                cnt+=1
        f.write('%d\n'%cnt)
        continue
    cnt=0
    for j in range(n):
        if tmp[3+j]>=p+p+p-2:
            cnt+=1
        elif tmp[3+j]>=3*p-4:
            if s>0:
                s-=1
                cnt+=1
    f.write('%d\n'%cnt)
f.close()
