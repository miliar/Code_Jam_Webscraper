def gcd(a,b):
    if b==0:return a
    return gcd(b,a%b)
cin=open('a.txt','r')
cout=open('b.txt','w')
C=int(cin.next())
for c in range(1,C+1,1):
    line=cin.next()
    x=line.split(' ')
    N=int(x[0])
    g=0
    for i in range(1,N+1,1):
        a=int(x[i])
        for j in range(i+1,N+1,1):
            b=int(x[j])
            if a<b:
                g=gcd(g,b-a)
            if a>b:
                g=gcd(g,a-b)
    m=int(x[1])%g
    if m==0:m=g
    cout.write('Case #'+str(c)+': '+str(g-m)+'\n')
cout.close()
