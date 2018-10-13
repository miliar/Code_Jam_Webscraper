def solver(line):
	l, sequence = line.split()[1:], []
	for i in xrange(0,len(l),2):
		sequence.append((l[i], int(l[i+1])))
	
	prevB, prevO = 1, 1
	timeB, timeO, time = 0, 0, 0
	
	for next in sequence:
		if next[0] == 'O':
			step = abs(prevO-next[1]) + 1
			prevO = next[1]
			timeO = max(timeO + step, timeB + 1)
			time = timeO
		else:
			step = abs(prevB-next[1]) + 1
			prevB = next[1]
			timeB = max(timeB + step, timeO + 1)
			time = timeB
	
	return str(time)		
		
f = open("test.out", 'w')
cases = open("test.in", 'r').readlines()[1:]
for i in range(0, len(cases)):
	line = "Case #" + str(i+1) + ": " + solver(cases[i])
	print line
	f.write(line + "\n")
f.close()