import sys

sys.stdin.readline()
numLine = 1



for line in sys.stdin:

	N = int(line)
	text = str(N)
	tidy = False
	fallo = 0

	while not tidy:

#		print N

		if N < -10:
			break
		
		candidate = True
		
		for i,char in enumerate(text[:-1]):
#			if numLine == 1:
#				print int(char), int(text[i+1])
			if int(char) > int(text[i+1]):
				candidate = False
				fallo = i
				break

		if candidate == True:
			tidy = True
		else:
			if fallo < len(text)-1:
				N -= int(text[fallo+1:])

			N -= 1
			text = str(N)

	print 'Case #' + str(numLine) + ': ' + str(N)

	numLine +=1
