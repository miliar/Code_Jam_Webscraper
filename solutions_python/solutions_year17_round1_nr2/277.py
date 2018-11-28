fi=open('ex2.in')
fo=open('ex2.out','w')
nCases=int(fi.readline())
import math

for case in range(1,nCases+1):
    N,P=[int(tok) for tok in fi.readline().strip().split()]
    packs=[]
    recipe=[int(tok) for tok in fi.readline().strip().split()]
    for i in range(N):
        npack=[int(tok) for tok in fi.readline().strip().split()]
        assert len(npack)==P
        packs.append(sorted(npack))

    assert N<3

    res=0
    if N==1:
        for p in packs[0]:
            for i in range(int(p/(recipe[0]*1.2))-1,int(p/(recipe[0]*0.8))+2):
                if i*recipe[0]*0.9<=p<=i*recipe[0]*1.1:
                    res+=1
                    break
    elif N==2:
        for id0 in range(P):
            brek=False
            for id1 in range(len(packs[1])):
                for i in range(int(packs[0][id0]/(recipe[0]*1.2))-1,int(packs[0][id0]/(recipe[0]*0.8))+2):
                    if i*recipe[0]*0.9<=packs[0][id0]<=i*recipe[0]*1.1 and i*recipe[1]*0.9<=packs[1][id1]<=i*recipe[1]*1.1:
                        res+=1
                        del packs[1][id1]
                        brek=True
                        break
                if brek:break

    fo.write('Case #%s: %s\n' % (case,res))

fi.close()
fo.close()
