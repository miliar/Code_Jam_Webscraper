from math import floor,ceil
import queue as q
class container:
    l=None
    r=None
    lend=None
    rend=None
    pos=None
    res1=None
    res2=None
    def __init__(self,lend,rend):
        self.lend=lend
        self.rend=rend
        dist=rend-lend
        self.pos=int(dist/2)+lend
        self.l=int(floor((dist)/2.0))
        self.r=int(ceil((dist)/2.0))
        self.res1=max(self.l,self.r)
        self.res2=min(self.l,self.r)
    def __lt__(self,other):
        if min(self.l,self.r)>min(other.l,other.r):
            return True
        if min(self.l,self.r)<min(other.l,other.r):
            return False
        if max(self.l,self.r)>max(other.l,other.r):
            return True 
        if max(self.l,self.r)<max(other.l,other.r):
            return False
        if self.pos<other.pos:
            return True
        return False
    def print(self):
        print(self.res1,self.res2)
    def print2(self):
        print(self.pos,self.l,self.r,self.lend,self.rend)


f_name='tst_input'
f_name='C-small-1-attempt1.in'
rows=open(f_name,'r').readlines()
nn=int(rows[0])
for tt in range(1,nn+1):
    n,k=map(int,rows[tt].split())
    pq=q.PriorityQueue()
    st=container(0,n-1)
    pq.put(st)
    res=None
    for it in range(k):
        top=pq.get()
        nxt1=container(top.lend,top.pos-1)
        nxt2=container(top.pos+1,top.rend)
        pq.put(nxt1)
        pq.put(nxt2)
        #top.print2()
        res=top


    #top.print()
    print('Case #%d: %d %d'%(tt,top.res1,top.res2))
    #print()
