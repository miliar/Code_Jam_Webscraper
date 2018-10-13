from math import *

def getNum(n,minN,maxN):
    m=n
    if n<10:
        return 0
    ans=0
    found=[n]
    dig=int(log10(n))
    for p in range(dig):
        d=n%10
        n=d*(10**dig)+(n//10)
        if d==0 or n in found or n>maxN or n<minN:
            continue
        if minN==733 and maxN==764:
            print(m,n)
        ans+=1
        found+=[n]
    return ans

f=open('1c_large.txt')
f2=open('1c_large_output.txt','w')
f.readline()
for m,line in enumerate(f):
    a,b=tuple([int(x) for x in line.split()])
    tot=0
    for n in range(a,b+1):
        pairs=getNum(n,a,b)
        tot+=pairs
    f2.write('Case #'+str(m+1)+': '+str(tot//2)+'\n')
f.close()
f2.close()
