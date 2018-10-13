f=file("file.in",'r')
f2=file("a.out","w")
aa=(int)(f.readline())
for k in range(aa):
    tmp=f.readline().split()
    a=int(tmp[0])
    b=int(tmp[1])
    cnt=0
    for i in range(int(pow(a,0.5))-1,int(pow(b,0.5))+1):
        s=str(i*i)
        flag=True
        for j in range(len(s)/2):
            if s[j]!=s[len(s)-1-j]:
                flag=False
        s=str(i)
        for j in range(len(s)/2):
            if s[j]!=s[len(s)-1-j]:
                flag=False
        if flag and i*i in range(a,b+1):
            cnt+=1
    f2.write('Case #'+str(k+1)+': '+str(cnt)+'\n')
f.close()
f2.close()
