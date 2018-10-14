"""
Alien numbers
"""

class Solution:
    def __init__(self,gps):
        self.GPS=gps
    def result(self):
        ret=0
        gps=self.GPS
        ss,tt=[],[]
        for s,n,t in gps:
            if n==1:
                ss.append(s);tt.append(t)
            else:
                for k in range(n):
                    ss.append(s);tt.append(t+k)
        
        if len(ss)==1: return 0
        if len(ss)==2 and tt[0]==tt[1]: return 0
        elif len(ss)==2:
            if ss[1]<ss[0]: ss.reverse();tt.reverse()
            if tt[0]>=tt[1]:
                if (360.0-(ss[1]-ss[0]))/(360-ss[0])<=1.0*tt[0]/tt[1]-1: return 1
                else: return 0
            else:
                if (360.0+(ss[1]-ss[0]))/(360-ss[1])<=1.0*tt[1]/tt[0]-1: return 1
                else: return 0
        return 0
        

with open('testin.txt','r') as f:
	data=f.readlines()

N=int(data[0])
res=""

start,delta=1,0
for i in range(N):
    ng=int(data[start])
    gps=map(lambda xx: map(int,xx.split()),data[start+1:start+ng+1])
    x=Solution(gps)
    res+="Case #{}: {}\n".format(i+1,x.result())
    start+=ng+1

with open('res.txt', 'w') as f:
	f.write(res)