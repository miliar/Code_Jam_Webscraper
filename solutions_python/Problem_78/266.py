

fp = open('A-small-attempt2.in', 'r')
#fp = open('input', 'r')
n = int(fp.next())

case = 1

for line in fp:
	result = False
	line = [int(x) for x in line.split()]
	
	#print line
	
	if line[2] == 100:
		if line[1] == 100: result = True
	elif line[2] == 0:
		if line[1] == 0: result = True
	else:
		for x in range(line[0] + 1):
			if x == 0 and line[1] not in [0, 100]:
				continue
			#print x, x * line[1], (x * line[1]) % 100
			if (x * line[1]) % 100 == 0:
				#print x, x * line[1]
				result = True
				break
	
	print 'Case #' + str(case) + ':',
	
	if result:
		print 'Possible'
	else:
		print 'Broken'
	
	case += 1

	#break
	
