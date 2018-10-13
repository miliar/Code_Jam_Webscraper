'''
Created on Apr 11, 2015

@author: sshadmin
'''
d={"11":"1","1i":"i","1j":"j","1k":"k","i1":"i","ii":"-1","ij":"k","ik":"-j","j1":"j","ji":"-k","jj":"-1","jk":"i","k1":"k","ki":"j","kj":"-i","kk":"-1"}

def mul(sign,a,b):
    r=d[a+b]
    if len(r)==1:
        return (0+sign%2),r
    else:
        return (1+sign)%2,r[1]
def solve2():
    sm,sign="1",0
    p=0
    for i in range(len(s)):
        sign,sm=mul(sign,sm,s[i])
        if p==2:
            continue
        if sign==0 and ijk[p]==sm:
            p+=1
    if sm=="1" and sign==1 and p==2:
        return "YES"
    else:
        return "NO"
        
def solve(si,ii):
    if (si,ii) in dm:
        return dm[(si,ii)] 
    if si==len(s) and ii==len(ijk):
        dm[(si,ii)] ="YES"
        return "YES"
    elif si==len(s) or ii==len(ijk):
        dm[(si,ii)] ="NO"
        return "NO"
    sm,sign="1",0
    for i in range(si,len(s)):
        sign,sm=mul(sign,sm,s[i])
        if sm==ijk[ii] and sign==0:
            x=solve(i+1,ii+1)
            if x=="YES" :
                dm[(si,ii)] ="YES"
                return "YES"
    dm[(si,ii)] ="NO"
    return "NO"
        
    
    

fin=open('../in','r') ; fout=open('../out','w')
cases=int(fin.readline().strip())
for case in range(1,cases+1):
    ijk="ik1"
    dm=dict()
    print case
    line=[x for x in fin.readline().strip().split(' ')]
    l=int(line[0]) ; x=int(line[1])
    s=(fin.readline().strip())*x
    fout.write("Case #"+str(case)+": "+str(solve2())+"\n")