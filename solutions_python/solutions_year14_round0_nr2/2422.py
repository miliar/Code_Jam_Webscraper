class cookie:
	def __init__(self,sent_c,sent_f,sent_x):
		self.C=sent_c
		self.F=sent_f
		self.X=sent_x
		self.cps=2.0
		self.wait_cost=0.0

	def isForwardBetter(self):
		current_goal_cost = self.X/self.cps
		self.wait_cost = self.C/self.cps
		forward_goal_cost = self.X/(self.cps+self.F)
		forward_cost = self.wait_cost+forward_goal_cost
		return current_goal_cost>forward_cost

	def get_min_time(self):
		total_cost=0.0
		while(self.isForwardBetter()):
			total_cost+=self.wait_cost
			self.cps+=self.F
		total_cost+=(self.X/self.cps)
		return total_cost

file=open("B-large.in","r")
total_cases=int(file.readline().split()[0])

for i in xrange(1,total_cases+1):
	c,f,x=file.readline().split()
	c=float(c)
	f=float(f)
	x=float(x)

	temp=cookie(c,f,x)
	print "Case #"+str(i)+": "+str(temp.get_min_time())
	del temp
file.close()
