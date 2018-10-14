
class Solution:
    def __init__(self,Pi):
        Pi=tuple(sorted(Pi,reverse=True))
        self.tp=Pi
        self.map={(1,):1,(0,):0}
    def result(self):
        tp=self.tp
        if max(tp)<=1: return max(tp)
        stack=[tp]
        while stack:
            tmppi=stack[-1]
            if tmppi in self.map: stack.pop();continue
            elif max(tmppi)<=1: stack.pop();continue
            p1=tuple(filter(None,[i-1 for i in tmppi]))
            minv=1+max(p1)
            allTry=True
            for k in range(1,tmppi[0]//2+1):                
                p2=[k,tmppi[0]-k]+list(tmppi[1:])
                p2=tuple(sorted(p2,reverse=True))
                if max(p1)==1: p1=(max(p1),)
                if max(p2)==1: p2=(max(p2),)
                if p1 in self.map and p2 in self.map:
                    minv=min(minv,1+min(self.map[p1],self.map[p2]))
                else:
                    allTry=False
                    if p1 not in self.map: stack.append(p1)
                    if p2 not in self.map: stack.append(p2)
            if allTry: self.map[tmppi]=minv;stack.pop()
        return self.map[tp]
        

with open('testin.txt','r') as f:
	data=f.readlines()

N=int(data[0])
res=""

start,delta=1,2
for i in range(N):
    D=int(data[start])
    Pi=map(int,data[start+1].split())
    x=Solution(Pi)
    res+="Case #{}: {}\n".format(i+1,x.result())
    start+=delta

with open('res.txt', 'w') as f:
	f.write(res)