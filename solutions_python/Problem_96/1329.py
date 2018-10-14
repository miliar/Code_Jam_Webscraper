
fIn = open('in.txt', 'rb')
fOut = open('out.txt', 'wb')

lIn = [map(int, line[:-1].split(' ')) for line in fIn][1:]
results = []
print lIn
for contest in lIn:
	N = contest[0]
	S = contest[1]
	p = contest[2]	
	upper = p * 3
	totalUnSup = 0
	totalSup = 0
	for score in contest[3:]:
		if score >= upper - 2 and score != 0:
			totalUnSup += 1
		elif score >= upper - 4 and score != 0:
			totalSup += 1
		'''
		maxUnSup = (score + 2) // 3
		maxSup = (score + 4) // 3
		if maxUnSup >= p and score != 0:
			totalUnSup += 1
		elif maxSup >= p and score != 0:
			totalSup += 1
		'''
	if p == 0:
		results.append(N)
	else:
		results.append(totalUnSup + min(S, totalSup))
for i, line in enumerate(results):
	fOut.write('Case #' + str(i+1) + ': ' + str(line) + '\n')
	print 'Case #' + str(i+1) + ': ' + str(line)


