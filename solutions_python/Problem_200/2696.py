import sys
cases=input()
for case in xrange(1, cases+1):
	line=sys.stdin.readline().strip()
	N = map(int, list(line))
	if len(N)>1 and int(line)<>0:
		for i in xrange(0, len(N)-1):
			if N[i+1] < N[i]:
				N[i]=N[i]-1
				for j in xrange(i+1, len(N)):
					N[j]=9
				break
		
		for k in xrange(i-1, -1, -1):
			if N[k] > N[k+1]:
				N[k] = N[k]-1
				N[k+1] = 9
		solution=int("".join(map(str, N)))
	else:
		solution=N[0]
	print "Case #%s:" % case, solution
	


