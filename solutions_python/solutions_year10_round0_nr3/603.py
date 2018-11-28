#!/usr/bin/python
t=int(raw_input())
for tt in range(t):
	money = 0
	par=raw_input().split()
	times = int(par[0])
	space = int(par[1])
	size = int(par[2])
	groups = [int(x) for x in raw_input().split()]

	while times>0:
		times-=1
		curspace=space
		ind = 0
		while(ind<size):
			if(curspace>=groups[ind]):
				curspace-=groups[ind]
				money+=groups[ind]
				ind+=1
			else:
				break
		while(ind>0):
			ind-=1
			groups.append(groups[0])
			groups=groups[1:]


	#print groups
	print "Case #"+str(tt+1)+":",money

