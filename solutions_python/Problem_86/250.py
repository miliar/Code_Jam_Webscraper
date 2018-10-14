import sys
import fractions
gcd=fractions.gcd

with open('in.txt','r+') as i:
    z=i.readlines()

z[0]=int(z[0])
l=z[0]
z=z[1:]
res=[] #res


for y in range(l):#z:# range(l):
    y4=z[0].split()
    y1=int(y4[0])
    y2=int(y4[1])
    y3=int(y4[2])
    i=y1
    ree=z[1].split()
    for _y in range (i):
        ree[_y]=int(ree[_y])
    z=z[2:]

    '''if i==1: 
        for m in range(y2,min(ree[0],y3)+1,1):
            if ree[0]%m==0:
                res.append(str(m))
                break
    else:
        g=gcd(ree[0],ree[1])
        for _y in range(1,i,1):
            g=gcd(g,ree[_y])
        for m in range(y2,min(g,y3)+1,1):
            if g%m==0:
                res.append(str(m))
        g=1    
    '''
    for m in range(y2,y3+1,1):
        u=1
        for m2 in ree:
            if m2%m!=0 and m%m2!=0:
                u=0
            if u==0:
                #print(m2)
                break
        if u==1:
            res.append(str(m))
            break
    if len(res)==y:
        res.append('NO')
                        
        
n=1
with open('out.txt','w+') as o:
    for u in res:
        o.write("Case #"+str(n)+': '+u+'\n')
        n=n-(-1)
    
    
