
class Solution:
    def __init__(self,s,_l,_x):
        self.S,self.L,self.X=s,_l,_x
        self.map={'ii':(-1,''),'ij':(1,'k'),'ik':(-1,'j'),
                  'ji':(-1,'k'),'jj':(-1,''),'jk':(1,'i'),
                  'kk':(-1,''),'ij':(1,'k'),'ik':(-1,'j'),
                  'ki':(1,'j'),'kj':(-1,'i'),'kk':(-1,''),
                    'i':(1,'i'),'j':(1,'j'),'k':(1,'k'),'':(1,'')}
        self.multip=lambda s1,s2: (s1[0]*s2[0]*self.map[s1[1]+s2[1]][0],self.map[s1[1]+s2[1]][1])
    def pows(self,s,X):
        x=X%4;inis=(1,'')
        for ii in range(x): inis=self.multip(inis,s)
        return inis
    def result(self):
        s,L,X=self.S,self.L,self.X
        accProd=[]
        inis=(1,'')
        for c in s:
            accProd.append(self.multip(inis,(1,c)));
            inis=accProd[-1]
        res='NO';
        # check i*j*k==-1
        if self.pows(accProd[-1],X)!=(-1,''): return res
        # check i*j==k
        prepows=range(X-1,max(-1,X-5),-1)
        jFlag=False
        for j in prepows:
            pre=self.pows(accProd[-1],j)
            idx=L
            for c in accProd[::-1]:
                idx-=1
                if self.multip(pre,c)==(1,'k'):
                    jFlag=True;break
            if jFlag: break
        if jFlag==False: return res
        # check i
        prepows=range(min(4,X))
        iFlag=False
        for ii in prepows:
            pre=self.pows(accProd[-1],ii)
            idxi=-1
            for c in accProd:
                idxi+=1
                if self.multip(pre,c)==(1,'i'):
                    iFlag=True;break
            if iFlag: break
        if iFlag==False: return res
        if (ii,idxi)>=(j,idx): return res
        return 'YES'
        
        
        
        
        
                
        
        
        
        
        
        
        
        
        

with open('testin.txt','r') as f:
	data=f.readlines()

N=int(data[0])
res=""

start,delta=1,2
for i in range(N):
    sL,sX=map(int,data[start].split())
    mystr=data[start+1].strip()
    x=Solution(mystr,sL,sX)
    res+="Case #{}: {}\n".format(i+1,x.result())
    start+=delta
    print 'finished case %d'%i

with open('res.txt', 'w') as f:
	f.write(res)