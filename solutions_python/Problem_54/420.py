def gcd(a, b):
    if a<b:
        a,b=b,a
    while b != 0:
        (a, b) = (b, a%b)
    return a

f=open('b-large.in','r')
g=open('B-large.out','w')
getline=f.readline()

t=int(getline)
print t

for case in range(t):
    getline=f.readline()
    eleline=getline.split()
    n=int(eleline[0])
    t=[]
    for i in range(n):
        t.append(int(eleline[i+1]))
    t.sort()
    minus=[]
    for i in range(n-1):
        minus.append(t[i+1]-t[i])
    divisor=minus[0]
    for i in range(1,n-1):
        divisor=gcd(divisor,minus[i])
    if t[1]%divisor==0:
        ans=0
    else:
        ans=divisor-(t[1] % divisor)
    g.write('Case #'+str(case+1)+': '+str(ans)+'\n')

f.close()
g.close()

            


