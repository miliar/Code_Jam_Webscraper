# Train Script
import math

class Test:
	def dfs(self, id, k):
		if id==len(self.g) and k[0]<=k[1]: return 1
		for i in range(len(self.l[id])):
			if self.vis[id][i]==1: continue
			else: 
				a0=max(k[0],int(math.ceil(self.l[id][i]*1.0/1.1/self.g[id])))
				b0=min(k[1],int(math.floor(self.l[id][i]*1.0/0.9/self.g[id])))
				if a0>b0: continue
				self.vis[id][i]=1
				c0=self.dfs(id+1,[a0,b0])
				if c0==1: return 1
				self.vis[id][i]=0
		return 0

	def solve(self):
		T=input()
		for zz in range(T):
			self.N,self.P=[int(i) for i in raw_input().split(' ')]
			self.g=[int(i) for i in raw_input().split(' ')]
			self.l=[]
			for i in range(self.N): 
				self.l+=[[int(j) for j in raw_input().split(' ')]]
				self.l[i].sort()
			self.ans=0
			self.vis=[[0]*self.P for i in range(self.N)]
			for i in range(self.P):
				self.ans+=self.dfs(0,[-1,1000000000])
			print 'Case #%d: %d'%(zz+1,self.ans)
			
if __name__ == "__main__":
	t=Test()
	t.solve()