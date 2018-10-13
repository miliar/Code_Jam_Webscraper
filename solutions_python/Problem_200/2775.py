def tidy(N):
	N = [int(d) for d in str(N)]
	while(True):
		j=0;
		for i in range(len(N)-1):
			if N[i]>N[i+1]:
				N[i]-= 1
				N[i+1:len(N)] = (len(N)-j-1)*[9]
			else:
				j = j+1
		if(sorted(N)==N):
			break
	backtoint = lambda N: int(''.join(str(i) for i in N))
	N = backtoint(N)
	return N


t = int(raw_input())
for i in xrange(1,t+1):
	N = input()		
	result = tidy(N)
	print "Case #{}: {}".format(i,result)	
