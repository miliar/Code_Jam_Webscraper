def chg(c,x,i):
    for k in range(x,x+i):
        if c[k]=='+':
            c=c[:k]+'-'+c[k+1:]
        else:
            c=c[:k]+'+'+c[k+1:]
    return(c)
    
def verif(c,k):
    bien=True
    l=len(c)
    pos=l-k
    while pos<l and bien:
        bien=c[pos]=='+'
        pos+=1
    return(bien)
    
def prog(c,k):
    nb=0
    l=len(c)
    for i in range(l-k+1):
        if c[i]=='-':
            c=chg(c,i,k)
            nb+=1
    if verif(c,k):
        return(nb)
    else:
        return('IMPOSSIBLE')
        
def lecture(txt):
    pos=0
    pos2=0
    S=[]
    for k in range(1):
        car='0'
        while car!=' ':
            pos2+=1
            car=txt[pos2]
        S+=[txt[pos:pos2]]
        pos=pos2+1
    S+=[txt[pos2+1:]]
    return(S)
        
def main():
    ifn='A-large.in'
    ofn='output2.txt'
    f=open(ifn,'r',encoding='utf-8')
    g=open(ofn,'w')
    nb_val=int(f.readline().strip())
    for k in range(nb_val):
        nbc=f.readline().strip()
        lec=lecture(nbc)
        S=prog(lec[0],int(lec[1]))
        if S=='IMPOSSIBLE':
            g.write("Case #%d: " %(k+1))
            g.write("IMPOSSIBLE\n" )
        else:
            g.write("Case #%d: " %(k+1))
            g.write("%d\n" %S)
    f.close()
    g.close()
    return('Fin')