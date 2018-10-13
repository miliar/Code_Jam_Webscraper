from math import ceil
def primes(n):
    F=range(n)
    for i in range(n):
        for j in range(2,ceil(i**0.5)+1):
            if i%j==0 and i in F:
                F.remove(i)
    return [2]+F[2:]

P=primes(3000)

def factors(n):
    F=[]
    for i in P:
        if n%i==0:
            F.append(i)
    return F
    

f=open('B-small-attempt2.in')
k=0
c=0
for l in f:
    k+=1
    if k>1:
        a,b,p=map(int,l.split(' '))
        L=[factors(i) for i in range(a,b+1)]
        test=True
        while test==True:
            test=False
            try:
                for i in range(len(L)):
                    for j in range(i+1,len(L)):
                        for o in L[j]:
                            if o in L[i] and o>=p:
                                for m in L[j]:
                                    L[i].append(m)
                                del L[j]
                                test=True
                                break
            except:
                pass
        c+=1
        print 'Case #'+str(c)+': '+str(len(L))
