
import math

def tokill(ad,hk,b):
    minres=100
    for k1 in range(100):
        for k2 in range(20):
            if (ad+b*k2)*k1 >=hk:
                if k1+k2 < minres:
                    minres =k1+k2
    return minres

def calc(hd,ak,d,i):
    li=hd
    dmg=ak
    res=0
    j=0
    while j<i:
        res+=1
        if li > dmg-d:
            j+=1
            dmg=dmg-d
        else:
            li= hd
        li =li -dmg
    return li,res
            
            
            
        
        
        

def solve(hd,ad,hk,ak,b,d):
    if ad >= hk:
        return "1"+"\n"
    if ak-d >= hd:
        return "IMPOSSIBLE"+"\n"
    if ak < hd and 2*ad >=hk:
        return "2"+"\n"
    if ak < hd and b+ad >=hk:
        return "2"+"\n"
    if 2*ak-3*d >= hd:
        return "IMPOSSIBLE"+"\n"
    res=tokill(ad,hk,b)
    if d==0:
        k1=math.floor((hd-1)/ak)
        if k1>=res:
            return str(res)+"\n"
        return str(math.ceil((res-k1-1)/(k1-1))+res)+"\n"
    minres=300
    for i in range(100):
        
        tmpres=300
        li,k=calc(hd,ak,d,i)
        if ak-i*d <=0:
            tmpres=res+k
        else:
            if math.floor((li-1)/(ak-i*d))>=res:
                tmpres=res+k
            else:
                if math.floor((hd-1)/(ak-i*d))-1 <=0:
                    tmpres=300
                else:
                    tmpres=math.ceil((res-math.floor((li-1)/(ak-i*d))-1)/(math.floor((hd-1)/(ak-i*d))-1))+res+k
        if minres > tmpres:
            minres=tmpres
    return str(minres)+"\n"

g = open('output.txt', 'w')

f = open('C-small-attempt0.in', 'r')

t= int(f.readline())
for i in range(t):
    s=f.readline().split()
    hd=int(s[0])
    ad=int(s[1])
    hk=int(s[2])
    ak=int(s[3])
    b=int(s[4])
    d=int(s[5])
    out=solve(hd,ad,hk,ak,b,d)
    g.write("Case #" +str(i+1) +": "+out)
g.close()
        

