def solve(n,sofar,dig,prev):
	if dig<0:
		return sofar
	for i in range(9,prev-1,-1):
		if sofar+i*(10**dig)<=n:
			s = solve(n,sofar+i*(10**dig),dig-1,i)
			if s>0:
				return s
	return -1

numruns = int(input())
for run in range(numruns):
	n = int(input())
	print('Case #'+str(run+1)+': '+str(solve(n,0,len(str(n))-1,0)))