
fileout = open('output.out', 'w')
filein = open('C-small.in', 'r')


T = int(filein.readline()) #Number of cases
for i in range(T):
	res = filein.readline().split(' ')
	people = int(res[1])
	N_stalls = int(res[0])

	Rs = list()
	Ls = list()
	stalls = list()

	for x in range(N_stalls + 2):
		Ls.append(0)
		Rs.append(0)
		stalls.append(0)

	stalls[0] = 2000
	stalls[-1] = 2000

	for person in range(people):
		counter = 0
		for stall in range(len(stalls)):
			if(stalls[stall] == 2000):
				counter = 0
				Ls[stall] = 0
			else:
				counter += 1
				Ls[stall] = counter

		counter = 0
		for stall in range(len(stalls)-1, -1, -1):
			if(stalls[stall] == 2000):
				counter = 0
				Rs[stall] = 0
			else:
				counter += 1
				Rs[stall] = counter
		maxLsRs = 0
		minLsRs = 0
		minind = -1
		for index in range(len(Ls)):
			if(min(Ls[index], Rs[index]) > maxLsRs):
				minind = index
				maxLsRs = min(Ls[index], Rs[index])
				minLsRs = max(Ls[index], Rs[index])
			elif(min(Ls[index], Rs[index]) == maxLsRs):
				if(minLsRs < max(Ls[index], Rs[index])):
					minind = index
					maxLsRs = min(Ls[index], Rs[index])
					minLsRs = max(Ls[index], Rs[index])					

		stalls[minind] = 2000

	result = str(Rs[minind]-1) + ' ' + str(Ls[minind]-1)

	fileout.write('Case #'+str(i+1)+': '+str(result)+'\n')
	print('Case #'+str(i+1)+': '+str(result)+'\n')
