base = {'Q':1,'W':1,'E':1,'R':1,'A':1,'S':1,'D':1,'F':1}

T = int(raw_input())
for i in range(T):
	# read each input line
	line = raw_input().split()
	index = 0
	C = int(line[index])
	combined = {}
	for j in range(C):
		index += 1
		combined[line[index][0:2]] = line[index][-1]
	index += 1
	D = int(line[index])
	opposed = {}
	for j in range(D):
		index += 1
		opposed[line[index][0]] = line[index][1]
		opposed[line[index][1]] = line[index][0]
	index += 1
	N = int(line[index])
	index += 1
	n_string = line[index]
	#print combined, opposed
	result = []
	for c in n_string:
		#print result, c	
		if (len(result) == 0) or (c not in base):
			result.append(c)
			continue
		# check combination
		token1 = result[-1]+c
		token2 = c+result[-1]
		token = None
		if token1 in combined:
			token = token1
		elif token2 in combined:
			token = token2
		if token != None:
			result.pop()
			result.append(combined[token])
			continue
		# check opposition
		if (c not in opposed) or (opposed[c] not in result):
			result.append(c)
			continue
		
		result = []
	
	print 'Case #%d: [%s]' % (i+1, ', '.join(result))