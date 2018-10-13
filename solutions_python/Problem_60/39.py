import math


f=open('B-large(2).in','r')
g=open('B-large.out','w')
getline=f.readline()
#eleline=getline.split()

tt=int(getline)
print tt


for case in range(tt):
    getline=f.readline()
    eleline=getline.split()
    n=int(eleline[0]);k=int(eleline[1]);b=int(eleline[2]);m=int(eleline[3])

    getline=f.readline()
    eleline=getline.split()
    x=[0 for i in range(n)];
    for i in range(n):
        x[i]=int(eleline[i])*1.

    getline=f.readline()
    eleline=getline.split()    
    v=[0 for i in range(n)];
    for i in range(n):
        v[i]=int(eleline[i])*1.

    li=[]

    for i in range(n):
        if x[i]+v[i]*m>=b:
            num=0
            for j in range(i+1,n):
                if (v[j]<v[i]):
                    if x[j]+v[j]*m<b:
                        num+=1
            li.append(num)

    li.sort()
    if len(li)<k:
        g.write('Case #'+str(case+1)+': '+"IMPOSSIBLE"+'\n')
        print 'Case #'+str(case+1)+': '+"IMPOSSIBLE"+'\n'
    else:
        ans=0
        for i in range(k):
            ans+=li[i]
        g.write('Case #'+str(case+1)+': '+str(ans)+'\n')
        print 'Case #'+str(case+1)+': '+str(ans)+'\n'

f.close()
g.close()

            


