for t in xrange(int(raw_input())): # each test case
	out = []
	bases = ''
	combination = ''
	opposed = ''
	inline = raw_input().split()
	index= 0
	if inline[index] == '0':
		index+=1
	else:
		index+=1
		bases = inline[index]
		index+=1
	if inline[index] == '0':
		index+=1
	else: 
		index+=1
		opposed=inline[index]
		index+=1
	index += 1#skip number
	list = inline[index]
	
	if (bases != ''):
		combination = bases[2]
		bases = bases[:2]
	
	out.append(list[0])
	
	for char in xrange(1,len(list)):
		out.append(list[char])
		if (sorted(bases) == sorted(out[-2:])): #combine
			out.pop()
			out.pop()
			out.append(combination)
		if (len(opposed) != 0):
			if ((opposed[0] in out) and (opposed[1] in out)):
				out = []
		
	
	print "Case #"+str(t+1)+": "+"[" + ', '.join(out) + "]"	