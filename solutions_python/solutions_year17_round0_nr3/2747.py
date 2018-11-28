# encoding: utf-8
from queue import PriorityQueue

txtin="C-small-1-attempt0.in"
fout="out.txt"

with open(txtin,'r') as f:
    t=int(f.readline())
    with open(fout, 'w') as fout:
        for cas in range(t):
            n,k=map(int,f.readline().split())
            occupied=[0,n+1]
            intvs=PriorityQueue()
            intvs.put((1-n,1,n))
            while k>0:
                dist,start,end=intvs.get()
                k-=1
                mid=(start+end)//2
                ls=start-mid+1
                rs=mid+1-end
                intvs.put((ls,start,mid-1))
                intvs.put((rs,mid+1,end))
                occupied.append(mid)
#             occupied.sort(reverse=True)
            print(occupied)
            fout.write('Case #'+str(cas+1)+': '+str(1-rs)+' '+str(1-ls)+'\n')
            