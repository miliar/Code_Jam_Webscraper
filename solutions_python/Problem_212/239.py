import numpy as np

with open('A-small-attempt0.in','r') as f, open('out.txt','w') as fout:
    print('Input file:',f.name)
    t=int(f.readline().strip())
    for case in range(1,t+1):
        n,p=[int(s) for s in f.readline().strip().split()]
        g=np.array([int(s) for s in f.readline().strip().split()])
        gi=[np.sum(g%p==i) for i in range(p)]
        if p==2:
            ans=gi[0]+(gi[1]-1)//2+1
        elif p==3:
            ans=gi[0]+min(gi[1],gi[2])+(abs(gi[1]-gi[2])-1)//3+1
        else:
            ans=gi[0]+min(gi[1],gi[3])+(gi[2]-1)//2+1
        print('Case #%d: %d'%(case, ans),file=fout)
