T = int(raw_input())

for i in range(T):
	D,N = raw_input().split()
	D = int(D)
	N = int(N)

	the_time = 0

	for j in range(N):
		K,S = raw_input().split()
		K = int(K)
		S = int(S)

		rem_dist = D - K
		rem_time = rem_dist / float(S)

		if(rem_time > the_time):
			the_time = rem_time

	my_time = D / float(the_time)

	print 'Case #' + str(i+1) + ': ' + str(my_time)