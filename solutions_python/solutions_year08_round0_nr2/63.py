import sys

from heapq import heappush, heappop

problemset = sys.argv[1]
inf = file('B-'+problemset+'.in')
outf = file('B-'+problemset+'.out','w')

N = int(inf.readline()) # Number of test cases
for testcase in xrange(N):
	T = int(inf.readline()) # Turn-around time
	(NA,NB) = map(int,inf.readline().split(' ')) # Trips to A, and to B
	
	A=[]
	B=[]
	for x in xrange(NA):
		(s,e) = [map(int,y.strip().split(':')) for y in inf.readline().split(' ')]
		A.append((s[0]*60+s[1],e[0]*60+e[1]+T))
	for x in xrange(NB):
		(s,e) = [map(int,y.strip().split(':')) for y in inf.readline().split(' ')]
		B.append((s[0]*60+s[1],e[0]*60+e[1]+T))
	A.sort()
	B.sort()
	
	(SSA,SSB) = (0,0) # Starting at A,B
	(SA,SB) = (0,0) # Available at A,B
	GA = [] # Heap of trains arriving at A
	GB = [] # Heap of trains arriving at A
	C = 0 # Current time
	
	while A or B: # Still trains to go
		if not A or (B and (B[0][0] < A[0][0])):
			# B leaving next
			Z = B.pop(0)
			C = Z[0]
			while GA and (GA[0] <= C):
				SA += 1
				heappop(GA)
			while GB and (GB[0] <= C):
				SB += 1
				heappop(GB)
				
			if SB > 0: SB -= 1
			else: SSB += 1
			heappush(GA,Z[1])
			
		else:
			# A leaving next
			Z = A.pop(0)
			C = Z[0]
			while GA and (GA[0] <= C):
				SA += 1
				heappop(GA)
			while GB and (GB[0] <= C):
				SB += 1
				heappop(GB)
		
			if SA > 0: SA -= 1
			else: SSA += 1
			heappush(GB,Z[1])
			
	print >> outf, "Case #"+str(testcase+1)+": "+str(SSA)+" "+str(SSB)
