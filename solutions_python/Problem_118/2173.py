from math import sqrt,floor

def isPal(numero):
    st=str(numero)
    return st==st[::-1]

def solucion(a,b):
    bb=floor(sqrt(b))
    l=[i**2 for i in range(bb+1) if i**2>=a]
    ll=[i for i in l if isPal(i)]
    lll=[i for i in ll if isPal(floor(sqrt(i)))]
    return len(lll)

if __name__=='__main__':
    f=open('C-small-attempt0.in')
    g=open('Solucion3.txt','w')
    M=int(f.readline())
    for m in range(1,M+1):
        A,B=map(int,f.readline().strip().split(' '))
        print('Case #%d: %d' %(m,solucion(A,B)),file=g)
    f.close()
    g.close()
    
    
        
    
