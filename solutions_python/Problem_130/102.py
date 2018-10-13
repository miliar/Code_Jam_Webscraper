def guaranteed(N,P):
	pos = 0
	rank = 0
	size = pow(2,N-1)
	step = 2
	for i in range(N):
		if(P<pos+size): return rank
		pos += size
		rank += step
		size /= 2
		step *= 2
	return pow(2,N)-1
def possible(N,P):
	pos = 0
	rank = 0
	size = 1
	step = pow(2,N-1)
	for i in range(N):
		if(P<pos+size): return rank
		pos += size
		rank += step
		step /= 2
		size *= 2
	return pow(2,N)-1
# N = 3
# for p in range(pow(2,N)):
# 	print str(guaranteed(N,p)) + " " + str(possible(N,p))


T = int(raw_input())
for t in range(T):
	N,P = raw_input().split(' ')
	N = int(N)
	P = int(P)
	# print "N " + str(N)
	# print "P " + str(P)
	print "Case #" + str(t+1) + ": " + str(guaranteed(N,P-1)) + " " + str(possible(N,P-1))	