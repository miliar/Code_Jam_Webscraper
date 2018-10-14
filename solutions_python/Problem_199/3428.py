# encoding: utf-8
from sympy.physics.units import current

txtin="A-large.in"
fout="out.txt"

f = open(txtin,'r')
# lst = list(map(int,f.readline()))
t=int(f.readline())

res=[]

with open(fout, 'w') as fout:
    for k in range(t):
        line,s=f.readline().split()
        s=int(s)
        pancakes=[];
        for i,c in enumerate(line):
            if c=='-':
                pancakes.append(1)
            else:
                pancakes.append(0)
        currentSign=0
        signchangedAt=[]
        ans=0
        for i in range(len(pancakes)):# due to automatical )
            if signchangedAt and signchangedAt[0]+s==i :
                signchanged=True
                signchangedAt.pop(0)
            else:
                signchanged=False
            currentSign=1-currentSign if signchanged else currentSign# due to automatical )
            if (currentSign+pancakes[i])%2==0:
                continue
            else:
                currentSign=1-currentSign
                signchangedAt.append(i)
                ans+=1
        ans='IMPOSSIBLE' if signchangedAt and signchangedAt[-1]+s!=len(pancakes) else ans
        fout.write('Case #'+str(k+1)+': '+str(ans)+'\n')