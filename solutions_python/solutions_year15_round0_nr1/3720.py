i, o = open('A-small-attempt1.in','r'), open('A-small-output1.txt', 'w')
nCases = int(i.readline())
for case_num in range(nCases):
	tokens = i.readline().split()
	maxShyness = int(tokens[0])
	nString = tokens[1]
	totalClapping = 0
	necessaryAdds = 0
	for level in range(maxShyness+1):
		nShyLevel = int(nString[level])
		if level == 0:
			totalClapping += nShyLevel
		elif totalClapping >= level:
			totalClapping += nShyLevel
		else:
			if nShyLevel != 0:
				necessaryAdds += level - totalClapping
				totalClapping += necessaryAdds + nShyLevel
		print('case:', case_num+1, 'level:', level, 'nShyLevel', nShyLevel, 'totalClapping:', totalClapping, 'necessaryAdds:', necessaryAdds)
	o.write('Case #' + str(case_num+1) + ': ' + str(necessaryAdds)+'\n')
