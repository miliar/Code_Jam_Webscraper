T = int(raw_input())

for i in range(T):
	N = int(raw_input())
	Naomi = map(float, raw_input().split())
	Ken = map(float, raw_input().split())
	Naomi.sort()
	Ken.sort()
	Naomi.reverse()
	Ken.reverse()
	NaomiDW = Naomi
	KenDW = Ken
	j = 0
	k = 0
	count1 = 0
	count2 = 0

	while j < N and k < N:
		if NaomiDW[j] > KenDW[k]:
			count1 = count1 + 1
			j = j + 1 
			k = k + 1
		else:
			while NaomiDW[j] < KenDW[k]:
				k = k + 1
				if k >= N:
					break
			if k < N:
				count1 = count1 + 1
			j = j + 1
			k = k + 1
	
	j = 0
	k = 0
	count2 = 0

	while j < N and k < N:
		if KenDW[j] > NaomiDW[k]:
			count2 = count2 + 1
			j = j + 1 
			k = k + 1
		else:
			while KenDW[j] < NaomiDW[k]:
				k = k + 1
				if k >= N:
					break
			if k < N:
				count2 = count2 + 1
			j = j + 1
			k = k + 1

	print "Case #" + str(i + 1) + ": " + str(count1) + " " + str(N - count2)