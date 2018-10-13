def moins1(nc): #Tout est dans le nom, effectue l'opération n-1
    return(str(int(nc)-1))

def first(nc):
    l=len(nc)
    der=nc[0]
    chg=False
    c=1
    while c<l and chg==False:
        chfr=nc[c]
        if chfr<der:
            chg=True
            deb=moins1(nc[:c])
            if deb=='0':
                nc='9'*(l-c)
            else:
                nc=deb+'9'*(l-c)
        else:
            der=chfr
            c+=1    
    return(nc)
    
def next(nc):
    nc1=nc
    nc2=first(nc)
    while nc1!=nc2:
        nc1,nc2=nc2,first(nc2)
    return(int(nc2))
    
def main():
    ifn='B-large.in'
    ofn='output.txt'
    f=open(ifn,'r',encoding='utf-8')
    g=open(ofn,'w')
    nb_val=int(f.readline().strip())
    for k in range(nb_val):
        nbc=f.readline().strip()
        S=next(nbc)
        g.write("Case #%d: " %(k+1))
        g.write("%d\n" %S)
    f.close()
    g.close()
    return('Fin')