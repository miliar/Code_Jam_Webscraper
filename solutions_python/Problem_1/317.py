
def process():

	# First, translate each SE into a number

	S = int(raw_input())
	SEnames = {}

	for i in range(0,S):
		x = raw_input()
		SEnames[x] = i
	
	Q = int(raw_input())
	query = []
	for i in range(0,Q):
		x = raw_input()
		query.append(SEnames[x])
	
	# Now, do the processing

	A = set(range(0, len(SEnames)))
	#RET = []
	RET = 0
	i = 0
	for line in query:
		i += 1
		if line in A:
			if len(A) == 1:
				#RET.append((i, line))
				# Commented out cause we need only a number of switches
				A = set(range(0, len(SEnames)))
				RET += 1
			
			A.remove(line)

	#if A:
	#	RET.append((-1, A.pop()))
	return RET


N = int(raw_input())

for i in range(1,N+1):
	print 'Case #%i:'%i, process()
