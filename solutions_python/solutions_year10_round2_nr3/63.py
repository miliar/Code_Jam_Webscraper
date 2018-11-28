consec_cache = {}
def consec(N, F, T):
	if N==0: return 1
	elif N==1: return T-F-1
	else:
		global consec_cache
		if not (N,F,T) in consec_cache:
			s = 0
			for k in xrange(F+1,T-1):
				s += consec(N-1, k, T)
			consec_cache[(N,F,T)] = s
		return consec_cache[(N,F,T)]

# To N, starting with S
def calc(N,S):
	if N==S: return 1
	M = S + S-1
	D = S-2
	P = S
	print 'N='+str(N),'starting with',S,'minimum',M
	total = 0
	for k in range(M,N+1):
		C = consec(D,S,k) # number of numbers, leaving k at M
		print 'Place',k,'consec='+str(C)
		if k == N: total += C
		else:
			calced = calc(N,k)
			print 'Add calc('+str(N)+','+str(k)+')','=',calced
			total += calced
			pass
	return total

# Number of ways to put M at position P to get N
# POS, PUT, NUM
ways_cache = {}
def ways(P, M, N):
	global ways_cache
	if M == N: return 1
	if not (P,M,N) in ways_cache:
		total = 0
		# What can we put at position M
		smallest = M+M-P
		for k in xrange(smallest,N+1):
			ans = ways(M, k, N)
			#print " - Number of ways to put",k,"at",M,"to get",N,"=",ans
			total += consec(M-P-1,M,k) * ans
		ways_cache[(P,M,N)] = total
	return ways_cache[(P,M,N)]
		

	

def run(C,N):
	total = 0
	for k in xrange(N,1,-1):
		ans = ways(1, k, N)
		#print "Number of ways to put",k,"at",1,"to get",N,"=",ans
		total += ways(1, k, N)
		#print 'ADD',c
	print 'Case #'+str(C)+': '+str(total%100003)

for C in xrange(int(raw_input())):
	q = int(raw_input())
	run(C+1,q)

