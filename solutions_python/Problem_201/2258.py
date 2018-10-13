import math
def stall(N,K):
    if N==1:
        y,z=0,0
    elif N==2:
        y,z=K%2,0
    else:
        if K==1:
            y,z=int(math.ceil(float(N-1)/2)),int(math.floor(float(N-1)/2))
        else:
            if K%2==0:
                y,z=stall(math.ceil(float(N-1)/2),K/2)
            else:
                y,z=stall(math.floor(float(N-1)/2),K/2)
    return [y,z]
f=open('C-small-2-attempt0.in','r')
o=open('out.txt','w')
T=int(f.readline())
for t in range(T):
    N,K=[int(i) for i in f.readline().split()]
    y,z=stall(N,K)
    o.write('Case #'+str(t+1)+': '+str(y)+' '+str(z)+'\n')
o.close()
f.close()