T = int(raw_input())

for index in range(T):
	N = int(raw_input())
	Naomi = map(float, raw_input().split())
	Ken = map(float, raw_input().split())
	Naomi.sort()
	Ken.sort()
	Naomi.reverse()
	Ken.reverse()
	NaomiNew = Naomi
	KenNew = Ken
	j, k, sumfirst = 0, 0, 0
	while j < N and k < N:
		if NaomiNew[j] > KenNew[k]:
			sumfirst = sumfirst + 1
			j = j + 1 
			k = k + 1
		else:
			while NaomiNew[j] < KenNew[k]:
				k = k + 1
				if k >= N:
					break
			if k < N:
				sumfirst = sumfirst + 1
			j = j + 1
			k = k + 1
	j, k, sumsecond = 0, 0, 0
	while j < N and k < N:
		if KenNew[j] > NaomiNew[k]:
			sumsecond = sumsecond + 1
			j = j + 1 
			k = k + 1
		else:
			while KenNew[j] < NaomiNew[k]:
				k = k + 1
				if k >= N:
					break
			if k < N:
				sumsecond = sumsecond + 1
			j = j + 1
			k = k + 1
	print "Case #" + str(index + 1) + ": " + str(sumfirst) + " " + str(N - sumsecond)