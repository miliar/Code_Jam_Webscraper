cases = input()

for n in range( 1, cases + 1 ):
	line = raw_input()
	
	n1, n2 = (s for s in line.split())
	n2 = list(n2)
	
	stood = 0
	invite = 0
	for i in range(len(list(n2))):			
		if i > stood:			
			invite += i - stood
			stood = i + int(n2[i])
		else:
			stood += int(n2[i])
	
	print "Case #" + repr(n) + ":",
	print invite
	