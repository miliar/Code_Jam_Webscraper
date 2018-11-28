f = open('input.txt', 'r')
w = open('output.txt', 'w')

testcase = f.readline()
caseth = 1

for line in f:
	l = line.rstrip().split(' ')
	maxSi = int(l[0])

	standed = 0
	requestMore = 0
	for i in range(0, maxSi + 1):
		si = int(l[1][i])
		if standed < i and si > 0:
			requestMore += (i - standed)
			standed = i
		standed += si

	#print('Case #' + str(caseth) + ': ' + str(requestMore))	
	w.write('Case #' + str(caseth) + ': ' + str(requestMore) + '\n')
	caseth += 1
	
