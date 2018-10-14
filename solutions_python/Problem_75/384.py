import sys
T=int(sys.stdin.readline().strip())
for t in range(1,T+1):
	nums=sys.stdin.readline().strip().split(' ')
	C=int(nums[0])
	comb={}
	des={}
	for i in range(C):
		comb[(nums[i+1][0],nums[i+1][1])]=nums[i+1][2]
		comb[(nums[i+1][1],nums[i+1][0])]=nums[i+1][2]
	D=int(nums[C+1])
	for i in range(D):
		des[(nums[i+C+2][0],nums[i+C+2][1])]=1
		des[(nums[i+C+2][1],nums[i+C+2][0])]=1
	N=int(nums[-2])
	s=nums[-1]
	L=[]
	for e in s:
		L.append(e)
		while len(L)>1:
			if comb.has_key((L[-1],L[-2])):
				c=comb[(L[-1],L[-2])]
				L.pop()
				L.pop()
				L.append(c)
			else:
				for e1 in L:
					if des.has_key((L[-1],e1)):
						L=[]
						break
				break
		
					
	print "Case #%d: [%s]" % (t,", ".join(L))
