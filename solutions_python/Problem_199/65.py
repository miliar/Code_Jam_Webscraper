import math
fin=open("opan.in","r")
fout=open("opan.out","w")
T=int(fin.readline())
for dummy in range(T):
    fout.write("Case #"+str(dummy+1)+": ")    
    S=fin.readline().split()
    ##print S
    K=int(S[1])
    S=S[0]
    B=[]
    s='+'
    for c in S:
        if s==c:
            B+=[0]
        else:
            B+=[1]
        s=c
    if s=='+':
        B+=[0]
    else:
        B+=[1]
    pos='y'
    count=0
    for i in range(len(B)-K):
        if B[i]==1:
            B[i]=0
            B[i+K]+=1
            B[i+K]%=2
            count+=1
    for b in B:
        if b==1:
            pos='n'
    if pos=='n':
        fout.write('IMPOSSIBLE\n')
    else:
        fout.write(str(count)+'\n')

fout.close()
fin.close()
