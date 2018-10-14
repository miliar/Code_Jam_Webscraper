def answer():
	data = raw_input().split(' ')
	stand = 0
	need = 0
	for i, n in enumerate(data[1]):
		if i > stand:
			need = (i-stand) if i-stand > need else need
		stand += int(n)
	
	return need
	
for i in range(input()):
	print "Case #%d: %d" % (i+1, answer())