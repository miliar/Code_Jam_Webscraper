# -*- coding: utf-8 -*-

import sys

class Dancing:
	def solve(self,n,s,p,params):
		#print"\nn:%d,s:%d,p:%d,params:%s"%(n,s,p,params)
		ans=0
		cand=0

		for total in params:
			a=int(total/3)
			if(total%3==1):
				if a+1>=p:
					ans+=1
			else:
				if(total%3==0):
					min_best = a
					if a==0 or a==10:
						max_best = min_best
					else:
						max_best = min_best+1
						
				elif(total%3==2):
					min_best = a+1
					if a==9:
						max_best = min_best
					else:
						max_best = min_best+1
										
				min_best=max(min_best,0)
				max_best=min(max_best,10)

				if max_best < p or min_best >= p:
					if max_best >= p:
						ans+=1
				elif max_best >= p and min_best < p:
					#print "increase cand."
					cand+=1
			#print "min_best:%d,max_best:%d"%(min_best,max_best)
		ans+=min(s,cand)
		return ans
		

dancing=Dancing()

f=open(sys.argv[1])
f2=open(sys.argv[2],'w')

lines=f.read().split('\n')

for idx in range(int(lines[0])):
	params = [int(param) for param in (lines[idx+1]).split(' ')]
	n=params.pop(0)
	s=params.pop(0)
	p=params.pop(0)
	ans = dancing.solve(n,s,p,params)
	f2.write("Case #%d: %d\n"%(idx+1,ans))
f2.close
