"""
Alien numbers
"""

class Solution:
    def __init__(self,s):
        self.s=s
    def result(self):
        ret=0
        N=len(self.s)
        allsum=0
        self.s=map(int,self.s)
        for i in range(N):
            if allsum<i: ret+=i-allsum;allsum+=i-allsum;
            allsum+=self.s[i]
        return ret

with open('testin.txt','r') as f:
	data=f.readlines()

N=int(data[0])
res=""

start,delta=1,1
for i in range(N):
    smax,strs=data[start].split()
    x=Solution(strs)
    res+="Case #{}: {}\n".format(i+1,x.result())
    start+=delta

with open('res.txt', 'w') as f:
	f.write(res)