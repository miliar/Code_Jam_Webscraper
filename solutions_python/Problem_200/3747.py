t = int(raw_input())
for i in range(1,t+1):
	number = int(raw_input())
	for j in range(number,-1,-1):
		strNumber = str(j)
		tidy = True
		for k in range(0,len(strNumber)-1):
			if strNumber[k] > strNumber[k+1]:
				tidy = False
				break
		if tidy:
			print "CASE #%d: %d" % (i,j)
			break


