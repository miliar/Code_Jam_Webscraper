import numpy as np



def cumsum(X):
    return np.cumsum(X)

def inv_cumsum(X):
    return np.cumsum(X[::-1])[::-1]
    
    
N = 4
K = 2

def toilette(INPUT):
    C,N,K = map(int,INPUT)
    if K >= N:
        return C,0,0
    if K < 1:
        return C,-1,-1

    RANGE = np.arange(N+2)
    iRANGE = np.arange(N+2)[::-1]
    ONE = np.ones(N+2)
    Z = np.zeros((2,N+2))
    Zl = np.zeros(N+2)
    Zr = np.zeros(N+2)


    Zl[0] = -1
    Zl[N+1] = -N-1

    Zr[0] = -N-1
    Zr[N+1] = -1

    for loop in xrange(K):
        ## build Z
        Z[0] = cumsum(Zl+ONE)-1
        Z[1] = inv_cumsum(Zr+ONE)-1

        Mn = np.min(Z,0)
        Mx = np.max(Z,0)

        z = Mn.argmax()
        nz = (Mn == Mn[z])
        #print Mn[nz], Mx[nz]
        if nz.sum() != 1:
            z = ((Mx == Mx[nz].max()) * nz).argmax()
            
        Zl[z] = -1
        Zl[(Zl<0)] = -np.diff(np.concatenate([[-1],RANGE[(Zl<0)]]))

        Zr[z] = -1
        Zr[Zr<0] = np.diff(np.concatenate([iRANGE[(Zr<0)],[-1]]))
        
    Z[0] = cumsum(Zl+ONE)-1
    Z[1] = inv_cumsum(Zr+ONE)-1
    #print (Z[:,1:-1]<0)+0
    print K,Mx[z],Mn[z]
    return C,Mx[z],Mn[z]

def toilette_anal(INPUT):
    C,N,K = map(int,INPUT)
    if K >= N:
        return C,0,0
    if K < 1:
        return C,-1,-1
    KK = int(np.log2(K))
    return C, (N-(K-2**KK))/2**(KK+1) , (N-K)/2**(KK+1)
    
TEST = np.hstack([ np.arange(100)[:,None]+1 , np.loadtxt('Toilette.in2') ])
RES = map( toilette_anal , TEST )

W = open('Toilette.res22','w')
for r in RES:
    
    W.write( 'Case #'+str(int(r[0]))+': '+str(int(r[1]))+' '+str(int(r[2]))+'\n')

W.close()

