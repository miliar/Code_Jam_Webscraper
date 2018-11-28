import numpy as np

def road(D,N):

    horses = np.empty((N,2))
    for i in range(N):
        K,S = [int(s) for s in input().split(' ')]
        horses[i,0] = K
        horses[i,1] = S
    
    if N == 1:
        return D/((D-K)/S)
    
    horses = horses[horses[:,0].argsort()]

    T=0
    for i in range(N-1):
        th = (D-horses[i,0])/horses[i,1]
        dv = (horses[i+1,1]-horses[i,1])
        if dv == 0:
            T += (th) 
            return D/T

        t = -1*(horses[i+1,0]-horses[i,0])/dv
        
        if  th > t and t > 0 :
            horses[i+1:,0] += t*horses[i+1:,1] 
        else:
            T += (th) 
            return D/T
        T += t
    return D/(T + (D-horses[N-1,0])/horses[N-1,1])

T = int(input())
for t in range(1,T+1):
    D,N = [int(s) for s in input().split(' ')]
    x = road(D,N)
    print ('Case #{}: {:6f}'.format(t,x))