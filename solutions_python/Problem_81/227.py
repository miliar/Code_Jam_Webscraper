import sys
import fractions
gcd=fractions.gcd

with open('in.txt','r+') as i:
    z=i.readlines()

z[0]=int(z[0])
l=z[0]
z=z[1:]
res=[] #res


for c in range(l):
    ret=[]
    z2=int(z[0])
    sh=[]
    for u in range(z2):
        ret.append([[],[],[],[],[],[],[],[],[],[]])
        sh.append(list(z[u+1].strip()))
    z=z[z2+1:]
    res.append('Case #'+str(c+1)+': ')
    for u in range(z2):
        z3=0;z4=0
        for s in range(z2):
            if sh[u][s]=='1' or sh[u][s]=='0':z4+=1
            if sh[u][s]=='1':z3+=1
        ret[u][7]=z4
        ret[u][8]=z3
        if z4==0:ret[u][0]=0
        else:ret[u][0]=z3/z4
    z3=0
    z4=0
    for u in range(z2):
        z3=0
        for s in range(z2):
            if sh[u][s]=='1' or sh[u][s]=='0':
                z5=ret[s][0]
                if ret[u+s-u][8]==0:z6=0
                else:z6=z5*ret[s][7]*(ret[s][8]-int(sh[s][u]))/((ret[s][7]-1)*ret[u+s-u][8])
                z3+=z6
        if ret[u][7]==0:ret[u][1]=0 
        else:ret[u][1]=z3/ret[u][7]

    for u in range(z2):
        z3=0
        for s in range(z2):
            if sh[u][s]!='.':
                z3+=ret[s][1]
        if ret[u][7]==0:ret[u][2]=0        
        else:ret[u][2]=z3/ret[u][7]
        z4=0.25*ret[u][0]+0.50*ret[u][1]+0.25*ret[u][2]
        res.append(z4)
    
    
n=1
with open('out.txt','w+') as o:
    for u in res:
        o.write(str(u)+'\n')
        n=n-(-1)
    
    
