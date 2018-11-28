def gcd(a, b):
    if a<b:
        a,b=b,a
    while b != 0:
        (a, b) = (b, a%b)
    return a

f=open('c.small.in','r')
g=open('c-small.out','w')
getline=f.readline()

t=int(getline)
print t

for case in range(t):
    getline=f.readline()
    eleline=getline.split()
    r=int(eleline[0])
    k=int(eleline[1])
    n=int(eleline[2])

    getline=f.readline()
    eleline=getline.split()
    a=[];sum=0
    for i in range(n):
        a.append(int(eleline[i]))
        sum+=a[i]       

    if sum<k:
        g.write('Case #'+str(case+1)+': '+str(r*sum)+'\n')
        continue

    index=[0]*n;num=[0]*n;
    a=a*2;left=0;right=0;s=a[0];
    while left<n:
        while s<=k:
            right+=1
            s=s+a[right]
        index[left]=right;num[left]=s-a[right]
        s-=a[left]
        left+=1
    now=0;ans=0
    for i in range(r):
        ans+=num[now];
        now=index[now]%n
    g.write('Case #'+str(case+1)+': '+str(ans)+'\n')

f.close()

g.close()

            


