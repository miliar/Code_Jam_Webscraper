def solve(alphafreq,P,K):
    sum1=0
    for j in range(P):
        for l in range(K):
            if(len(alphafreq)!=0):
                key=alphafreq.pop(0)
                sum1+=key*(j+1)
            else:
                return sum1
    return sum1
    
a=file('A-smallin.in')
b=file('A-small.out','w')
T=int(a.readline())
for i in range(T):
    P,K,L=[int(l) for l in a.readline().split()]
    alphafreq=[int(l) for l in a.readline().split()]
    alphafreq.sort(reverse=1)
    sum1=solve(alphafreq,P,K)
    b.write('Case #'+str(i+1)+': '+str(sum1)+'\n')

a.close()
b.close()
print 'finish'

