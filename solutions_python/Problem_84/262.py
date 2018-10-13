import sys
import fractions
gcd=fractions.gcd

with open('in.txt','r+') as i:
    z=i.readlines()

z[0]=int(z[0])
l=z[0]
z=z[1:]
res=[] #res


for c in range(l):#z:# range(l):
    t=z[0].split()
    s1,s2=int(t[0]),int(t[1])
    r=[]
    for s in range(s1):
        r.append(list(z[s+1]))
    z=z[s1+1:]
    i=0
    for k in range(s1):
        if r[k].count('#')%2!=0:
            res.append('Impossible')
            i=1
            break
    n=0
    if not i:
        for m in range(s2):
            for m1 in range(s1):
                if r[m1][m]=='#':n+=1
            if n%2==1:
                res.append('Impossible ')
                i=1
                n=0
                break
            n=0
    if not i:
        #print(r)
        re=''
        re=[]
        rz=[' ']*s2
        ed=[0]*s2
        for l1 in range(s1):
            ec=0
            re.append([])
            for l2 in range(s2):
                re[l1].append([])
                if r[l1][l2]=='.':
                    re[l1][l2]='.'
                    #print(l1,l2)
                elif r[l1][l2]=='#':
                    #print(re)
                    if (ed[l2]+ec)%2==0:
                        re[l1][l2]='/'
                    else:
                        re[l1][l2]="\\"
                    ec+=1
                    ed[l2]+=1
                    #print('\n'.join([''.join(s) for s in re]),'\n')
        
        #print(re)
        re='\n'.join([''.join(s) for s in re])
        #print(re)
        res.append(re)
          
                        
        
n=1
with open('out.txt','w+') as o:
    for u in res:
        o.write("Case #"+str(n)+':'+'\n'+u+'\n')
        n=n-(-1)
    
    
