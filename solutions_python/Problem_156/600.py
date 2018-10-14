
T=int(raw_input().strip())
for t in range(T):
	N=int(raw_input().strip())
	diners=map(int,raw_input().strip().split())
	res=1000
	for max_h in range(1,1001):
		curr_special=0
		for diner in diners:
			curr_special+=(diner-1)//max_h
		res=min(res,curr_special+max_h)

	print "Case #"+str(t+1)+": "+str(res)