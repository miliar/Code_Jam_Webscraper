T = int(raw_input())
def fee(e,o):
	return N*(e-o)-(e-o)*(e-o-1)/2
for cas in range(1,T+1):
	N,M = map(int,raw_input().split())
	cost1=0
	cost2=0
	xx=[]
	s=set();
	for i in range(M):
		o,e,p=map(int,raw_input().split())
		cost1+=fee(e,o) * p
		xx += [(o,e,p)]
		s.add(o)
		s.add(e)
	ss = sorted(list(s))
	mp = {}
	for i in range(len(ss)):
		mp[ss[i]]=i

	pa = [0] * (len(ss)+10)
	for o,e,p in xx:
		oo=mp[o]
		ee=mp[e]
		for i in range(oo,ee):
			pa[i]+=p
	#print pa
	for i in range(len(ss)):
		while pa[i]>0:
			x=i;
			mn=pa[i]
			while pa[x]!=0 and x<len(ss):
				mn=min(mn,pa[x])
				x+=1
			for j in range(i,x):
				pa[j]-=mn;
	#		print ss[x],ss[i]
			cost2+=fee(ss[x],ss[i])*mn
	#		print ">>",i,x,mn
	#print pa
	#print xx


	print "Case #%d:" % cas,cost1-cost2
